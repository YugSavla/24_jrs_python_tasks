def undoMove(log, xState, zState):
    if not log:
        print("No moves to undo!")
        return False
    lastMove = log.pop()
    if lastMove[1] == 1:
        xState[lastMove[0]] = 0
    else:
        zState[lastMove[0]] = 0
    return True