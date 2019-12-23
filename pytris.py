import pygame
import pygame.locals


class Square:
    def __init__(self, subsurface):
        self.is_active = False
        self.subsurface = subsurface


def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, width):
        line = []
        tile_table.append(line)
        for tile_y in range(0, height):
            rect = (tile_x, tile_y, 30, 30)
            line.append(Square(image.subsurface(rect)))
    return tile_table


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1280, 980))
    table = load_tile_table("ground.png", 10, 20)

    table[5][10].is_active = True

    pygame.display.flip()
    while pygame.event.wait().type != pygame.locals.QUIT:
        screen.fill((255, 255, 255))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            table[1][1].is_active = not table[1][1].is_active
            
        for x, row in enumerate(table):
            for y, square in enumerate(row):
                if square.is_active:
                    screen.blit(square.subsurface, (x*30, y*30))
        pygame.display.update()
