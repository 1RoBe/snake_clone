import pygame
from Tail import Tail

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
        self.old_tile_position: list[int, int] = []
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
        # self.segment_list: list[Snake] = [self]
        
        # tail
        self.segment_list: list[Tail] = []
    
    # set direction 
    def set_direction(self, direction: int) -> None:
        # check if new direction is not opposite of old direction
        if abs(direction - self.direction) != 2:
            self.direction = direction
        
    def move_head(self) -> None:
        if (self.check_wall_collision()):
            print("COLLISON")
        else:
            # change tile_position depending on direction
            # There seems to be a bug when I try to assign self.old_tile_position = self.tile_position
            # and then change the self.tile_position => both old and new show same coords
            # BUG FOUND remembered that lists are copied by reference in python
            self.old_tile_position = self.tile_position[:]
            
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
            # print(self.old_tile_position, self.tile_position)
            

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
        # check if tail exists and use snake old tile position or the tail position of last segment
        if len(self.segment_list) != 0:
            old_tile_position = self.segment_list[-1].old_tile_position[:]
            # print(old_tile_position, self.tile_position, self.old_tile_position)
        else:
            old_tile_position = self.old_tile_position[:]
            # print("else", old_tile_position, self.tile_position, self.old_tile_position)
        
        # print(old_tile_position, self.tile_position)
        segment: Tail = Tail(self.screen, self.field_min_x, self.field_min_y, old_tile_position, self.tile_size)
        self.segment_list.append(segment)
        for element in self.segment_list:
            print(element.tile_position)
            
        
    def move(self):
        if (self.check_wall_collision()):
            print("COLLISON")
        if len(self.segment_list) != 0:
            self.segment_list[0].old_tile_position = self.segment_list[0].tile_position[:]
            self.segment_list[0].tile_position = self.old_tile_position[:]
            for index in reversed(range(len(self.segment_list))):
                if index < 0:
                    break
                else:
                    self.segment_list[index].old_tile_position = self.segment_list[index].tile_position[:]
                    self.segment_list[index].tile_position = self.segment_list[index - 1].old_tile_position[:]
            

    # def grow(self):
    #     segment = Snake(self.screen)
    #     segment.tile_position = self.segment_list[-1].old_tile_position
    #     self.segment_list.append(segment)
    #     for element in self.segment_list:
    #         print(segment.tile_position, segment.old_tile_position)
            
    #     print(len(self.segment_list))