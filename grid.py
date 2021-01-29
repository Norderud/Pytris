from shapes import I

class Square:
    def __init__(self, rect):
        self.is_active = False
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
        self.active_piece = I(0)


    def move_right(self):
        self.active_piece.move_right()
        
    def move_left(self):
        self.active_piece.move_left()

    def move_down(self):
        self.active_piece.move_down()


    def row_is_full(self, row):
        is_full = True
        s = ""
        for square in row:
            s += "1" if square.is_active else "0"
            if not square.is_active:
                is_full = False
        print(s)
        return is_full

    def draw_active_piece(self):
        for e in self.active_piece.active_cells:
            self.table[e[1]][e[0]].is_active = True
                
    def remove_line(self, idx):
        del self.table[idx]
        self.table.insert(0, [Square((i*30, 0, 30, 30)) for i in range(10)])

    def check_lines(self):
        for i, row in enumerate(self.table):
            if self.row_is_full(row):
                self.remove_line(i)
