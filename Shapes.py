class Shape:
    def __init__(self, start_x):
        self.x = start_x
        self.y = 0
        self.active_cells = [[self.x, self.y]]

    def move_down(self):
        self.y += 1
        for y in self.active_cells:
            y[1] += 1
    
    def move_right(self):
        self.x += 1
        for x in self.active_cells:
            x[0] += 1

    def move_left(self):
        self.x -= 1
        for x in self.active_cells:
            x[0] -= 1

class I(Shape):
    def __init__(self, start_x):
        print(start_x)
        super().__init__(start_x)
        self.active_cells.extend([[self.x, self.y+1], [self.x, self.y+2], [self.x, self.y+3]])
    


class J(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.active_cells.extend([[self.x, self.y+1], [self.x, self.y+2], [self.x-1, self.y+2]])


class L(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.active_cells.extend([[self.x, self.y+1], [self.x, self.y+2], [self.x+1, self.y+2]])


class O(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.active_cells.extend([[self.x, self.y+1], [self.x+1, self.y], [self.x+1, self.y+1]])
        


class S(Shape):
    def __init__(self):
        pass


class T(Shape):
    def __init__(self):
        pass


class Z(Shape):
    def __init__(self):
        pass


if __name__ == '__main__':
    i = I(0)

    print(i.active_cells)
    i.move_down()
    print(i.active_cells)
    i.move_right()
    print(i.active_cells)


