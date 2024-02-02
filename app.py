#.venv\Scripts\activate
#flask run --debug
from flask import Flask, render_template, session, redirect, url_for, request
from flask_session import Session
from tempfile import mkdtemp
from tictactoe import TicTacToeMatrix, UltimateTicTacToe
from utils import player, boardState

app = Flask(__name__)

app.config['SESSION_FILE_DIR'] = mkdtemp() #Directory gdzie beda zapisywane pliki
app.config['SESSION_PERMANENT'] = False #Czy sesja permenentna
app.config['SESSION_TYPE'] = 'filesystem' #Jakiego typu sesja

Session(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        print('graj od nowa button')
        session.clear()
        uttc = {}
        return redirect(url_for('index'))

    uttc = UltimateTicTacToe()
    if 'board' not in session:
        session['tictactoe'] = uttc
        session['board'] = uttc.getMatrix()
        # session['boardstate'] = uttc.getBoardState()
        session['turn'] = 'X'
        session['winner'] = ''
    print(session['tictactoe'])
    return render_template('base.html', game=session['board'],turn=session['turn'], winner=session['winner'])

@app.route("/make_turn/<int:row>/<int:col>/<string:turn>")
def make_turn(row, col, turn, tableid):
    print(row,col,turn)
    if(turn == 'X'):
        session[f'tictactoe{tableid}'].setInput(row, col, True)
        print
        session['turn'] = 'O'
    else:
        session['tictactoe'].setInput(row, col, False)
        session['turn'] = 'X'

    if (session['tictactoe'].checkWin() == boardState.WIN.value):
        print('wchodzisz tu?')
        print('boardState', session['tictactoe'].getBoardState())
        return redirect(url_for('winner'))
    
    if(session['tictactoe'].checkIfFull() == boardState.DRAW.value):
        print('wchodzisz tu?')
        print('boardState', session['tictactoe'].getBoardState())
        return redirect(url_for('winner'))
    return redirect(url_for('index'))
    
    

@app.route("/winner")
def winner():
    winner = session['tictactoe'].getWinner()
    endState = session['tictactoe'].getBoardState()
    return render_template('winner.html', winner = winner, endState = endState)