import pygame
from operator import add

class Snake:
    def __init__(self, 
                 screen: pygame.surface, 
                 field_dimension: list[list[int], list[int]] = [[0, 0], [0, 0]],
                 tile_dimension: list[list[int], list[int]] = [[0, 0], [0, 0]],
                 tile_size: int = 0,
                 tile_position: list[int] = [0, 0],
                 direction: int = 2):
        #screen
        self.screen = screen
        
        # min and max value in x and y of gamefield in px and tile coords
        self.field_dimension: list[list[int], list[int]] = field_dimension   
        self.tile_dimension: list[list[int], list[int]] = tile_dimension
        
        # tile_size
        self.tile_size: int = tile_size
        
        # position in tile coords
        # self.tile_position: list[int] = tile_position
        self.tile_position_last_segment: list[int] = []
        
        # direction
        self.direction: int = direction
        
        # position in px for drawing Rect
        # self.position_x: int = self.tile_position[0] * self.tile_size + self.field_dimension[0][0]
        # self.position_y: int = self.tile_position[1] * self.tile_size + self.field_dimension[1][0]
        
        # design of drawing
        self.width: int = self.tile_size
        self.height: int = self.tile_size
        # self.design = pygame.Rect(self.position_x, self.position_y, self.width, self.height)
        self.color: tuple[int, int, int] = (255, 255, 255)
        
        # create list of all snake segments and append head
        self.body = []
        self.body.append(tile_position)
    
    # def draw(self) -> None:
    #     for segment in self.body:
    #         pygame.draw.rect(self.screen, self.color, segment.design)
    #     # pygame.draw.rect(self.screen, self.color, self.design)
    
    def set_direction(self, direction) -> None:
        # make sure that snake can only turn right, left and straight
        if abs(direction - self.direction) != 2:
            self.direction = direction
            
    def update_tile_head(self) -> None:
        # check if head of snake beyond boundaries
        if self.collision_wall():
            print("wall collision")
        elif self.collision_body():
            print("body collision")
        else:
            # assign old_tile_position before changing tile_position
            self.tile_position_last_segment = self.body[-1][:]
            old_tile_position_body = self.body[0][:]
            
            # tile_position buffer, to check if new movement would result in collision to precent right - left, up - down movements
            new_tile_position_buffer: list[int] = self.body[0][:]
            
            # since only the head reacting to directions I move self.body[0]
            match self.direction:
                # north
                case 1:
                    new_tile_position_buffer[1] -= 1
                    # self.body[0][1] -= 1
                # east
                case 2:
                    new_tile_position_buffer[0] += 1
                    # self.body[0][0] += 1
                # south
                case 3:
                    new_tile_position_buffer[1] += 1
                    # self.body[0][1] += 1
                # west
                case 4:
                    new_tile_position_buffer[0] -= 1
                    # self.body[0][0] -= 1
            if len(self.body) == 1:
                self.body[0] = new_tile_position_buffer
            elif self.body[1] != new_tile_position_buffer:
                self.body[0] = new_tile_position_buffer
                # print(old_tile_position_body, self.body[0])
                body_len = len(self.body)
                new_tile_position_body = []
                for index, _ in enumerate(self.body[:]):
                    if index + 1 < body_len:
                        new_tile_position_body = self.body[index + 1]
                        self.body[index + 1] = old_tile_position_body
                        old_tile_position_body = new_tile_position_body
    
    def draw(self) -> None:
        for tile_positon in self.body:
            position_x = tile_positon[0] * self.tile_size + self.field_dimension[0][0]
            position_y = tile_positon[1] * self.tile_size + self.field_dimension[1][0]
            design = pygame.Rect(position_x, position_y, self.width, self.height)
            pygame.draw.rect(self.screen, self.color, design)
            
    
    def collision_wall(self) -> bool:
        # print(self.body)
        if (self.body[0][0] < self.tile_dimension[0][0] or 
            self.body[0][1] > self.tile_dimension[0][1] or 
            self.body[0][0] < self.tile_dimension[1][0] or 
            self.body[0][1] > self.tile_dimension[1][1]):
            
            return True
        else: 
            return False
        
    # def update_tile_position_body(self):

    def collision_body(self) -> bool:
        for tile_position in self.body[1:]:
            if self.body[0] == tile_position:
                return True
        return False
            
    #     pass
        
    def grow(self):
        self.body.append(self.tile_position_last_segment)
        pass
    
test = []

