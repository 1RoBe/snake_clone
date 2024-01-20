import pygame

class Snake:
    def __init__(self, 
                 screen,
                 field_min_x: int = 0,
                 field_max_x: int = 544,
                 field_min_y: int = 0,
                 field_max_y: int = 480,
                 
                 tile_position: list[int, int] = [0, 0],
                 tile_min_x: int = 0,
                 tile_max_x: int = 16,
                 tile_min_y: int = 0,
                 tile_max_y: int = 14,
                 tile_size: int = 32,
                 
                 direction: int = 2):
        
        self.screen = screen
        
        # tile positions
        self.tile_position: list[int, int] = tile_position
        self.tile_size: int = tile_size
        
        # size of game field in px
        self.field_min_x = field_min_x 
        self.field_max_x = field_max_x 
        self.field_min_y = field_min_y
        self.field_max_y = field_max_y
        
        # size of game field in tiles
        self.tile_min_x = tile_min_x
        self.tile_max_x = tile_max_x
        self.tile_min_y = tile_min_y
        self.tile_max_y = tile_max_y
        
        # pixel positions
        self.position_x: int = self.tile_position[0] * self.tile_size + self.field_min_x
        self.position_y: int = self.tile_position[1] * self.tile_size + self.field_min_y
        
        # north = 1, east = 2, south = 3, west = 4
        self.direction: int = direction
        
        # desing of snake
        self.dimension_x = 32
        self.dimension_y = 32
        self.color: tuple[int, int, int] = (255, 255, 255)
        self.snake_head = pygame.Rect(self.position_x, self.position_y, self.dimension_x, self.dimension_y)
        
        # speed
        self.speed = tile_size
    
    # set direction 
    def set_direction(self, direction: int) -> None:
        # check if new direction is not opposite of old direction
        if abs(direction - self.direction) != 2:
            self.direction = direction
        
    def move_head(self) -> None:
        if (self.check_wall_collision()):
            print("COLLISON")
        else:
            # print(self.snake_head.x, self.snake_head.y)
            match self.direction:
                case 1:
                    self.snake_head.move_ip((0, - self.speed))
                    self.tile_position[1] -= 1
                case 2:
                    self.snake_head.move_ip((self.speed, 0))
                    self.tile_position[0] += 1
                case 3:
                    self.snake_head.move_ip((0, self.speed))
                    self.tile_position[1] += 1
                case 4:
                    self.snake_head.move_ip((- self.speed, 0))
                    self.tile_position[0] -= 1

    def draw_head(self) -> None:
        pygame.draw.rect(self.screen, self.color, self.snake_head)
    
    def check_wall_collision(self) -> bool:
        if (self.tile_position[0] < self.tile_min_x or 
            self.tile_position[0] > self.tile_max_x or 
            self.tile_position[1] < self.tile_min_y or
            self.tile_position[1] > self.tile_max_y):
            return True
        else:
            return False
    
    # def eat_fruit(self, fruit_x, fruit_y):
    #     if (self.position_x == fruit_x and self.position_y == fruit_y):
    #         pass
    
    def grow(self):
        pass