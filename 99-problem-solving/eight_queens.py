
class EightQueens:
    def __init__(self) -> None:
        self.board = [[0]*8 for i in range(8)]
        self.counter = 0

    def is_attacked(self, row, col):
        c_left = col - row
        c_right = col + row
        for i in range(row):
            if self.board[i][col] == 1:
                return True
            if c_left > -1 and self.board[i][c_left] == 1:
                return True
            if c_right < 8 and self.board[i][c_right] == 1:
                return True
            c_left += 1
            c_right -= 1
        return False

    def find_solution(self, row):
        if row == 8:
            self.counter += 1
            print("Solution", self.counter)
            self.print_board()
            return
        else:
            for col in range(8):
                if col == 8:
                    return
                if not self.is_attacked(row, col):
                    self.board[row][col] = 1
                    self.find_solution(row + 1)
                    self.board[row][col] = 0



    def print_board(self):
        for row in self.board:
            print(row)


queens = EightQueens()
queens.find_solution(0)