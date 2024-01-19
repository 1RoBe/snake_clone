import pygame
from pygame.locals import *
import time

# 17 to 15 tiles
TILE_NUMBER_X = 17
TILE_NUMBER_Y = 15
TILE_WIDTH = 32

SCREEN_WIDTH = TILE_NUMBER_X * TILE_WIDTH
SCREEN_HEIGHT = TILE_NUMBER_Y * TILE_WIDTH


# initialize all imported pygame modules
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

snake_pos = pygame.Vector2(int(TILE_NUMBER_X / 2) * TILE_WIDTH, int(TILE_NUMBER_Y / 2) * TILE_WIDTH)
snake_dim = pygame.Vector2(TILE_WIDTH, TILE_WIDTH)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("red")

    pygame.draw.rect(screen, (255, 255, 255), (snake_pos, snake_dim))
    # pygame.draw.circle()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_pos.y -= 10 * dt
    if keys[pygame.K_s]:
        snake_pos.y += 10 * dt
    if keys[pygame.K_a]:
        snake_pos.x -= 10 * dt
    if keys[pygame.K_d]:
        snake_pos.x += 10 * dt
        
    # RENDER GAME HERE
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    
    # limit fps to 60
    dt = clock.tick(60) / 1000

pygame.quit()




# for event in range(0, 10):
#     print(clock)
#     time.sleep(1)

