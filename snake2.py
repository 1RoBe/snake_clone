import pygame

class Snake:
    def __init__(self, game, game_world):
        # imports from game and game_world classes
        self.game = game
        self.game_world = game_world
        
        # check if snake can move in that frame
        self.can_move = False
        
        # position in tile coords
        self.tile_position_last_segment: list[int] = []
        
        # direction
        self.direction: list = [1, 0]
        self.tile_position_start: int = [4, 7]
        
        # design of drawing
        self.width: int =  self.game_world.TILE_SIZE 
        self.height: int =  self.game_world.TILE_SIZE 
        self.color: tuple[int, int, int] = (255, 255, 255)
        
        # create list of all snake segments and append head
        self.body = [self.tile_position_start]
        
        # start with 2 segments
        for index in range(1, 3):
            self.body.append([self.tile_position_start[0] - index, self.tile_position_start[1]])

    def update(self, direction: list[int]) -> None:
        if self.can_move:
            if [a + b for a, b in zip(self.direction, direction)] != [0, 0]:
                self.direction = direction
            if self.collision_wall() or self.collision_body():
                self.game.playing = False
            else:
                self.update_tile_position()        
            self.can_move = False
    
    def update_tile_position(self) -> None:
        self.tile_position_last_segment = self.body[-1][:]
        
        # save old positions
        old_tile_positions = self.body[:]
        
        # update position of head of snake
        self.body[0] = [pos1 + pos2 for pos1, pos2 in zip(self.body[0], self.direction)]
        
        # update body of snake
        for index in range(len(self.body) - 1):
            self.body[index + 1] = old_tile_positions[index]
                
    def collision_wall(self) -> bool:
        # print(self.game_world.TILE_DIMENSION[1][1])
        self.game.test = True
        if (self.body[0][0] + self.direction[0] < self.game_world.TILE_DIMENSION[0][0] or 
            self.body[0][0] + self.direction[0] > self.game_world.TILE_DIMENSION[0][1] or 
            self.body[0][1] + self.direction[1] < self.game_world.TILE_DIMENSION[1][0] or 
            self.body[0][1] + self.direction[1] > self.game_world.TILE_DIMENSION[1][1]):
            return True
        return False
        
    def collision_body(self) -> bool:
        for tile_position in self.body[1:]:
            if [pos1 + pos2 for pos1, pos2 in zip(self.body[0], self.direction)] == tile_position:
                return True
        return False
    
    def grow(self) -> None:
        self.body.append(self.tile_position_last_segment)
        
    def draw(self) -> None:
        # conversion into pixel coordinates
        position_x = self.body[0][0] *  self.game_world.TILE_SIZE  + self.game_world.FIELD_DIMENSION [0][0]
        position_y = self.body[0][1] *  self.game_world.TILE_SIZE  + self.game_world.FIELD_DIMENSION [1][0]
        design_head = pygame.Rect(position_x, position_y, self.width, self.height)
        pygame.draw.rect(self.game.screen, self.color, design_head)
        
        # draw snake face depending on current direction
        match self.direction:
            case [0, -1]:
                design_eye_1 = pygame.Rect(position_x + 8, position_y + 32 - 18 - 4, 4, 4)
                design_eye_2 = pygame.Rect(position_x + + 32-8-4, position_y + 32 - 18 - 4, 4, 4)
                pygame.draw.rect(self.game.screen, (0, 0, 0), design_eye_1)
                pygame.draw.rect(self.game.screen, (0, 0, 0), design_eye_2)
                
            case [1, 0]:
                design_eye_1 = pygame.Rect(position_x + 18, position_y + 8, 4, 4)
                design_eye_2 = pygame.Rect(position_x + 18, position_y + 32-8-4, 4, 4)
                pygame.draw.rect(self.game.screen, (0, 0, 0), design_eye_1)
                pygame.draw.rect(self.game.screen, (0, 0, 0), design_eye_2)
                
            case [0, 1]:
                design_eye_1 = pygame.Rect(position_x + 8, position_y + 18, 4, 4)
                design_eye_2 = pygame.Rect(position_x + + 32-8-4, position_y + 18, 4, 4)
                pygame.draw.rect(self.game.screen, (0, 0, 0), design_eye_1)
                pygame.draw.rect(self.game.screen, (0, 0, 0), design_eye_2)
            
            case [-1, 0]:
                design_eye_1 = pygame.Rect(position_x + 10, position_y + 8, 4, 4)
                design_eye_2 = pygame.Rect(position_x + 10, position_y + 32-8-4, 4, 4)
                pygame.draw.rect(self.game.screen, (0, 0, 0), design_eye_1)
                pygame.draw.rect(self.game.screen, (0, 0, 0), design_eye_2)
            
        # iterate through each snake segment other than the head and draw them
        for index, tile_position in enumerate(self.body[1:]):
            position_x = tile_position[0] *  self.game_world.TILE_SIZE  + self.game_world.FIELD_DIMENSION [0][0]
            position_y = tile_position[1] *  self.game_world.TILE_SIZE  + self.game_world.FIELD_DIMENSION [1][0]
            design = pygame.Rect(position_x, position_y, self.width, self.height)
            pygame.draw.rect(self.game.screen, [max(255-230*index/len(self.body), 50), 255-230*index/len(self.body), 255-230*index/len(self.body)], design)
                
 

    

