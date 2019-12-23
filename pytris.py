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
    screen = pygame.display.set_mode((1280, 980))

    grid = Grid(10, 20)

    grid.table[5][10].is_active = True
    count = 0
    
    while pygame.event.wait().type != pygame.locals.QUIT:
        screen.fill((255, 255, 255))
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            grid.table[0][count].is_active = not grid.table[1][count].is_active
            count +=1

        for x, row in enumerate(grid.table):
            for y, square in enumerate(row):
                if square.is_active:
                    pygame.draw.rect(screen, (0, 0, 0), square.rect)
        pygame.display.update()
