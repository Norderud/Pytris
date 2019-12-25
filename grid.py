class Square:
    def __init__(self, rect):
        self.is_active = False
        self.rect = rect


class Grid:
    def load_grid(self, width, height):
        table = []
        for x in range(0, width):
            line = []
            table.append(line)
            for y in range(0, height):
                rect = (x*30, y*30, 30, 30)
                line.append(Square(rect))
        return table

    def __init__(self, width, height):
        self.table = self.load_grid(width, height)
        self.x_pos = 0
        self.y_pos = 5
    
    

    def move_right(self):
        if self.x_pos == 9:
            pass
        else:
            self.x_pos += 1
            self.table[self.x_pos][self.y_pos].is_active = True
            self.table[self.x_pos-1][self.y_pos].is_active = False

    def move_left(self):
        if self.x_pos == 0:
            pass
        else:
            self.x_pos -= 1
            self.table[self.x_pos][self.y_pos].is_active = True
            self.table[self.x_pos+1][self.y_pos].is_active = False

    def move_down(self):
        if self.y_pos == 19 or self.table[self.x_pos][self.y_pos+1].is_active == True:
            self.y_pos = 0
            self.x_pos = 5
            self.check_lines()
        else:
            self.y_pos += 1
            self.table[self.x_pos][self.y_pos].is_active = True
            self.table[self.x_pos][self.y_pos-1].is_active = False

    def row_is_full(self, row):
        all_active = True
        for square in row:
            if not square.is_active:
                all_active = False
        return all_active

    def remove_line(self, idx):
        self.table.remove(idx)
        line = [Square((i*30, 0, 30, 30)) for i in range(10)]
        self.table.insert(0, line)

    def check_lines(self):
        for i, row in enumerate(self.table):
            for square in row:
                print(square.is_active)
            # if self.row_is_full(row):
            #     self.remove_line(i)
