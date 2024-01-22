import pygame

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
            
    def update_tile_position_body(self) -> None:
        # check if head of snake beyond boundaries
        if self.collision_wall():
            print("wall collision")
        elif self.collision_body():
            print("body collision")
        else:
            # assign old_tile_position before changing tile_position
            self.tile_position_last_segment = self.body[-1][:]
            old_tile_position_body = self.body[0][:]
            
            # since only the head reacting to directions I move self.body[0]
            match self.direction:
                # north
                case 1:
                    self.body[0][1] -= 1
                # east
                case 2:
                    self.body[0][0] += 1
                # south
                case 3:
                    self.body[0][1] += 1
                # west
                case 4:
                    self.body[0][0] -= 1

            # print(old_tile_position_body, self.body[0])
            body_len = len(self.body)
            new_tile_position_body = []
            for index, _ in enumerate(self.body[:]):
                if index + 1 < body_len:
                    new_tile_position_body = self.body[index + 1]
                    self.body[index + 1] = old_tile_position_body
                    old_tile_position_body = new_tile_position_body
    
    def draw(self) -> None:
        # don't draw snake segments outside game field
        # if (self.body[0][0] >= self.tile_dimension[0][0] or 
        #     self.body[0][0] <= self.tile_dimension[0][1] or
        #     self.body[0][1] >= self.tile_dimension[1][0] or
        #     self.body[0][1] <= self.tile_dimension[1][1]):
        
        # print(self.body[0][0] > self.tile_dimension[0][0] or 
        #     self.body[0][0] < self.tile_dimension[0][1] or
        #     self.body[0][1] > self.tile_dimension[1][0] or
        #     self.body[0][1] < self.tile_dimension[1][1])
        # print("draw",not self.collision_wall())
        #     position_x = self.body[0][0] * self.tile_size + self.field_dimension[0][0]
        #     position_y = self.body[0][1] * self.tile_size + self.field_dimension[1][0]
        #     design = pygame.Rect(position_x, position_y, self.width, self.height)
        #     pygame.draw.rect(self.screen, self.color, design)
        
        # don't draw snake segments outside game field
        if not self.collision_wall():
            position_x = self.body[0][0] * self.tile_size + self.field_dimension[0][0]
            position_y = self.body[0][1] * self.tile_size + self.field_dimension[1][0]
            design = pygame.Rect(position_x, position_y, self.width, self.height)
            pygame.draw.rect(self.screen, self.color, design)
        
        # iterate through each snake segment other than the head and draw them
        for tile_position in self.body[1:]:
            position_x = tile_position[0] * self.tile_size + self.field_dimension[0][0]
            position_y = tile_position[1] * self.tile_size + self.field_dimension[1][0]
            design = pygame.Rect(position_x, position_y, self.width, self.height)
            pygame.draw.rect(self.screen, self.color, design)
                
            # # don't draw snake segments outside game field
            # if (tile_positon[0] < self.tile_dimension[0][0] or 
            #     tile_positon[0] > self.tile_dimension[0][1] or
            #     tile_positon[1] > self.tile_dimension[1][0] or
            #     tile_positon[1] > self.tile_dimension[1][1]):
                
            #     pygame.draw.rect(self.screen, self.color, design)
            
    
    def collision_wall(self) -> bool:
        # print(self.body, self.tile_dimension)
        if (self.body[0][0] < self.tile_dimension[0][0] or 
            self.body[0][0] > self.tile_dimension[0][1] or 
            self.body[0][1] < self.tile_dimension[1][0] or 
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
    

