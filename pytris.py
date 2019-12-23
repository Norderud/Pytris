import pygame
import pygame.locals

class Square:
    def __init__(self, rect):
        self.is_active = False
        self.rect = rect


class Grid:
    def load_grid(self, width, height):
        table = []
        for tile_x in range(0, width):
            line = []
            table.append(line)
            for tile_y in range(0, height):
                rect = (tile_x*30, tile_y*30, 30, 30)
                line.append(Square(rect))
        return table

    def __init__(self,width, height):
        self.table = self.load_grid(width, height)




if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((400, 600))

    grid = Grid(10, 20)

    x_pos = 0
    y_pos = 0
    
    while pygame.event.wait().type != pygame.locals.QUIT:
        screen.fill((255, 255, 255))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            x_pos +=1
            grid.table[x_pos][y_pos].is_active = not grid.table[x_pos][y_pos].is_active
            grid.table[x_pos-1][y_pos].is_active = False
        elif keys[pygame.K_LEFT]:
            x_pos -=1
            grid.table[x_pos][y_pos].is_active = not grid.table[x_pos][y_pos].is_active
            grid.table[x_pos+1][y_pos].is_active = False

        pygame.time.delay(500)
        y_pos += 1
        for x, row in enumerate(grid.table):
            for y, square in enumerate(row):
                if square.is_active:
                    pygame.draw.rect(screen, (0, 0, 0), square.rect)
        pygame.display.update()
