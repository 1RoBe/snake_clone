import pygame
import random

class Fruit:
    # def __init__(self, screen, tile_size: int, min_x: int, max_x: int, min_y: int, max_y: int):
    def __init__(self, game, game_world):
        self.game = game
        self.game_world = game_world
        self.seed = random.seed
        
        self.fruit_eaten: bool = False
        
        # self.tile_size = tile_size
        # self.tile_min_x = 0
        # self.tile_max_x = 16
        # self.tile_min_y = 0
        # self.tile_max_y = 14
        
        # self.field_dimension: list[list[int], list[int]] = field_dimension
        # self.min_x = min_x
        # self.max_x = max_x
        # self.min_y = min_y
        # self.max_y = max_y
        
        self.width = 16
        self.height = 16
        
        self.tile_position = [random.randrange(self.game_world.TILE_DIMENSION[0][0], self.game_world.TILE_DIMENSION[0][1]), 
                              random.randrange(self.game_world.TILE_DIMENSION[1][0], self.game_world.TILE_DIMENSION[1][1])]
        
        self.position_x = self.tile_position[0] * self.game_world.TILE_SIZE + (self.game_world.TILE_SIZE - self.width) / 2 + self.game_world.FIELD_DIMENSION[0][0]
        self.position_y = self.tile_position[1] * self.game_world.TILE_SIZE + (self.game_world.TILE_SIZE - self.width) / 2 + self.game_world.FIELD_DIMENSION[1][0]
        

        
        # self.new_position()
        self.design = pygame.Rect(self.position_x, self.position_y, self.width, self.height)
        self.color: tuple[int, int, int] = (0, 0, 0)
    
    # def update(self):
    #     if self.fruit_eaten():
    #         self.update_position()
    #         self.fruit_eaten = False
        
    def update(self) -> None:
        self.tile_position = [random.randrange(self.game_world.TILE_DIMENSION[0][0], self.game_world.TILE_DIMENSION[0][1]), 
                              random.randrange(self.game_world.TILE_DIMENSION[1][0], self.game_world.TILE_DIMENSION[1][1])]
        
        self.position_x = self.tile_position[0] * self.game_world.TILE_SIZE + (self.game_world.TILE_SIZE - self.width) / 2 + self.game_world.FIELD_DIMENSION[0][0]
        self.position_y = self.tile_position[1] * self.game_world.TILE_SIZE + (self.game_world.TILE_SIZE - self.width) / 2 + self.game_world.FIELD_DIMENSION[1][0]
        self.design = pygame.Rect(self.position_x, self.position_y, self.width, self.height)
        
    def draw(self) -> None:
        pygame.draw.rect(self.game.screen, self.color, self.design)
    

        
        
    
    