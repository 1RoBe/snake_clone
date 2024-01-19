import pygame
from pygame.locals import *
import time
from Snake import Snake
from Fruit import Fruit

def main():
    
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
    game_over = False

    # define snake

    snake_move_timer = 150
    move_snake_event = pygame.USEREVENT + 1
    pygame.time.set_timer(move_snake_event, snake_move_timer)


    snake = Snake(screen = screen,
                position_x = int(TILE_NUMBER_X / 2) * TILE_WIDTH, 
                position_y = int(TILE_NUMBER_Y / 2) * TILE_WIDTH,
                min_x = 0,
                max_x = TILE_WIDTH * (TILE_NUMBER_X - 1),
                min_y = 0,
                max_y = TILE_WIDTH * (TILE_NUMBER_Y - 1),
                )

    fruit = Fruit(screen = screen, 
                tile_width = TILE_WIDTH,
                min_x = 0, 
                max_x = SCREEN_WIDTH, 
                min_y = 0, 
                max_y = SCREEN_HEIGHT)

    print(fruit.position_x)


    while running:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == move_snake_event:
                snake.move_head()

        screen.fill("red")
        snake.draw_head()
        fruit.draw() 
        eat_fruit(snake, fruit)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            snake.set_direction(1)
        if keys[pygame.K_d]:
            snake.set_direction(2)
        if keys[pygame.K_s]:
            snake.set_direction(3)
        if keys[pygame.K_a]:
            snake.set_direction(4)
            
        # RENDER GAME HERE
        
        # flip() the display to put your work on screen
        pygame.display.flip()
        
        # limit fps to 60
    pygame.quit()

def eat_fruit(snake: Snake, fruit: Fruit):
    if (snake.position_x == fruit.position_x and snake.position_y == fruit.position_y):
        snake.grow()
        fruit.new_position()
        print("FRUIT COLLISION")
        
        
if __name__ == "__main__":
    main()



# for event in range(0, 10):
#     print(clock)
#     time.sleep(1)

