import pygame
from snake import Snake
from fruit import Fruit

# from fruit2 import Fruit
# from game2 import Game


class Game_world:
    """Defines the parameters for the game world. Initializes snake and fruit object

    Defines the size and position of the game_world and its borders and of the tiles.
    Initialises the snake and fruit object.

    Attributes:
        game: game object that defines parameters specific to the screen
        color: a dict that contains the colors used in the game class
        TILE_SIZE: constant int defining the tilesize
        TILES_X: constant int defining number of tiles in x-direction
        TILES_Y: constant int defining number of tiles in y-direction
        TILE_DIMENSION: constant list of ints defining the game world dimension in tile coords
        FIELD_WIDTH: constant int defining width of game world in pixels
        FIELD_HEIGHT: constant int defining height of game world in pixels
        MARGIN_LEFT: constant int defining the leftside margin between game world and SCREEN_WIDTH
        MARGIN_RIGHT: constant int defining the rightside margin between game world and SCREEN_WIDTH
        MARGIN_TOP: constant int defining the topside margin between game world and SCREEN_HEIGHT
        MARGIN_BOTTOM: constant int defining the bottomside margin between game world and SCREEN_HEIGHT
        FIELD_DIMENSION: constant list of ints defining the game world dimension in pixels
        BORDER_COLOR: constant int defining the color of the border rectangles
        BORDER_WIDTH: constant int defining the width of the border rectangles
        snake: Snake object
        fruit: Fruit object
    """

    def __init__(self, game):
        self.game = game
        self.color: dict = {"RED": (255, 0, 0), "BLACK": (0, 0, 0)}

        # tile data
        self.TILE_SIZE: int = 32
        self.TILES_X: int = 17
        self.TILES_Y: int = 15
        self.TILE_DIMENSION: list[list[int], list[int]] = [
            [0, self.TILES_X - 1],
            [0, self.TILES_Y - 1],
        ]

        # game field
        self.FIELD_WIDTH: int = self.TILE_SIZE * self.TILES_X
        self.FIELD_HEIGHT: int = self.TILE_SIZE * self.TILES_Y

        # center game_world relative to screen
        self.MARGIN_LEFT: int = (self.game.SCREEN_WIDTH - self.FIELD_WIDTH) / 2
        self.MARGIN_RIGHT: int = (self.game.SCREEN_WIDTH - self.FIELD_WIDTH) / 2
        self.MARGIN_TOP: int = 50
        self.MARGIN_BOTTOM: int = 20

        # field dimension
        self.FIELD_DIMENSION: list[list[int], list[int]] = [
            [self.MARGIN_LEFT, self.MARGIN_LEFT + self.FIELD_WIDTH],
            [self.MARGIN_TOP, self.MARGIN_TOP + self.FIELD_HEIGHT],
        ]
        # border data
        self.BORDER_COLOR = self.color["BLACK"]
        self.BORDER_WIDTH = 5

        # create snake and fruit objects
        self.snake = Snake(self.game, self)
        self.fruit = Fruit(self.game, self)

    # draw borders
    def draw(self):
        """method to draw the borders"""
        # create border coords
        border_position_top = (
            self.MARGIN_LEFT - self.BORDER_WIDTH,
            self.MARGIN_TOP - self.BORDER_WIDTH,
        )

        border_dimension_top = (
            self.FIELD_WIDTH + 2 * self.BORDER_WIDTH,
            self.BORDER_WIDTH,
        )

        border_position_right = (
            self.MARGIN_LEFT + self.FIELD_WIDTH,
            self.MARGIN_TOP - self.BORDER_WIDTH,
        )

        border_dimension_right = (
            self.BORDER_WIDTH,
            self.FIELD_HEIGHT + 2 * self.BORDER_WIDTH,
        )

        border_position_bottom = (
            self.MARGIN_LEFT - self.BORDER_WIDTH,
            self.MARGIN_TOP + self.FIELD_HEIGHT,
        )

        border_dimension_bottom = (
            self.FIELD_WIDTH + 2 * self.BORDER_WIDTH,
            self.BORDER_WIDTH,
        )

        border_position_left = (
            self.MARGIN_LEFT - self.BORDER_WIDTH,
            self.MARGIN_TOP - self.BORDER_WIDTH,
        )

        border_dimension_left = (
            self.BORDER_WIDTH,
            self.FIELD_HEIGHT + 2 * self.BORDER_WIDTH,
        )

        # create list of all border objects
        rect_list = [
            pygame.Rect(border_position_top, border_dimension_top),
            pygame.Rect(border_position_right, border_dimension_right),
            pygame.Rect(border_position_bottom, border_dimension_bottom),
            pygame.Rect(border_position_left, border_dimension_left),
        ]

        # draw borders
        for rect in rect_list:
            pygame.draw.rect(self.game.screen, self.BORDER_COLOR, rect)
