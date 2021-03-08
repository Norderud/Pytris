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

    def rotate(self):
        center_cell = self.active_cells[1]
        x_offset = center_cell[0] - (-center_cell[1])
        y_offset = center_cell[1] - center_cell[0]

        for cell in self.active_cells:
            temp = cell[0] + y_offset
            cell[0] = -cell[1] + x_offset
            cell[1] = temp


class I(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.active_cells.extend(
            [[self.x, self.y+1], [self.x, self.y+2], [self.x, self.y+3]])

        self.color = (255, 0, 0)


class J(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.active_cells.extend(
            [[self.x, self.y+1], [self.x, self.y+2], [self.x-1, self.y+2]])
        self.color = (255, 69, 0)


class L(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.active_cells.extend(
            [[self.x, self.y+1], [self.x, self.y+2], [self.x+1, self.y+2]])
        self.color = (255, 255, 0)


class O(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.active_cells.extend(
            [[self.x, self.y+1], [self.x+1, self.y], [self.x+1, self.y+1]])
        self.color = (255, 0, 255)


class S(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.active_cells.extend(
            [[self.x, self.y+1], [self.x+1, self.y], [self.x-1, self.y+1]])
        self.color = (0, 255, 0)


class Z(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.active_cells.extend(
            [[self.x, self.y+1], [self.x-1, self.y], [self.x+1, self.y+1]])
        self.color = (128, 0, 128)


class T(Shape):
    def __init__(self, start_x):
        super().__init__(start_x)
        self.active_cells.extend(
            [[self.x, self.y+1], [self.x-1, self.y+1], [self.x+1, self.y+1]])
        self.color = (0, 0, 255)
