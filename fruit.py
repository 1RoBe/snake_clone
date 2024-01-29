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
            seed: creates a random seed 
        """
        self.game = game
        self.game_world = game_world

        random.seed
        self.fruit_eaten: bool = False
        self.color: dict = {"BLACK": (0, 0, 0)}

        self.width: int = 16
        self.height: int = 16

        self.update()

        self.design = pygame.Rect(
            self.position_x, self.position_y, self.width, self.height
        )
        self.color: tuple[int, int, int] = self.color["BLACK"]

    def update(self) -> None:
        """"""
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

        self.position_x = (
            self.tile_position[0] * self.game_world.TILE_SIZE
            + (self.game_world.TILE_SIZE - self.width) / 2
            + self.game_world.FIELD_DIMENSION[0][0]
        )
        self.position_y = (
            self.tile_position[1] * self.game_world.TILE_SIZE
            + (self.game_world.TILE_SIZE - self.width) / 2
            + self.game_world.FIELD_DIMENSION[1][0]
        )

        self.design = pygame.Rect(
            self.position_x, self.position_y, self.width, self.height
        )

    def draw(self) -> None:
        pygame.draw.rect(self.game.screen, self.color, self.design)
