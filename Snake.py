import pygame

class Snake:
    def __init__(self, 
                 screen: pygame.surface, 
                 field_dimension: list[list[int], list[int]] = [[0, 0], [0, 0]],
                 tile_dimension: list[list[int], list[int]] = [[0, 0], [0, 0]],
                 tile_size: int = 0,
                 tile_position: int = [0, 0],
                 direction: int = 2):
        #screen
        self.screen = screen
        
        # min and max value in x and y of gamefield in px and tile coords
        self.field_dimension: list[list[int], list[int]] = field_dimension   
        self.tile_dimension: list[list[int], list[int]] = tile_dimension
        
        # tile_size
        self.tile_size: int = tile_size
        
        # position in tile coords
        self.tile_position: list[int] = tile_position
        self.tile_position_old: list[int] = []
        
        # direction
        self.direction: int = direction
        
        # position in px for drawing Rect
        self.position_x: int = self.tile_position[0] * self.tile_size + self.field_dimension[0][0]
        self.position_y: int = self.tile_position[1] * self.tile_size + self.field_dimension[1][0]
        
        # design of drawing
        self.width = self.tile_size
        self.height = self.tile_size
        # self.design = pygame.Rect(self.position_x, self.position_y, self.width, self.height)
        self.color: tuple[int, int, int] = (255, 255, 255)
        
        # create list of all snake segments and append head
        self.body: list[Snake] = []
        self.body.append(self)
    
    # def draw(self) -> None:
    #     for segment in self.body:
    #         pygame.draw.rect(self.screen, self.color, segment.design)
    #     # pygame.draw.rect(self.screen, self.color, self.design)
            
    def set_direction(self, direction) -> None:
        self.direction = direction
            
    def update_tile_head(self) -> None:
        # check if head of snake beyond boundaries
        if self.collision_wall():
            print("wall collision")
        else:
            # assign old_tile_position before changing tile_position
            self.tile_position_old = self.tile_position[:]
            match self.direction:
                # north
                case 1:
                    self.tile_position[1] -= 1
                # east
                case 2:
                    self.tile_position[0] += 1
                # south
                case 3:
                    self.tile_position[1] += 1
                # west
                case 4:
                    self.tile_position[0] -= 1
    
    def draw(self) -> None:
        for segment in self.body:
            segment.position_x = segment.tile_position[0] * self.tile_size + self.field_dimension[0][0]
            segment.position_y = segment.tile_position[1] * self.tile_size + self.field_dimension[1][0]
            design = pygame.Rect(segment.position_x, segment.position_y, segment.width, segment.height)
            pygame.draw.rect(self.screen, self.color, design)
            
    
    def collision_wall(self) -> bool:
        if (self.tile_position[0] < self.tile_dimension[0][0] or 
            self.tile_position[0] > self.tile_dimension[0][1] or 
            self.tile_position[1] < self.tile_dimension[1][0] or 
            self.tile_position[1] > self.tile_dimension[1][1]):
            
            return True
        else: 
            return False