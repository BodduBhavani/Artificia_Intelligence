import random

class TicTacToe:
    def __init__(self):
        self.magic_square = [8, 3, 4, 1, 5, 9, 6, 7, 2]
        self.current_player = ""
        self.game_over = False
        self.board = [" " for _ in range(9)]

    def print_board(self):
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]} ")
            if i < 6:
                print("---+---+---")

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.check_winner()
            self.check_draw()
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("That cell is already taken. Try again.")

    def make_computer_move(self):
        empty_cells = [i for i, cell in enumerate(self.board) if cell == " "]
        if empty_cells:
            random_position = random.choice(empty_cells)
            magic_position = self.magic_square[random_position] - 1
            self.make_move(magic_position)

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for condition in win_conditions:
            a, b, c = condition
            if self.board[a] == self.board[b] == self.board[c] != " ":
                print(f"Player {self.current_player} wins!")
                self.game_over = True

    def check_draw(self):
        if " " not in self.board and not self.game_over:
            print("It's a draw!")
            self.game_over = True

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        play_again = True

        while play_again:
            self.board = [" " for _ in range(9)]
            self.current_player = ""
            self.game_over = False

            player_choice = input("Choose your symbol (X/O): ").upper()
            while player_choice not in ["X", "O"]:
                player_choice = input("Invalid choice. Choose X or O: ").upper()

            self.current_player = player_choice

            while not self.game_over:
                self.print_board()

                if self.current_player == "X":
                    position = int(input(f"Player {self.current_player}, enter position (1-9): ")) - 1
                    if position >= 0 and position < 9:
                        magic_position = self.magic_square[position] - 1
                        self.make_move(magic_position)
                    else:
                        print("Invalid position. Try again.")
                else:
                    print(f"Computer's turn ({self.current_player})")
                    self.make_computer_move()

            self.print_board()
            play_again = input("Do you want to play again? (yes/no): ").lower() == "yes"


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
