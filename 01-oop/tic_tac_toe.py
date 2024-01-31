

class TicTacToe:
    def __init__(self) -> None:
        self.player = 'X'
        self.board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]

    def print_board(self):
        for row in range(3):
            for col in range(3):
                print(self.board[row][col], end=' ')
            print()

    def play(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Row or Col out of range")
        elif self.board[row][col] != '-':
            print("Position already taken")
        else:
            self.board[row][col] = self.player
            self.player = 'X' if self.player == 'O' else 'O'

    def get_winner(self):
        # Exercise 1: find if there is a winner and return its symbol, if not return None
        return None
    
    def is_tie(self):
        # Exercise 2: find if it is a Tie
        return False


game = TicTacToe()
while True:
    print(game.player, "plays")
    game.print_board()
    row = int(input("Row: "))
    col = int(input("Col: "))
    game.play(row, col)
    winner = game.get_winner()
    if winner is not None:
        print(winner, "wins!")
        break
    if game.is_tie():
        print("It is a Tie")
        break
