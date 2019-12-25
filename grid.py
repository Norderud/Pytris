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
    

    def l_piece(self):
        self.table[self.y][self.x].is_active = True
        self.table[self.y][self.x-1].is_active = True
        self.table[self.y][self.x-2].is_active = True
        self.table[self.y+1][self.x].is_active = True

   

    def move_right(self):
        if self.x == 9:
            pass
        if  self.x == 9 or self.table[self.y][self.x+1].is_active:
            pass
        else:
            self.x += 1
            self.table[self.y][self.x].is_active = True
            self.table[self.y][self.x-1].is_active = False

    def move_left(self):
        if self.x == 0:
            pass
        if self.table[self.y][self.x-1].is_active:
            pass
        else:
            self.x -= 1
            self.table[self.y][self.x].is_active = True
            self.table[self.y][self.x+1].is_active = False

    def move_down(self):
        if self.y == 19 or self.table[self.y+1][self.x].is_active == True:
            self.y = 0
            self.x = 5
            self.check_lines()
        else:
            self.y += 1
            self.table[self.y][self.x].is_active = True
            self.table[self.y-1][self.x].is_active = False


    def row_is_full(self, row):
        is_full = True
        s = ""
        for square in row:
            s += "1" if square.is_active else "0"
            if not square.is_active:
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