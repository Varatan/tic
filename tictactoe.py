from utils import playerMap, boardStateMap

class TicTacToeMatrix:
    def __init__(self):
        self.matrix = [
            [0, 0, 0], 
            [0, 0, 0], 
            [0, 0, 0]
            ]
        self.boardState = boardStateMap['PENDING']
        self.winner = 0
    def setInput(self, xval, yval, isX):  # Added self parameter
        if isX:
            self.matrix[xval][yval] = playerMap["PLAYER_X"] #X
        else:
            self.matrix[xval][yval] = playerMap["PLAYER_O"] #O
    def checkIfThreeRow(self):
        # Check if three in a row 
        for i in range(3):
            res = sum(self.matrix[i])
            if res == 3:
                return playerMap["PLAYER_X"]  #X
            elif res == 12:
                return playerMap["PLAYER_O"] #O
        return 0
    def checkIfThreeCol(self):
        # Check if three in a column
        for i in range(3):
            res = self.matrix[0][i] + self.matrix[1][i] + self.matrix[2][i]
            if res == 3:
                return playerMap["PLAYER_X"] #X
            elif res == 12:
                return playerMap["PLAYER_O"] #O
        return 0
    def checkIfThreeDiag(self):
        # Check if three in a diagonal
        res = self.matrix[0][0] + self.matrix[1][1] + self.matrix[2][2]
        if res == 3:
            return playerMap["PLAYER_X"] #X
        elif res == 12:
            return playerMap["PLAYER_O"] #O
        res = self.matrix[0][2] + self.matrix[1][1] + self.matrix[2][0]
        if res == 3:
            return playerMap["PLAYER_X"]  #X
        elif res == 12:
            return playerMap["PLAYER_O"] #O
        return 0
    def checkIfFull(self):
        # Check if matrix is full
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == 0:
                   self.boardState = boardStateMap['PENDING']
                   return
        self.boardState = boardStateMap['DRAW']
    def checkWin(self):
        res = self.checkIfThreeRow()
        print('1', res)
        if res == playerMap["PLAYER_X"] or res == playerMap["PLAYER_O"]:
            self.winner = res
            self.boardState = boardStateMap["WIN"]
            print('boardstate', self.boardState)
            return
        res = self.checkIfThreeCol()
        print('2', res)
        if res == playerMap["PLAYER_X"] or res == playerMap["PLAYER_O"]:
            self.winner = res
            self.boardState = boardStateMap["WIN"]
            return
        res = self.checkIfThreeDiag()
        print('3', res)
        if res == playerMap["PLAYER_X"] or res == playerMap["PLAYER_O"]:
            self.winner = res
            self.winner = res
            self.boardState = boardStateMap["WIN"]
            return