import random


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True


def printingBoard(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-----")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-----")
    print(board[8]+"|"+board[7]+"|"+board[6])
    print("-----")


def playerInput(board):
    inp = int(input("Enter a number 1-9 "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("OOP's incorrect Option")


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner = board[6]
        return True
    else:
        return False


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[3]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    else:
        return False


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    else:
        return False


def checkTie(board):
    if "-" not in board and (CheckDiagonal != True and checkRow != True and checkHorizontal != True):
        printingBoard(board)
        print("It's a TIE!!!")
        gameRunning = False
        resetGame(board)


def CheckWinner():
    global winner
    if checkDiagonal(board) or checkRow(board) or checkHorizontal(board):
        print(f"The Winner is {winner}")
        resetGame(board)
        return True


def TogglePlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def resetGame(board):
    printingBoard(board)
    playerInput(board)


def Computer():
    while currentPlayer == "O":
        pos = random.randint(0, 8)
        if board[pos] == "-":
            board[pos] = "O"
            TogglePlayer()


while gameRunning:
    printingBoard(board)
    playerInput(board)
    CheckWinner()
    checkTie(board)
    TogglePlayer()
    Computer()
