# Make the Board and Variables

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

X = input("Player 1's name: ")
O = input("Player 2's name: ")
currentPlayer = X
currentshape = "X"
playerWinner = None
GameOn = True
# print board

def makeBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# Player inputs number from 1-9
# Non number inputs
# make sure you don't switch turns if its an invalid input

def inputPosition(board):
    print(f"{currentPlayer}'s turn")
    try:
        playerInput = int(input("Play by choosing a number 1-9: "))
        if type(playerInput) == int:
            if playerInput >= 1 and playerInput <= 9 and board[playerInput - 1] == "-":
                board[playerInput - 1] = currentshape
            elif playerInput <= 0 or playerInput >= 10:
                not switchTurns()
                print("That number isn't allowed in Tac Tac Toe!")
            else:
                not switchTurns()
                print("That position is already taken.\n")
    except ValueError:
        not switchTurns()
        print("Sorry, you need to input a number!")


# Look to see if game has been won or tied yet from all three directions.


def checkAcross(board):
    global playerWinner
    if board[0] == board[1] == board[2] and board[0] != "-":
        playerWinner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        playerWinner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        playerWinner = board[6]
        return True


def CheckVertical(board):
    global playerWinner
    if board[0] == board[3] == board[6] and board[0] != "-":
        playerWinner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        playerWinner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        playerWinner = board[2]
        return True


def checkDiagonal(board):
    global playerWinner
    if board[0] == board[4] == board[8] and board[0] != "-":
        playerWinner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        playerWinner = board[2]
        return True


# If there are no dashes on the board and no player has won, it is a tie.
def tieGame(board):
    global GameOn
    if "-" not in board:
        makeBoard(board)
        print("The game has finished in a tie.")
        GameOn = False
    return


# If there is a playerWinner, function outputs the name of the player
def wonGame():
    global GameOn
    if CheckVertical(board) or checkAcross(board) or checkDiagonal(board):
        if playerWinner == "X":
            print(f"The Winner is {X}!")
        elif playerWinner == "O":
            print(f"The Winner is {O}!")
        makeBoard(board)
        GameOn = False
    return


# switch player for each turn

def switchTurns():
    global currentPlayer
    global currentshape
    if currentPlayer == X:
        currentshape = "O"
        currentPlayer = O
    else:
        currentshape = "X"
        currentPlayer = X


# check for win or tie again

def play():
    while GameOn:
        makeBoard(board)
        inputPosition(board)
        wonGame()
        tieGame(board)
        switchTurns()


# Play Again

while True:
    play()

    # Ask player if they want to play another game
    if input("\nWould you like to Play Again? (yes/no): ") == "no":
        break
    else:
        # Clean gameboard
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]

        # Clean variables
        currentPlayer = X
        currentshape = "X"
        playerWinner = None
        GameOn = True