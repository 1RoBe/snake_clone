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
    
    FIELD_MIN_X = 20
    FIELD_MAX_X = TILE_MAX_X * TILE_SIZE + FIELD_MIN_X
    FIELD_MIN_Y = 100
    FIELD_MAX_Y = TILE_MAX_Y * TILE_SIZE + FIELD_MIN_Y
    FIELD_DIMENSION: list[list[int], list[int]] = [[FIELD_MIN_X, FIELD_MAX_X], [FIELD_MIN_Y, FIELD_MAX_Y]]
    

    SCREEN_WIDTH = FIELD_MIN_X + (TILE_MAX_X + 1) * TILE_SIZE + FIELD_MIN_X
    SCREEN_HEIGHT = (TILE_MAX_Y + 1) * TILE_SIZE + FIELD_MIN_Y + 20


    # initialize all imported pygame modules
    pygame.init()
    screen: pygame.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running: bool = True
    game_over = False
    paused: bool = False

    # define snake

    snake_move_timer: int = 150
    move_snake_event: pygame.USEREVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(move_snake_event, snake_move_timer)


    snake = Snake(screen = screen,
                  field_dimension = FIELD_DIMENSION,
                  tile_dimension = TILE_DIMENSION,
                  tile_size = TILE_SIZE,
                  tile_position = [0, 0],
                  direction = 2)

    fruit = Fruit(screen = screen, 
                tile_size = TILE_SIZE,
                field_dimension = FIELD_DIMENSION)

    # print(fruit.position_x)
    
    while running:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == move_snake_event:
                

                snake.update_tile_position_body()
                # snake.draw()
                # snake.update_drawing_body()
                # snake.draw()
                # for segment in snake.body:a
                    # print(segment.tile_position)
                # snake.move()
                # for element in snake.segment_list:
                #     print(element)

        screen.fill("red")
        draw_field_border(screen)
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
        
def draw_field_border(screen):
    
    color = (0, 0, 0)
    
    TILE_SIZE = 32
    
    TILE_MIN_X = 0
    TILE_MAX_X = 16
    TILE_MIN_Y = 0
    TILE_MAX_Y = 14
    TILE_DIMENSION: list[list[int], list[int]] = [[TILE_MIN_X, TILE_MAX_X], [TILE_MIN_Y, TILE_MAX_Y]]
    
    FIELD_MIN_X = 20
    FIELD_MAX_X = TILE_MAX_X * TILE_SIZE + FIELD_MIN_X
    FIELD_MIN_Y = 105
    FIELD_MAX_Y = TILE_MAX_Y * TILE_SIZE + FIELD_MIN_Y
    FIELD_DIMENSION: list[list[int], list[int]] = [[FIELD_MIN_X, FIELD_MAX_X], [FIELD_MIN_Y, FIELD_MAX_Y]]
    

    SCREEN_WIDTH = FIELD_MIN_X + (TILE_MAX_X + 1) * TILE_SIZE + FIELD_MIN_Y
    SCREEN_HEIGHT = (TILE_MAX_Y + 1) * TILE_SIZE + FIELD_MIN_X
    
    color = (0, 0, 0)
    
    margin_top = 100
    margin_left = 20
    margin_bottom = 0
    margin_right = 20
    border_width = 5
    
    # new position(margin_left - border_width, margin_top - border_width)
    # new dimension(field_width + 2 * border_width, )
    
    # use field_width and field_height
    
    position_top = (margin_left - border_width, margin_top - border_width)
    dimenstion_top = (32*17 + 2*border_width, border_width)
    
    position_right = (margin_left + 32*17 , margin_top - border_width)
    dimenstion_right = (border_width, 32*15 + 2*border_width)
    
    position_bottom = (margin_left - border_width, margin_top + 32*15)
    dimenstion_bottom = (32*17 + 2*border_width, border_width)
    
    position_left = (margin_left - border_width, margin_top - border_width)
    dimenstion_left = (border_width, 32*15 + 2*border_width)
    
    
    rect_list = [pygame.Rect(position_top, dimenstion_top), 
                 pygame.Rect(position_left, dimenstion_left),
                 pygame.Rect(position_bottom, dimenstion_bottom),
                 pygame.Rect(position_right, dimenstion_right)]
    # rect_top = pygame.Rect(position_top, dimenstion_top)
    # rect_right = pygame.Rect(left, top, width, height)
    # rect_bottom = pygame.Rect(left, top, width, height)
    # rect_left = pygame.Rect(left, top, width, height)
    for rect in rect_list:
        pygame.draw.rect(screen, color, rect)


        
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