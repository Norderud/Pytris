class Shape:
    def __init__(self, start_x):
        self.x = start_x
        self.y = 0
        self.squares = [[self.x, self.y]]
        self.center_square = self.squares[0]

    def move_down(self):
        for y in self.squares:
            y[1] += 1

    def move_right(self):
        for x in self.squares:
            x[0] += 1

    def move_left(self):
        for x in self.squares:
            x[0] -= 1

    def rotate(self):
        x_offset = self.center_square[0] - (-self.center_square[1])
        y_offset = self.center_square[1] - self.center_square[0]

        for square in self.squares:
            temp = square[0] + y_offset
            square[0] = -square[1] + x_offset
            square[1] = temp


class I(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.squares.extend(
            [[self.x, self.y+1], [self.x, self.y+2], [self.x, self.y+3]])
        self.center_square = self.squares[1]
        self.color = (255, 0, 0)


class J(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.squares.extend(
            [[self.x, self.y+1], [self.x, self.y+2], [self.x-1, self.y+2]])
        self.center_square = self.squares[1]
        self.color = (255, 69, 0)


class L(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.squares.extend(
            [[self.x, self.y+1], [self.x, self.y+2], [self.x+1, self.y+2]])
        self.center_square = self.squares[1]
        self.color = (255, 255, 0)


class O(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.squares.extend(
            [[self.x, self.y+1], [self.x+1, self.y], [self.x+1, self.y+1]])
        self.color = (255, 0, 255)
    
    def rotate(self):
        pass


class S(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.squares.extend(
            [[self.x, self.y+1], [self.x+1, self.y], [self.x-1, self.y+1]])
        self.center_square = self.squares[1]
        self.color = (0, 255, 0)


class Z(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.squares.extend(
            [[self.x, self.y+1], [self.x-1, self.y], [self.x+1, self.y+1]])
        self.center_square = self.squares[1]
        self.color = (128, 0, 128)


class T(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.squares.extend(
            [[self.x, self.y+1], [self.x-1, self.y+1], [self.x+1, self.y+1]])
        self.center_square = self.squares[1]
        self.color = (0, 0, 255)
