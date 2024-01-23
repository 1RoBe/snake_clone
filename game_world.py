import pygame
from snake2 import Snake
# from fruit2 import Fruit
# from game2 import Game

class Game_world:
    def __init__(self, game):
        self.game = game
        self.BACKGROUND_COLOR = (255, 0, 0)
        
        # tile data
        self.TILE_SIZE: int = 32
        self.TILES_X: int = 17
        self.TILES_Y: int = 15
        self.TILE_DIMENSION: list[list[int], list[int]] = [[0, self.TILES_X - 1], 
                                                           [0, self.TILES_X - 1]]
        
        # game field
        self.FIELD_WIDTH: int = self.TILE_SIZE * self.TILES_X
        self.FIELD_HEIGHT: int = self.TILE_SIZE * self.TILES_Y
        
        # center game_world relative to screen
        self.MARGIN_LEFT: int = (self.game.SCREEN_WIDTH - self.FIELD_WIDTH) / 2
        self.MARGIN_RIGHT: int = (self.game.SCREEN_WIDTH - self.FIELD_WIDTH) / 2
        self.MARGIN_TOP: int = 100
        self.MARGIN_BOTTOM: int = 20
        
        # field dimension
        self.FIELD_DIMENSION: list[list[int], list[int]] = [[self.MARGIN_LEFT,
                                                             self.MARGIN_LEFT + self.FIELD_WIDTH],
                                                            [self.MARGIN_TOP,
                                                             self.MARGIN_TOP + self.FIELD_HEIGHT]]
        # border data
        self.BORDER_COLOR = (50, 0, 0)
        self.BORDER_WIDTH = 5
        
        # create snake and fruit objects
        self.snake = Snake(self.game, self)
        
    # draw borders
    def draw_border(self):
        
        # create border coords
        border_position_top = (self.MARGIN_LEFT - self.BORDER_WIDTH, 
                               self.MARGIN_TOP - self.BORDER_WIDTH)
        
        border_dimension_top = (self.FIELD_WIDTH + 2 * self.BORDER_WIDTH,
                                self.BORDER_WIDTH)
        
        border_position_right = (self.MARGIN_LEFT + self.FIELD_WIDTH ,
                                 self.MARGIN_TOP - self.BORDER_WIDTH)
        
        border_dimension_right = (self.BORDER_WIDTH, 
                                  self.FIELD_HEIGHT + 2 * self.BORDER_WIDTH)
        
        border_position_bottom = (self.MARGIN_LEFT - self.BORDER_WIDTH, 
                                  self.MARGIN_TOP + self.FIELD_HEIGHT)
        
        border_dimension_bottom = (self.FIELD_WIDTH + 2 * self.BORDER_WIDTH,
                                   self.BORDER_WIDTH)
        
        border_position_left = (self.MARGIN_LEFT - self.BORDER_WIDTH, 
                                self.MARGIN_TOP - self.BORDER_WIDTH)
        
        border_dimension_left = (self.BORDER_WIDTH,
                                 self.FIELD_HEIGHT + 2 * self.BORDER_WIDTH)
        
        # create list of all border objects
        rect_list = [pygame.Rect(border_position_top, border_dimension_top), 
                    pygame.Rect(border_position_right, border_dimension_right),
                    pygame.Rect(border_position_bottom, border_dimension_bottom),
                    pygame.Rect(border_position_left, border_dimension_left)]

        # draw borders
        for rect in rect_list:
            pygame.draw.rect(self.game.screen, self.BORDER_COLOR, rect)
            
    
        
        