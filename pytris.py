import pygame
from game import Game


def update():
    for x, row in enumerate(game.grid):
        for y, square in enumerate(row):
            pygame.draw.rect(screen, square.color,
                             ((y*30)-1, (x*30)-1, 29, 29))
    pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((300, 600))

    game = Game(10, 30)
    timer_ms = 180
    pygame.time.set_timer(pygame.USEREVENT+1, timer_ms)
    running = True
    paused = False
    while running:
        screen.fill((20, 20, 20))
        for event in pygame.event.get():
            if not paused:
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_RIGHT]:
                        game.move_right()
                    elif keys[pygame.K_LEFT]:
                        game.move_left()
                    elif keys[pygame.K_UP]:
                        game.rotate()
                    elif keys[pygame.K_p]:
                        paused = not paused
                elif event.type == pygame.USEREVENT+1:
                    game.move_down()
            else: 
                 if event.type == pygame.KEYDOWN:
                     if pygame.key.get_pressed()[pygame.K_p]:
                        paused = not paused
            if event.type == pygame.QUIT:
                running = False
                break
        update()
