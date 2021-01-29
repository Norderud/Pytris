import pygame
from grid import Grid


def update():
    grid.draw_active_piece()
    for x, row in enumerate(grid.table):
        for y, square in enumerate(row):
            if square.is_active:
                pygame.draw.rect(screen, (0, 0, 0), (y*30, x*30, 30, 30))
    pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((300, 600))

    grid = Grid(10, 20)
    timer_ms = 100
    pygame.time.set_timer(pygame.USEREVENT+1, timer_ms)
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
