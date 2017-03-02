# Tic Tac Toe

import random


def drawBoard(board, gridSize):
    # This function prints out the board that it was passed.
    if gridSize==3:
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')
    
    if gridSize==4:
        # "board" is a list of 17 strings representing the board (ignore index 0)
        print('   |   |   |')
        print(' ' + board[13] + ' | ' + board[14] + ' | ' + board[15] + ' | ' + board[16])
        print('   |   |   |')
        print('-----------')
        print('   |   |   |')
        print(' ' + board[9] + ' | ' + board[10] + ' | ' + board[11] + ' | ' + board[12])
        print('   |   |   |')
        print('-----------')
        print('   |   |   |')
        print(' ' + board[5] + ' | ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
        print('   |   |   |')
        print('-----------')
        print('   |   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ' + board[4])
        print('   |   |   |')

def inputPlayMode():
    # Allows the player to select the mode of play i.e., vs User or Computer
    mode = ''
    while not(mode == 'Computer' or mode == 'User'):
        print('Do you want to play against a Computer or User?')
        print('Enter 1 for Computer, 2 for User')
        mode = input().upper()

        if mode == '1':
            return 1
        else:
            return 2

def inputPlayerLetter(modeofPlay):
    # Lets the player type which letter they want to be.
    letter = ''
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    if modeofPlay == 1:    
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']
    elif modeofPlay == 2:
        while not (letter == 'X' or letter == 'O'):
            print('Enter letter of choice X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the Player 2's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst(modeofPlay):
    # Randomly choose the player who goes first.
    if modeofPlay == 1:
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player 1'
    elif modeofPlay == 2:
        if random.randint(0, 1) == 0:
            return 'player 1'
        else:
            return 'player 2'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter
        

def isWinner(bo, le, gridSize):
    if gridSize == 3:
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
    
    if gridSize == 4:
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[13] == le and bo[14] == le and bo[15] == le and bo[16] == le) or # across the top
        (bo[9] == le and bo[10] == le and bo[11] == le and bo[12] == le) or # across the middle
        (bo[5] == le and bo[6] == le and bo[7] == le and bo[8] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le and bo[4] == le) or # across the bottom
        (bo[13] == le and bo[9] == le and bo[5] == le and bo[1] == le) or # down the left side
        (bo[14] == le and bo[10] == le and bo[6] == le and bo[2] == le) or # down the middle
        (bo[15] == le and bo[11] == le and bo[7] == le and bo[3] == le) or # down the middle
        (bo[16] == le and bo[12] == le and bo[8] == le and bo[4] == le) or # down the right side
        (bo[13] == le and bo[10] == le and bo[7] == le and bo[4] == le) or # diagonal
        (bo[16] == le and bo[11] == le and bo[6] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board, gridSize):
    # Let the player type in his move.
    move = ' '
    if gridSize == 3:
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)
    
    if gridSize == 4:
        while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split() or not isSpaceFree(board, int(move)):
            print('Player 1! What is your next move? (1-16)')
            move = input()
        return int(move)

def getPlayer2Move(board, gridSize):
    # Let the player type in his move.
    move = ' '
    if gridSize == 3:
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    if gridSize == 4:
        while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split() or not isSpaceFree(board, int(move)):
            print('Player 2! What is your next move? (1-16)')
            move = input()
        return int(move)

def chooseRandomMoveFromList(board, movesList, level, gridSize):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    if level == 1:
        if gridSize == 3:
            movesList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if gridSize == 4:
            movesList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        return random.choice(movesList)
    if level == 2:
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

        
def getComputerMove(board, computerLetter, gridSize, level):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    if gridSize == 3:
        rNum = 10
    elif gridSize == 4:
        rNum = 17
    
    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, rNum):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter, gridSize):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, rNum):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter, gridSize):
                return i

                
    if gridSize == 3:
        # Try to take one of the corners, if they are free.
        move = chooseRandomMoveFromList(board, [1, 3, 7, 9], level, gridSize)
        if move != None:
            return move

        # Try to take the center, if it is free.
        if isSpaceFree(board, 5):
            return 5

        # Move on one of the sides.
        return chooseRandomMoveFromList(board, [2, 4, 6, 8], level, gridSize)
    
    if gridSize == 4:
        # Try to take one of the corners, if they are free.
        move = chooseRandomMoveFromList(board, [1, 4, 13, 16], level, gridSize)
        if move != None:
            return move

        # Try to take the center, if it is free.
        return chooseRandomMoveFromList(board, [6, 7, 10, 11], level, gridSize)

        # Move on one of the sides.
        return chooseRandomMoveFromList(board, [2, 3, 5, 8, 9, 12, 14, 15], level, gridSize)

def isBoardFull(board, gridSize):
    if gridSize==3:
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if isSpaceFree(board, i):
                return False
        return True
    
    if gridSize==4:
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 17):
            if isSpaceFree(board, i):
                return False
        return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    print("Choose the grid size:")
    print("Enter 3 for 3 * 3 ")
    print("Enter 4 for 4 * 4 ")
    gridSize = int(input())
    if (gridSize != 3 and gridSize!=4):
        print("Please enter a valid grid size, either 3 or 4")
        gridSize = int(input())
    
    if gridSize==3:
        theBoard = [' '] * 10
    if gridSize==4:
        theBoard = [' '] * 17
    
    modeofPlay = inputPlayMode()
    if modeofPlay == 1:
        print("Choose level")
        print("1. Beginner")
        print("2. Expert")
        level = int(input())
        if (level != 1 and level != 2):
            print("Please enter a valid grid size, either 1 or 2")
            level = int(input())
        playerLetter, computerLetter = inputPlayerLetter(modeofPlay)
        turn = whoGoesFirst(modeofPlay)
    elif modeofPlay == 2:
        playerLetter, player2Letter = inputPlayerLetter(modeofPlay)
        turn = whoGoesFirst(modeofPlay)

    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player 1':
            # Player's turn.
            drawBoard(theBoard, gridSize)
            move = getPlayerMove(theBoard, gridSize)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter, gridSize):
                drawBoard(theBoard, gridSize)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard, gridSize):
                    drawBoard(theBoard, gridSize)
                    print('The game is a tie!')
                    break
                else:
                    if modeofPlay == 2:
                        turn = 'player 2'
                    else:
                        turn = 'computer'

        elif turn == 'player 2':
            # Player's turn.
            drawBoard(theBoard, gridSize)
            move = getPlayer2Move(theBoard, gridSize)
            makeMove(theBoard, player2Letter, move)

            if isWinner(theBoard, player2Letter, gridSize):
                drawBoard(theBoard, gridSize)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard, gridSize):
                    drawBoard(theBoard, gridSize)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player 1'

        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter, gridSize, level)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter, gridSize):
                drawBoard(theBoard, gridSize)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard, gridSize):
                    drawBoard(theBoard, gridSize)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player 1'

    if not playAgain():
        break
