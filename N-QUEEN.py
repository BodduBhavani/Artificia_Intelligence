def printSolution(board):
    for row in board:
        print(" ".join(map(str, row)))

def isSafe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col + 1):
                return True
            board[i][col] = 0

    return False

def solveNQ():
    print("The problem is to try to place eight queens on a chessboard so that none of them are attacking any of the other")
    print("Remember that the queen can move as far as she likes vertically, horizontally or diagonally.")
    print("You can't place two queens in the same row")
    
    n = int(input("Enter the size of the chessboard: "))
    board = [[0] * n for _ in range(n)]

    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False

    print("Solution:")
    printSolution(board)
    return True

# Driver program
solveNQ()
