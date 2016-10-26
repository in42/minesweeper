import random

class MinesweeperCell:
    def __init__(self):
        self.has_mine = False
        self.is_open = False
        self.n_adj_mines = 0

    def __str__(self):
        if not self.is_open:
            return '#'
        elif self.has_mine:
            return '*'
        else:
            return '.'


class MinesweeperBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[MinesweeperCell() for c in range(width)] 
                    for r in range(height)]

    def open_all(self):
        for r in range(self.height):
            for c in range(self.width):
                self.board[r][c].is_open = True

    def place_mines(self, n_mines):
        for i in range(n_mines):
            while True:
                r = random.randrange(0, self.height)
                c = random.randrange(0, self.width)
                if not self.board[r][c].has_mine:
                    break
            self.board[r][c].has_mine = True
            self._increase_adjacent_mine_counts(r, c)

    def click_on_cell(self, r, c):
        self.board[r][c].is_open = True
        if self.board[r][c].has_mine:
            return False
        if self.board[r][c].n_adj_mines == 0:
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if (self._is_valid_coord(r + dr, c + dc) and
                        not self.board[r + dr][c + dc].is_open):
                        self.click_on_cell(r + dr, c + dc)

    def print_all_cells(self, show_mine_counts=True):
        print('  ', end='')
        for c in range(self.width):
            print(' ', end='')
            print(c, end='')
        print()
        for r in range(self.height):
            print(' ', end='')
            print(r, end='')
            for c in range(self.width):
                print(' ', end='')
                if (show_mine_counts and self.board[r][c].is_open and
                    self.board[r][c].n_adj_mines != 0):
                    print(self.board[r][c].n_adj_mines, end='')
                else:
                    print(self.board[r][c], end='')
            print()

    def _is_valid_coord(self, r, c):
        return 0 <= c < self.width and 0 <= r < self.height

    def _increase_adjacent_mine_counts(self, r, c):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self._is_valid_coord(r + i, c + j):
                    self.board[r + i][c + j].n_adj_mines = \
                    self.board[r + i][c + j].n_adj_mines + 1


#testing
if __name__ == "__main__":
    board = MinesweeperBoard(10, 10)
    board.place_mines(10)
    quit = False
    while not quit:
        board.print_all_cells()
        s = input('--> ')
        tokens = s.split(' ')
        if tokens[0] == 'q' or tokens[0] == 'quit':
            quit = True
        elif tokens[0] == 'c' or tokens[0] == 'click':
            board.click_on_cell(int(tokens[1]), int(tokens[2]))
        elif (tokens[0] == 's' or tokens[0] == 'show'):
            board.print_all_cells()
    # board.open_all()
    # board.print_all_cells()
