import pygame
import random

class Fruit:
    # def __init__(self, screen, tile_size: int, min_x: int, max_x: int, min_y: int, max_y: int):
    def __init__(self, game, game_world):
        self.game = game
        self.game_world = game_world
        
        self.seed = random.seed
        self.fruit_eaten: bool = False
        BLACK: tuple[int, int, int] = (0, 0, 0)
        
        self.width: int = 16
        self.height: int = 16
        
        self.update()
        
        self.design = pygame.Rect(self.position_x, self.position_y, self.width, self.height)
        self.color: tuple[int, int, int] = BLACK
    
    def update(self) -> None:
        self.tile_position = [random.randrange(self.game_world.TILE_DIMENSION[0][0], self.game_world.TILE_DIMENSION[0][1]), 
                              random.randrange(self.game_world.TILE_DIMENSION[1][0], self.game_world.TILE_DIMENSION[1][1])]
        
        self.position_x = self.tile_position[0] * self.game_world.TILE_SIZE + (self.game_world.TILE_SIZE - self.width) / 2 + self.game_world.FIELD_DIMENSION[0][0]
        self.position_y = self.tile_position[1] * self.game_world.TILE_SIZE + (self.game_world.TILE_SIZE - self.width) / 2 + self.game_world.FIELD_DIMENSION[1][0]
        
        self.design = pygame.Rect(self.position_x, self.position_y, self.width, self.height)
        
    def draw(self) -> None:
        pygame.draw.rect(self.game.screen, self.color, self.design)
    

        
        
    
    