import random

class MinesweeperCell:
    def __init__(self):
        self.has_mine = False
        self.is_open = False

    def get_as_string(self):
        if not self.is_open:
            return '#'
        elif self.has_mine:
            return '*'
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

    def print_all_cells(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.board[y][x].get_as_string(), end="")
            print()

#testing
if __name__ == "__main__":
    board = MinesweeperBoard(10, 10)
    board.place_mines(10)
    board.open_all()
    board.print_all_cells()
