from utils import player, boardState

class TicTacToeMatrix():
    def __init__(self, id):
        self.__id = id
        self.__matrix = [
            [0, 0, 0], 
            [0, 0, 0], 
            [0, 0, 0]
            ]
        self.__winner = ''
    def setInput(self, xval, yval, isX):  # Added self parameter
        if isX:
            self.__matrix[xval][yval] = player.PLAYER_X.value #X
        else:
            self.__matrix[xval][yval] = player.PLAYER_O.value #O
    # Getters and setters
    def getMatrix(self):
        return self.__matrix
    def getWinner(self):
        return self.__winner
    def setWinner(self, winner):
        self.__winner = winner

    def getId(self):
        return self.__id
    
    # Check if three in a row, column or diagonal or if full 
    def checkIfThreeRow(self):
        # Check if three in a row 
        for i in range(3):
            res = sum(self.__matrix[i])
            if res == 3:
                return player.PLAYER_X.value  #X
            elif res == 12:
                return player.PLAYER_O.value #O
        return 0
    def checkIfThreeCol(self):
        # Check if three in a column
        for i in range(3):
            res = self.__matrix[0][i] + self.__matrix[1][i] + self.__matrix[2][i]
            if res == 3:
                return player.PLAYER_X.value #X
            elif res == 12:
                return player.PLAYER_O.value #O
        return 0
    def checkIfThreeDiag(self):
        # Check if three in a diagonal
        res = self.__matrix[0][0] + self.__matrix[1][1] + self.__matrix[2][2]
        if res == 3:
            return player.PLAYER_X.value #X
        elif res == 12:
            return player.PLAYER_O.value #O
        res = self.__matrix[0][2] + self.__matrix[1][1] + self.__matrix[2][0]
        if res == 3:
            return player.PLAYER_X.value  #X
        elif res == 12:
            return player.PLAYER_O.value #O
        return 0
    def checkIfFull(self):
        for i in range(3):
            for j in range(3):
                if self.__matrix[i][j] == 0:
                   return
        return boardState.DRAW.value
    # 🤨🤨🤨🤨🤨🤨❤️❤️❤️❤️❤️❤️🤣🤣🤣🤣🤣🤣🤣🤣💕👌😘
    # Check if win or draw
    def checkWin(self):
        res = self.checkIfThreeRow()
        print('1', res)
        if res == player.PLAYER_X.value or res == player.PLAYER_O.value:
            self.setWinner(res)
            return boardState.WIN.value
        res = self.checkIfThreeCol()
        print('2', res)
        if res == player.PLAYER_X.value or res == player.PLAYER_O.value:
            self.setWinner(res)
            return boardState.WIN.value
        res = self.checkIfThreeDiag()
        print('3', res)
        if res == player.PLAYER_X.value or res == player.PLAYER_O.value:
            self.setWinner(res)
            return boardState.WIN.value
        return boardState.PENDING.value
    
class UltimateTicTacToe:

    def __init__(self):
        self.ttcMap = {
            "00": TicTacToeMatrix('00'),
            "01": TicTacToeMatrix('01'),
            "02": TicTacToeMatrix('02'),
            "10": TicTacToeMatrix('10'),
            "11": TicTacToeMatrix('11'),
            "12": TicTacToeMatrix('12'),
            "20": TicTacToeMatrix('20'),
            "21": TicTacToeMatrix('21'),
            "22": TicTacToeMatrix('22')
        }
        self.__matrix = [
            [self.ttcMap['00'], self.ttcMap['01'], self.ttcMap['02']],
            [self.ttcMap['10'], self.ttcMap['11'], self.ttcMap['12']],
            [self.ttcMap['20'], self.ttcMap['21'], self.ttcMap['22']]
            ]
        self.__boardState = boardState.PENDING.value
        self.__winner = ''

    def setInput(self, xval, yval, isX, tableIdX, tableIdY):
        if isX:
            self.__matrix[tableIdX][tableIdY].setInput(xval, yval, True)
        else:
            self.__matrix[tableIdX][tableIdY].setInput(xval, yval, False)
    # Getters and setters
    def getMatrix(self):
        return self.__matrix