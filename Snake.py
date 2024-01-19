import pygame

class Snake:
    def __init__(self, 
                 screen,
                 position_x: int = 0,
                 position_y: int = 0, 
                 direction: int = 2,
                 speed: int = 32, 
                 min_x: int = 0,
                 max_x: int = 0,
                 min_y: int = 0,
                 max_y: int = 0,
                 ):
        
        self.screen = screen
        self.position_x = position_x
        self.position_y = position_y
        self.tile_position: list[int, int] = [0, 0]
        self.direction = direction
        
        self.dimension_x = 32
        self.dimension_y = 32
        self.color: tuple[int, int, int] = (255, 255, 255)
        
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y 
        self.max_y = max_y
        
        self.speed = speed
        # self.snake_head = pygame.Rect(self.position_x, self.position_y, (self.dimension))
        self.snake_head = pygame.Rect(position_x, position_y, self.dimension_x, self.dimension_y)
    
    # set direction 
    def set_direction(self, direction: int) -> None:
        self.direction = direction
        
    def move_head(self) -> None:
        if (self.check_wall_collision(self.min_x, self.max_x, self.min_y, self.max_y)):
            print("COLLISON")
        else:
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
    
    def check_wall_collision(self, min_x: int, max_x: int, min_y: int, max_y: int) -> bool:
        if (self.snake_head.x < min_x or 
            self.snake_head.x > max_x or 
            self.snake_head.y < min_y or
            self.snake_head.y > max_y):
            return True
        else:
            return False
    
    # def eat_fruit(self, fruit_x, fruit_y):
    #     if (self.position_x == fruit_x and self.position_y == fruit_y):
    #         pass
    
    def grow(self):
        pass