import pygame


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
        self.y_pos = 0

    def move_right(self):
        if self.x_pos == 9:
            pass
        else:
            self.x_pos += 1
            self.table[self.x_pos][self.y_pos].is_active = not grid.table[self.x_pos][self.y_pos].is_active
            self.table[self.x_pos-1][self.y_pos].is_active = False

    def move_left(self):
        if self.x_pos == 0:
            pass
        else:
            self.x_pos -= 1
            self.table[self.x_pos][self.y_pos].is_active = not grid.table[self.x_pos][self.y_pos].is_active
            self.table[self.x_pos+1][self.y_pos].is_active = False

    def move_down(self):
        if self.y_pos == 19:
            pass
        else:
            self.y_pos += 1
            self.table[self.x_pos][self.y_pos].is_active = True
            self.table[self.x_pos][self.y_pos-1].is_active = False

def update():
    for row in grid.table:
        for square in row:
            if square.is_active:
                pygame.draw.rect(screen, (0, 0, 0), square.rect)
    pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((400, 600))

    grid = Grid(10, 20)

    pygame.time.set_timer(pygame.USEREVENT+1, 1000)
    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT]:
                    grid.move_right()
                elif keys[pygame.K_LEFT]:
                    grid.move_left()
            if event.type == pygame.USEREVENT+1:
                grid.move_down() 
            if event.type == pygame.QUIT:
                running = False
                break
        update()
    
            
