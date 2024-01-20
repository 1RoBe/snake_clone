import pygame

class Tail:
    def __init__(self, screen: pygame.surface, field_min_x: int = 0, field_min_y: int = 0, tile_position: int = [0, 0], tile_size: int = 0):
        
        # assign screen for drawing Rect
        self.screen: pygame.surface = screen
        
        # tile values
        self.tile_size: int = tile_size
        
        # game field values
        self.field_min_x: int = field_min_x
        self.field_min_y: int = field_min_y
        
        # positions
        self.tile_position: list[int, int] = tile_position
        self.old_tile_position: list[int, int] = []
        self.position_x: int = self.tile_position[0] * self.tile_size + self.field_min_x
        self.position_y: int = self.tile_position[1] * self.tile_size + self.field_min_y
        
        # desing of snake
        self.dimension_x: int = 32
        self.dimension_y: int = 32
        self.color: tuple[int, int, int] = (100, 100, 100)
        self.snake_tail = pygame.Rect(self.position_x, self.position_y, self.dimension_x, self.dimension_y)
    
    
    def draw_head(self) -> None:
        pygame.draw.rect(self.screen, self.color, self.snake_tail)