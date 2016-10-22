import random

class MinesweeperCell:
    def __init__(self):
        self.has_mine = False
        self.is_open = False
        self.n_adjacent_mines = 0

    def get_as_string(self):
        if not self.is_open:
            return '#'
        elif self.has_mine:
            return '*'
        elif self.n_adjacent_mines is not 0:
            return str(self.n_adjacent_mines)
        else:
            return '.'


class MinesweeperBoard:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.board = [[MinesweeperCell() for x in range(width)] 
                    for y in range(height)]

    def open_cell(self, x, y):
        self.board[x][y].is_open = True
        
    def open_all(self):
        for y in range(self.height):
            for x in range(self.width):
                self.open_cell(x, y)

    def place_mines(self, n_mines):
        for i in range(n_mines):
            while True:
                x = random.randrange(0, self.width)
                y = random.randrange(0, self.height)
                if not self.board[y][x].has_mine:
                    break
            self.board[y][x].has_mine = True
            self._increase_adjacent_mine_counts(x, y)

    def print_all_cells(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.board[y][x].get_as_string(), end="")
            print()

    def _is_valid_coord(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def _increase_adjacent_mine_counts(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self._is_valid_coord(y + i, x + j):
                    self.board[y + i][x + j].n_adjacent_mines = \
                    self.board[y + i][x + j].n_adjacent_mines + 1


#testing
if __name__ == "__main__":
    board = MinesweeperBoard(10, 10)
    board.place_mines(10)
    board.open_all()
    board.print_all_cells()
