import pygame
import pygame.locals

def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, width):
        line = []
        tile_table.append(line)
        for tile_y in range(0, height):
            rect = (tile_x, tile_y, 50, 50)
            line.append(image.subsurface(rect))
    return tile_table

if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((1280, 980))
    screen.fill((255, 255, 255))
    table = load_tile_table("ground.png", 10, 20)
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            screen.blit(tile, (x*30, y*30))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass