import random

def TicTacToe():
    print("Welcome to Tic Tac Toe game!")

    def PrintBoard():
        print()
        print('', board[0], "|", board[1], "|", board[2])
        print("---|---|---")
        print('', board[3], "|", board[4], "|", board[5])
        print("---|---|---")
        print('', board[6], "|", board[7], "|", board[8])
        print()

    def GetRow():
        while True:
            row = input("Choose row (1, 2, 3): ")
            if row in ['1', '2', '3']:
                return int(row)
            else:
                print("\nInvalid input. Choose row between 1 and 3.")

    def GetColumn():
        while True:
            column = input("Choose column (1, 2, 3): ")
            if column in ['1', '2', '3']:
                return int(column)
            else:
                print("\nInvalid input. Choose column between 1 and 3.")

    def GetNumber():
        while True:
            number = input()
            try:
                number = int(number)
                if number in range(1, 10):
                    return number
                else:
                    print("\nNumber not on board")
            except ValueError:
                print("\nThat's not a number. Try again")
                continue

    def getBoardCopy(board):
        dupeBoard = []
        for i in board:
            dupeBoard.append(i)
        return dupeBoard

    def isSpaceFree(board1, move):
        return board1[move - 1] == ' '

    def makeMove(board1, letter, move):
        board1[move - 1] = letter

    def chooseRandomMoveFromList(board, movesList):
        possibleMoves = []
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def computerchoice():
        for i in range(1, 10):
            copy = getBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, 'O', i)
                if CheckWin(copy, 'O'):
                    return i
        for i in range(1, 10):
            copy = getBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, 'X', i)
                if CheckWin(copy, 'X'):
                    return i
        if isSpaceFree(board, 5):
            return 5
        move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
        if move != None:
            return move
        return chooseRandomMoveFromList(board, [2, 4, 6, 8])

    def Turn(player):
        placing_index = GetNumber() - 1
        if board[placing_index] == "X" or board[placing_index] == "O":
            print("\nBox already occupied. Try another one")
            Turn(player)
        else:
            board[placing_index] = player

    def Turn1(move):
        board[move - 1] = 'O'

    def CheckWin(board1, player):
        for x in range(9):
            for y in range(9):
                for z in range(9):
                    if x != y and y != z and z != x:
                        if board1[x] == player and board1[y] == player and board1[z] == player:
                            if MagicSquare[x] + MagicSquare[y] + MagicSquare[z] == 15:
                                return True
        return False  # Return False if no winning combination is found

    def isBoardFull(board):
        count = 0
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
        if count == 9:
            print("The game ends in a Tie\n")
            return True

    print("Who plays first? (C for Computer / H for Human):")
    first_player = input().upper()

    while True:
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        MagicSquare = [4, 9, 2, 3, 5, 7, 8, 1, 6]


        if first_player == 'C':
            while True:
                PrintBoard()
                end = CheckWin(board, "O")
                if end:
                    print("Computer wins the game")
                    break
                else:
                    if isBoardFull(board):
                        break
                move = computerchoice()
                Turn1(move)
                PrintBoard()
                end = CheckWin(board, "X")
                if end:
                    print("You win the game")
                    break
                else:
                    if isBoardFull(board):
                        break
                print("Choose a box player X")
                row = GetRow()
                column = GetColumn()
                if board[(row - 1) * 3 + column - 1] == "X" or board[(row - 1) * 3 + column - 1] == "O":
                    print("\nBox already occupied. Try another one")
                    continue
                else:
                    board[(row - 1) * 3 + column - 1] = "X"

        elif first_player == 'H':
            while True:
                PrintBoard()
                row = GetRow()
                column = GetColumn()
                if board[(row - 1) * 3 + column - 1] == "X" or board[(row - 1) * 3 + column - 1] == "O":
                    print("\nBox already occupied. Try another one")
                    continue
                else:
                    board[(row - 1) * 3 + column - 1] = "X"
                PrintBoard()
                end = CheckWin(board, "X")
                if end:
                    print("You win the game")
                    break
                else:
                    if isBoardFull(board):
                        break
                move = computerchoice()
                Turn1(move)
                PrintBoard()
                end = CheckWin(board, "O")
                if end:
                    print("Computer wins the game")
                    break
                else:
                    if isBoardFull(board):
                        break

        # ...

        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != 'Y':
            break

TicTacToe()
