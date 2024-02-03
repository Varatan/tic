from utils import player, boardState

def checkGlobalWinOrDraw(finishedBoards):
    globalMatrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]
    for k,v in finishedBoards.items():
        globalMatrix[int(k[0])][int(k[1])] = v
    res = checkIfThreeRow(globalMatrix)
    if res == player.PLAYER_X.value or res == player.PLAYER_O.value:
        print(res)
        return {'boardState': boardState.WIN.value, 'res': res}
    res = checkIfThreeCol(globalMatrix)
    if res == player.PLAYER_X.value or res == player.PLAYER_O.value:
        print(res)
        return {'boardState': boardState.WIN.value, 'res': res}
    res = checkIfThreeDiag(globalMatrix)
    if res == player.PLAYER_X.value or res == player.PLAYER_O.value:
        print(res)
        return {'boardState': boardState.WIN.value, 'res': res} 
    res = checkIfFull(globalMatrix)
    if res == boardState.DRAW.value:
        return {'boardState': boardState.DRAW.value, 'res': res}
    return {'boardState': boardState.PENDING.value, 'res': 0}

def checkIfThreeRow(globalMatrix):
    # Check if three in a row 
    print('3row', globalMatrix)
    for i in range(3):
        res = sum(globalMatrix[i])
        if res == 3:
            return player.PLAYER_X.value  #X
        elif res == 12:
            return player.PLAYER_O.value #O
    return 0

def checkIfThreeCol(globalMatrix):
    # Check if three in a column
    for i in range(3):
        res = globalMatrix[0][i] + globalMatrix[1][i] + globalMatrix[2][i]
        if res == 3:
            return player.PLAYER_X.value #X
        elif res == 12:
            return player.PLAYER_O.value #O
    return 0

def checkIfThreeDiag(globalMatrix):
    # Check if three in a diagonal
    res = globalMatrix[0][0] + globalMatrix[1][1] + globalMatrix[2][2]
    if res == 3:
        return player.PLAYER_X.value #X
    elif res == 12:
        return player.PLAYER_O.value #O
    res = globalMatrix[0][2] + globalMatrix[1][1] + globalMatrix[2][0]
    if res == 3:
        return player.PLAYER_X.value  #X
    elif res == 12:
        return player.PLAYER_O.value #O
    return 0

def checkIfFull(globalMatrix):
    for i in range(3):
        for j in range(3):
            if globalMatrix[i][j] == 0:
                return
    return boardState.DRAW.value