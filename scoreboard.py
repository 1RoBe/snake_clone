import pygame
import shelve


class Scoreboard:
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
        with shelve.open("highscore") as hs_db:
            try:
                return hs_db["highscore"] if hs_db["highscore"] else 0
            except:
                hs_db["highscore"] = 0
                return 0

    def save_highscore(self):
        with shelve.open("highscore") as hs_db:
            hs_db["highscore"] = self.highscore

    def draw(self):
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
            topleft = (self.game.game_world.MARGIN_LEFT - 2, 7)
        )
        self.game.draw_text(
            f"Highscore: {self.highscore}",
            self.game.font_24,
            self.color["WHITE"],
            topleft = (self.game.game_world.MARGIN_LEFT + 250, 7)
        )
    def reset_score(self):
        self.score = 0


                # self.draw_text(
                #     "Press <SPACE> to unpause",
                #     self.font_24,
                #     self.color["BLACK"],
                #     self.color["WHITE"],
                #     center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 1.1),
                # )