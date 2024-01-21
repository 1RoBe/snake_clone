import pygame
from pygame.locals import *
import time
from Snake import Snake
from Tail import Tail
from Fruit import Fruit

def main():
    
    # 17 to 15 tiles

    TILE_SIZE = 32
    
    TILE_MIN_X = 0
    TILE_MAX_X = 16
    TILE_MIN_Y = 0
    TILE_MAX_Y = 14
    TILE_DIMENSION: list[list[int], list[int]] = [[TILE_MIN_X, TILE_MAX_X], [TILE_MIN_Y, TILE_MAX_Y]]
    
    FIELD_MIN_X = 0
    FIELD_MAX_X = TILE_MAX_X * TILE_SIZE + FIELD_MIN_X
    FIELD_MIN_Y = 0
    FIELD_MAX_Y = TILE_MAX_Y * TILE_SIZE + FIELD_MIN_Y
    FIELD_DIMENSION: list[list[int], list[int]] = [[FIELD_MIN_X, FIELD_MAX_X], [FIELD_MIN_Y, FIELD_MAX_Y]]
    
    SNAKE_STARTING_POSITION = [int(TILE_MAX_X/2), int(TILE_MAX_Y/2)]
    
    SCREEN_WIDTH = FIELD_MIN_X + (TILE_MAX_X + 1) * TILE_SIZE + FIELD_MIN_Y
    SCREEN_HEIGHT = (TILE_MAX_Y + 1) * TILE_SIZE


    # initialize all imported pygame modules
    pygame.init()
    screen: pygame.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    game_over = False

    # define snake

    snake_move_timer: int = 150
    move_snake_event: pygame.USEREVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(move_snake_event, snake_move_timer)


    snake = Snake(screen = screen,
                  field_dimension = FIELD_DIMENSION,
                  tile_dimension = TILE_DIMENSION,
                  tile_size = TILE_SIZE,
                  tile_position = SNAKE_STARTING_POSITION,
                  direction = 2)

    fruit = Fruit(screen = screen, 
                tile_size = TILE_SIZE,
                min_x = 0, 
                max_x = SCREEN_WIDTH, 
                min_y = 0, 
                max_y = SCREEN_HEIGHT)

    # print(fruit.position_x)
    
    while running:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == move_snake_event:
                
                
                snake.update_tile_head()
                # snake.update_drawing_body()
                # snake.draw()
                # for segment in snake.body:a
                    # print(segment.tile_position)
                # snake.move()
                # for element in snake.segment_list:
                #     print(element)

        screen.fill("red")
        # for segments in snake.segment_list:
        #     segments.draw_head()
        # snake.draw_head()
        # snake.update_tile_position_body()
        snake.draw()
        fruit.draw() 
        eat_fruit(snake, fruit)
        
        # should probably be look_north, look_east... due to encapsulation instead of using setters
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
    if (snake.body[0] == fruit.tile_position):
        snake.grow()
        fruit.new_position()
        print("FRUIT COLLISION")


        
if __name__ == "__main__":
    main()



# for event in range(0, 10):
#     print(clock)
#     time.sleep(1)

# OLD SNAKE class

#  snake = Snake(screen = screen,
#                 field_min_x = FIELD_MIN_X,
#                 field_max_x = FIELD_MAX_X,
#                 field_min_y = FIELD_MIN_Y,
#                 field_max_y = FIELD_MAX_Y,
                 
#                 tile_position = [0, 0],
#                 tile_min_x = 0,
#                 tile_max_x = TILE_MAX_X,
#                 tile_min_y = 0,
#                 tile_max_y = TILE_MAX_Y,
#                 tile_size = TILE_SIZE,
                 
#                 direction = 2,
#                 )