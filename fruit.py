import random
import pygame


class Fruit:
    def __init__(self, game, game_world):
        """Class that updates and draws the fruit

        Initializes and updates the fruit object to a random position.
        Draws the fruit object to self.game.screen

        Attributes:
            game: Game object for screen object and screen dimensions
            game_world: Game_world object for field dimension and tilesize
            seed: creates a random seed to randomly determine the fruit position
            color: dict containing the colors used in this class
            width: int describing the width of the fruit object
            height: int describing the height of the fruit object
            design: pygame.Rect object describing the look of the fruit object
        """
        self.game = game
        self.game_world = game_world

        random.seed
        
        self.width: int = 16
        self.height: int = 16
        self.color: dict = {"BLACK": (0, 0, 0)}
        self.design: pygame.Rect = None

        self.update()

    def update(self) -> None:
        """method for updating the pixel position of the fruit"""
        self.tile_position = [
            random.randrange(
                self.game_world.TILE_DIMENSION[0][0],
                self.game_world.TILE_DIMENSION[0][1],
            ),
            random.randrange(
                self.game_world.TILE_DIMENSION[1][0],
                self.game_world.TILE_DIMENSION[1][1],
            ),
        ]

        position_x = (
            self.tile_position[0] * self.game_world.TILE_SIZE
            + (self.game_world.TILE_SIZE - self.width) / 2
            + self.game_world.FIELD_DIMENSION[0][0]
        )
        position_y = (
            self.tile_position[1] * self.game_world.TILE_SIZE
            + (self.game_world.TILE_SIZE - self.width) / 2
            + self.game_world.FIELD_DIMENSION[1][0]
        )

        self.design = pygame.Rect(
            position_x, position_y, self.width, self.height
        )

    def draw(self) -> None:
        """method for drawing fruit object"""
        pygame.draw.rect(self.game.screen, self.color["BLACK"], self.design)
