import pygame
import random

class Fruit:
    def __init__(self, screen, tile_size: int, min_x: int, max_x: int, min_y: int, max_y: int):
        self.seed = random.seed
        
        self.tile_size = tile_size
        self.tile_min_x = 0
        self.tile_max_x = 16
        self.tile_min_y = 0
        self.tile_max_y = 14
        
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        
        self.width = 16
        self.height = 16
        
        self.tile_position = [random.randrange(self.tile_min_x, self.tile_max_x), random.randrange(self.tile_min_y, self.tile_max_y)]
        self.position_x = self.tile_position[0] * self.tile_size + (self.tile_size - self.width) / 2
        self.position_y = self.tile_position[1] * self.tile_size + (self.tile_size - self.width) / 2
        
        # self.position_x = int(random.randrange(self.min_x, self.max_x) / self.tile_size) + (self.tile_size - self.width) / 2
        # self.position_y = int(random.randrange(self.min_y, self.max_y) / self.tile_size) + (self.tile_size - self.width) / 2
        # self.position_x = int(random.randrange(self.min_x, self.max_x) / self.tile_size) * self.tile_size + (self.tile_size - self.width) / 2
        # self.position_y = int(random.randrange(self.min_y, self.max_y) / self.tile_size) * self.tile_size + (self.tile_size - self.width) / 2
        

        
        # self.new_position()
        self.design = pygame.Rect(self.position_x, self.position_y, self.width, self.height)
        self.color: tuple[int, int, int] = (0, 0, 0)
        
        self.screen = screen
        
    def draw(self) -> None:
        pygame.draw.rect(self.screen, self.color, self.design)
        
    def new_position(self) -> None:
        self.tile_position = [random.randrange(self.tile_min_x, self.tile_max_x), random.randrange(self.tile_min_y, self.tile_max_y)]
        self.position_x = self.tile_position[0] * self.tile_size + (self.tile_size - self.width) / 2
        self.position_y = self.tile_position[1] * self.tile_size + (self.tile_size - self.width) / 2
        self.design = pygame.Rect(self.position_x, self.position_y, self.width, self.height)
    

        
        
    
    