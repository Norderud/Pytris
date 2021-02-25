from shapes import I, J, L, O, S, T, Z
import random as r


class Square:
    def __init__(self, rect):
        self.state = 0
        self.rect = rect


class Grid:

    def load_grid(self, width, height):
        table = []
        for y in range(0, height):
            line = []
            table.append(line)
            for x in range(0, width):
                rect = (x, y, 30, 30)
                line.append(Square(rect))
        return table

    def __init__(self, width, height):
        self.table = self.load_grid(width, height)
        self.x = 0
        self.y = 5
        self.active_piece = J(5)

    def move_right(self):
        self.active_piece.move_right()

    def move_left(self):
        self.active_piece.move_left()

    def move_down(self):
        self.active_piece.move_down()
        if self.active_piece.active_cells[-1][1] >= 19:
            self.place_active_piece()

        for c in self.active_piece.active_cells:
            if self.table[c[1]+1][c[0]].state == 2:
                self.place_active_piece()

    def random_shape(self):
        return {
            0: I(5),
            1: J(5),
            2: L(5),
            3: O(5),
            4: S(5),
            5: T(5),
            6: Z(5)

        }.get(r.randint(0, 6))

    def draw_active_piece(self):
        for row in self.table:
            for s in row:
                if s.state == 1:
                    s.state = 0

        for e in self.active_piece.active_cells:
            self.table[e[1]][e[0]].state = 1

    def place_active_piece(self):
        for e in self.active_piece.active_cells:
            self.table[e[1]][e[0]].state = 2
        self.active_piece = self.random_shape()
        self.check_lines()

    def row_is_full(self, row):
        is_full = True
        s = ""
        for square in row:
            s += str(square.state)
            if square.state == 0:
                is_full = False
        print(s)
        return is_full

    def remove_line(self, idx):
        del self.table[idx]
        self.table.insert(0, [Square((i*30, 0, 30, 30)) for i in range(10)])

    def check_lines(self):
        for i, row in enumerate(self.table):
            if self.row_is_full(row):
                self.remove_line(i)
