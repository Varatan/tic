#.venv\Scripts\activate
#flask run
from flask import Flask, render_template, session, redirect,url_for
from flask_session import Session
from tempfile import mkdtemp
from tictactoe import TicTacToeMatrix
from utils import playerMap, boardStateMap

app = Flask(__name__)

app.config['SESSION_FILE_DIR'] = mkdtemp() #Directory gdzie będą zapisywane pliki
app.config['SESSION_PERMANENT'] = False #Czy sesja permenentna
app.config['SESSION_TYPE'] = 'filesystem' #Jakiego typu sesja

Session(app)

@app.route("/")
def index():
    ttc = TicTacToeMatrix()
    if 'board' not in session:
        session['tictactoe'] = ttc
        session['board'] = ttc.matrix
        session['boardstate'] = ttc.boardState
        session['turn'] = 'X'
        session['winner'] = ''
    game = session['board']
    return render_template('base.html', game=session['board'],turn=session['turn'], winner=session['winner'])

@app.route("/make_turn/<int:row>/<int:col>/<string:turn>")
def make_turn(row, col, turn):
    print(row,col,turn)
    if(turn == 'X'):
        session['tictactoe'].setInput(row, col, True)
        print
        session['turn'] = 'O'
    else:
        session['tictactoe'].setInput(row, col, False)
        session['turn'] = 'X'

    session['tictactoe'].checkWin()
    session['tictactoe'].checkIfFull()
    if (session['boardstate'] == boardStateMap['WIN']):
        return redirect(url_for('winner'))
    return redirect(url_for('index'))
    
    

@app.route("/winner")
def winner():
    return render_template('winner.html')