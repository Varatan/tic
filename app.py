#.venv\Scripts\activate
#flask run --debug
from flask import Flask, render_template, session, redirect, url_for, request
from flask_session import Session
from tempfile import mkdtemp
from tictactoe import TicTacToeMatrix, UltimateTicTacToe
from utils import player, boardState
from checkGlobalWin import checkGlobalWinOrDraw

app = Flask(__name__)

app.config['SESSION_FILE_DIR'] = mkdtemp() #Where to put files
app.config['SESSION_PERMANENT'] = False #Is session permanent
app.config['SESSION_TYPE'] = 'filesystem' #What type of session

Session(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        session.clear()
        uttc = {}
        return redirect(url_for('index'))

    uttc = UltimateTicTacToe()
    if 'board' not in session:
        session['tictactoe'] = uttc
        session['board'] = uttc.getMatrix()
        session['turn'] = 'X'
        session['activeBoards'] = ['11']
        session['finishedBoards'] = {}
        session['allActive']= ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    print(session['tictactoe'])
    return render_template('base.html', game=session['board'],turn=session['turn'], activeBoards=session['activeBoards'], finishedBoards=session['finishedBoards'])

@app.route("/make_turn/")
def make_turn():
    payloadMap ={
        "row": request.args.get('x'),
        "col": request.args.get('y'),
        "turn": request.args.get('trn'),
        "matId": request.args.get('matId')
    }
    if(payloadMap['turn'] == 'X'):
        session['board'][int(payloadMap['matId'][0])][int(payloadMap['matId'][1])].setInput(int(payloadMap['row']), int(payloadMap['col']), True)
        session['turn'] = 'O'
    else:
        session['board'][int(payloadMap['matId'][0])][int(payloadMap['matId'][1])].setInput(int(payloadMap['row']), int(payloadMap['col']), False)
        session['turn'] = 'X'
    finished = False

    if session['board'][int(payloadMap['matId'][0])][int(payloadMap['matId'][1])].checkWin() == boardState.WIN.value:
        finishedBoards = session['finishedBoards']
        winner = session['board'][int(payloadMap['matId'][0])][int(payloadMap['matId'][1])].getWinner()
        finishedBoards[payloadMap['matId']] = winner
        session['finishedBoards'] = finishedBoards
        
        # removing finished board from activeBoards
        allActive = session['allActive']
        allActive.remove(payloadMap['matId'])
        session['allActive'] = allActive
        finished = True
    
    if session['board'][int(payloadMap['matId'][0])][int(payloadMap['matId'][1])].checkIfFull() == boardState.DRAW.value and finished == False:
        finishedBoards = session['finishedBoards']
        finishedBoards[payloadMap['matId']] = 999
        session['finishedBoards'] = finishedBoards

        # removing finished board from activeBoards
        allActive = session['allActive']
        print(payloadMap['matId'])
        try:
            allActive.remove(payloadMap['matId'])
        except ValueError:
            redirect(url_for('winner', result=1,  winner = 0))
        session['allActive'] = allActive

    #modifyingActiveBoards
    if session['finishedBoards'].get(f'{payloadMap["row"]}{payloadMap["col"]}'):
        session['activeBoards'] = session['allActive']
    else:
        session['activeBoards'] = [f'{payloadMap["row"]}{payloadMap["col"]}']

    print('finishedBoards', session['finishedBoards'])
    
    x = checkGlobalWinOrDraw(session['finishedBoards'])
    globalRes = x['boardState']
    globalWin = x['res']

    if globalRes in [boardState.WIN.value,boardState.DRAW.value]:
        return redirect(url_for('winner', result=globalRes,  winner = globalWin))
    else:
        return redirect(url_for('index'))
    
    

@app.route("/winner/<int:result>/<int:winner>")
def winner(result, winner ):
    return render_template('winner.html', winner = winner, result = result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12128, debug=True)