from shapes import I, J, L, O, S, T, Z
import random as r


class Square:
    def __init__(self, rect):
        self.state = 0
        self.color = (0, 0, 0)
        self.rect = rect


class Grid:

    def load_game(self, width, height):
        table = []
        for y in range(0, height):
            line = []
            table.append(line)
            for x in range(0, width):
                rect = (x, y, 30, 30)
                line.append(Square(rect))
        return table

    def __init__(self, width, height):
        self.table = self.load_game(width, height)
        self.active_piece = self.random_shape()

    def move_right(self):
        for c in self.active_piece.active_cells:
            if c[0] >= 9:
                return
        self.active_piece.move_right()
        self.draw_active_piece()

    def move_left(self):
        for c in self.active_piece.active_cells:
            if c[0] <= 0:
                return
        self.active_piece.move_left()
        self.draw_active_piece()

    def move_down(self):
        self.active_piece.move_down()

        if self.active_piece.active_cells[-1][1] >= 19:
            self.place_active_piece()

        for c in self.active_piece.active_cells:
            if self.table[c[1]+1][c[0]].state == 2 or c[1] >= 19:
                self.place_active_piece()
                break
        self.draw_active_piece()

    def rotate_active_piece(self):
        self.active_piece.rotate()

    def random_shape(self):
        start_x = 5
        shapes = {
            0: I(start_x),
            1: J(start_x),
            2: L(start_x),
            3: O(start_x),
            4: S(start_x),
            5: T(start_x),
            6: Z(start_x)

        }
        return shapes.get(r.randint(0, len(shapes)-1))

    def draw_active_piece(self):
        for row in self.table:
            for s in row:
                if s.state == 1:
                    s.state = 0
                    s.color = (0, 0, 0)
        for cell in self.active_piece.active_cells:
            self.table[cell[1]][cell[0]].state = 1
            self.table[cell[1]][cell[0]].color = self.active_piece.color

    def place_active_piece(self):
        for cell in self.active_piece.active_cells:
            self.table[cell[1]][cell[0]].state = 2
            self.table[cell[1]][cell[0]].color = self.active_piece.color
        self.active_piece = self.random_shape()
        self.check_lines()

    def row_is_full(self, row):
        is_full = True
        for square in row:
            if square.state == 0:
                is_full = False
        return is_full

    def remove_line(self, idx):
        del self.table[idx]
        self.table.insert(0, [Square((i*30, 0, 30, 30)) for i in range(10)])

    def check_lines(self):
        for i, row in enumerate(self.table):
            if self.row_is_full(row):
                self.remove_line(i)
