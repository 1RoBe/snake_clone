import pygame
import shelve

class Scoreboard:
    """Class that saves and loads highscore and draws them.

    Class that loads a previously saved highscore and saves current score in case it is higher
    than the saved highscore by using shelve

    Attributes:
        game: Game object for screen object and screen dimensions
        score: int that indicates the current score of the player
        highscore: int indicates a previously saved highscore
        color: dict that defines the colors used in this class
    """
    def __init__(self, game):
        self.game = game
        self.score: int = 0
        self.highscore: int = self.get_highscore()
        self.color: dict = {
            "BLACK": (0, 0, 0),
            "WHITE": (255, 255, 255),
            "RED": (255, 0, 0),
        }

    def get_highscore(self) -> int:
        """method that loads a previous highscore in case it exists otherwise returns zero

        Returns:
            int: highscore obtained from file if it exists, otherwise returns 0
        """
        with shelve.open("highscore") as hs_db:
            try:
                return hs_db["highscore"] if hs_db["highscore"] else 0
            except:
                hs_db["highscore"] = 0
                return 0

    def save_highscore(self):
        """method that saves highscore to file"""
        with shelve.open("highscore") as hs_db:
            hs_db["highscore"] = self.highscore

    def draw(self):
        """method that draws the scoreboard"""
        self.game.screen.fill(self.color["RED"])
        pygame.draw.rect(
            self.game.screen,
            self.color["BLACK"],
            (
                self.game.game_world.MARGIN_LEFT - self.game.game_world.BORDER_WIDTH,
                5,
                self.game.game_world.FIELD_WIDTH
                + 2 * self.game.game_world.BORDER_WIDTH,
                35,
            ),
        )
        self.game.draw_text(
            f"Score: {self.score}",
            self.game.font_24,
            self.color["WHITE"],
            topleft = (self.game.game_world.MARGIN_LEFT, 10)
        )
        self.game.draw_text(
            f"Highscore: {self.highscore}",
            self.game.font_24,
            self.color["WHITE"],
            topleft = (self.game.game_world.MARGIN_LEFT + 250, 10)
        )
        
    def reset_score(self):
        """method that resets the players score after game_over state"""
        self.score = 0