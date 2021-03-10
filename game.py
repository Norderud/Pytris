from shapes import I, J, L, O, S, T, Z
import random as r


class Square:
    def __init__(self, rect):
        self.state = 0
        self.color = (0, 0, 0)
        self.rect = rect


class Game:
    def __init__(self, width, height):
        self.grid = self.init_grid(width, height)
        self.active_piece = self.random_shape()
        self.CENTER = 5

    def init_grid(self, width, height):
        grid = []
        for y in range(0, height):
            line = []
            grid.append(line)
            for x in range(0, width):
                rect = (x, y, 30, 30)
                line.append(Square(rect))
        return grid

    def move_right(self):
        for c in self.active_piece.squares:
            if c[0] >= 9:
                return
            if self.grid[c[1]][c[0]+1].state == 2:
                return
        
        self.active_piece.move_right()
        self.draw_active_piece()

    def move_left(self):
        for c in self.active_piece.squares:
            if self.grid[c[1]][c[0]-1].state == 2 or c[0] <= 0:
                return
        self.active_piece.move_left()
        self.draw_active_piece()

    def move_down(self):
        self.active_piece.move_down()

        if self.active_piece.squares[-1][1] >= 19:
            self.place_active_piece()

        for c in self.active_piece.squares:
            if self.grid[c[1]+1][c[0]].state == 2 or c[1] >= 19:
                self.place_active_piece()
                break
        self.draw_active_piece()

    def rotate(self):
        self.active_piece.rotate()

            

    def random_shape(self):
        shapes = {
            0: I(self.CENTER),
            1: J(self.CENTER),
            2: L(self.CENTER),
            3: O(self.CENTER),
            4: S(self.CENTER),
            5: T(self.CENTER),
            6: Z(self.CENTER)

        }
        return shapes.get(r.randint(0, len(shapes)-1))

    def draw_active_piece(self):
        for row in self.grid:
            for s in row:
                if s.state == 1:
                    s.state = 0
                    s.color = (0, 0, 0)
        for square in self.active_piece.squares:
            self.grid[square[1]][square[0]].state = 1
            self.grid[square[1]][square[0]].color = self.active_piece.color

    def place_active_piece(self):
        for square in self.active_piece.squares:
            self.grid[square[1]][square[0]].state = 2
            self.grid[square[1]][square[0]].color = self.active_piece.color
        self.active_piece = self.random_shape()
        self.check_rows()

    def check_rows(self):
        for i, row in enumerate(self.grid):
            if self.row_is_full(row):
                self.remove_line(i)

    def row_is_full(self, row):
        is_full = True
        for square in row:
            if square.state == 0:
                is_full = False
        return is_full

    def remove_line(self, idx):
        del self.grid[idx]
        self.grid.insert(0, [Square((i*30, 0, 30, 30)) for i in range(10)])
