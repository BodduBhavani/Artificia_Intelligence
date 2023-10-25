import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def generate_computer_move(board, player):
    magic_square = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    best_score, best_move = float('-inf'), None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                score = sum(magic_square[row][col] * (board[row][col] == player) - magic_square[row][col] for row in range(3) for col in range(3) if board[row][col] != " ")
                if score > best_score:
                    best_score, best_move = score, (i, j)
                board[i][j] = " "

    return best_move

def play_game():
    while True:
        board, players = [[" "]*3 for _ in range(3)], ["X", "O"]
        print("Welcome to Tic Tac Toe!\n")
        first_player = input("Who should play first (X - Human, O - Computer), 'X' or 'O'? ").upper()
        if first_player not in ["X", "O"]:
            print("Invalid input. Defaulting to 'X' as starting player.")
            first_player = "X"
        current_player = first_player

        while True:
            print_board(board)
            if current_player == "X":
                row, col = map(int, input("Enter row (0-2) and column (0-2) separated by space: ").split())
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    board[row][col] = current_player
                else:
                    print("Invalid move. Try again.")
                    continue
            else:
                print("Computer's turn...")
                row, col = generate_computer_move(board, current_player)
                board[row][col] = current_player

            if check_win(board, current_player):
                print_board(board)
                print(f"{current_player} wins!")
                break
            elif all(cell != " " for row in board for cell in row):
                print_board(board)
                print("It's a draw!")
                break
            current_player = "X" if current_player == "O" else "O"

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

play_game()
