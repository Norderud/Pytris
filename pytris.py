import pygame
from grid import Grid

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

    pygame.time.set_timer(pygame.USEREVENT+1, 100)
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
    
            
