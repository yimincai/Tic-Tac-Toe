import random

board = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
playerALetter = ''
playerBLetter = ''
switchPlayerCounter = 1

def drawBoard(board):

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Do you want to be X or O ? ').upper()
        global playerALetter
        global playerBLetter

        if letter == 'X':
            playerALetter = 'X'
            playerBLetter = 'O'

        if letter == 'O':
            playerALetter = 'O'
            playerBLetter = 'X'

def switchPlayer():
    global switchPlayerCounter
    switchPlayerCounter = switchPlayerCounter + 1

def currentPlayer():
    if switchPlayerCounter % 2 == 1:
        return playerALetter
    else:
        return playerBLetter

def playAgain():
    global board
    board = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    switchPlayerCounter = 1


def isWinner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[7] == letter and board[4] == letter and board[1] == letter) or
    (board[8] == letter and board[5] == letter and board[2] == letter) or
    (board[9] == letter and board[6] == letter and board[3] == letter) or
    (board[7] == letter and board[5] == letter and board[3] == letter) or
    (board[9] == letter and board[5] == letter and board[1] == letter))

def boardIsFull():
    return (board[1] != '1' and
    board[2] != '2' and
    board[3] != '3' and
    board[4] != '4' and
    board[5] != '5' and
    board[6] != '6' and
    board[7] != '7' and
    board[8] != '8' and
    board[9] != '9')

while True:
    inputPlayerLetter()
    print(currentPlayer(), ' will go first!')
    drawBoard(board)
    gameIsPlaying = True

    while gameIsPlaying:
        print('Choose the number you want to draw', currentPlayer(), ' : ')
        drawNumber = int(input())
        num = drawNumber

        if not board[num] == 'O' or board[num] == 'X':
            board[num] = currentPlayer()
            drawBoard(board)
            if isWinner(board, currentPlayer()):
                print(currentPlayer(), ' have won the game!!')
                playAgain()
                gameIsPlaying = False
            elif boardIsFull():
                print('No winner, tie!')
                playAgain()
                gameIsPlaying = False
            switchPlayer()
        else:
            print('The number you selected is already occupied, please try again later.')