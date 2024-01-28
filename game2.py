import os
import pygame

# Load our scenes
# from states.title import Title
from game_world import Game_world
from scoreboard import Scoreboard


class Game:
    """Initializes game_world and contains the gameloops.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """
    def __init__(self):
        pygame.init()

        # screen dimension
        self.SCREEN_WIDTH: int = 584  # 584 for right width
        self.SCREEN_HEIGHT: int = 550

        # set up screen surface
        self.screen: pygame.surface = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        )

        # create background
        self.scoreboard = Scoreboard(self)

        # create game world
        self.game_world = Game_world(self)

        # event states
        self.directions_tile_coordinates: dict = {
            "north": [0, -1],
            "east": [1, 0],
            "south": [0, 1],
            "west": [-1, 0],
        }
        self.direction: list[int] = self.directions_tile_coordinates["east"]
        self.actions: dict = {
            "start": False,
            "pause": True,
            "unpause": False,
            "restart": False,
        }
        self.running, self.playing = True, False
        # create periodic event for snake movement
        self.snake_move_timer: int = 100
        self.move_snake_event: pygame.USEREVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.move_snake_event, self.snake_move_timer)

        # load font
        self.load_font()

        # scores
        self.score = 0
        self.highscore = self.scoreboard.get_highscore()

        # colors
        self.color: dict = {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "RED": (255, 0, 0),
        }

    def game_start(self) -> None:
        self.scoreboard.draw(self.score)
        self.game_world.draw()
        self.game_world.snake.draw()
        self.game_world.fruit.draw()
        while self.running and not self.actions["start"]:
            self.get_events()
            self.draw_test(
                "RETRO SNAKE",
                self.font_50,
                self.color["WHITE"],
                self.color["BLACK"],
                center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 4),
            )
            self.draw_test(
                "by Ron Bellemann",
                self.font_24,
                self.color["WHITE"],
                self.color["BLACK"],
                center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 3.05),
            )
            self.draw_test(
                "to start or pause the game",
                self.font_24,
                self.color["BLACK"],
                self.color["WHITE"],
                center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 1.2835),
            )
            self.draw_test(
                "Press <SPACE>",
                self.font_24,
                self.color["BLACK"],
                self.color["WHITE"],
                center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 1.2),
            )
            pygame.display.flip()
        if self.running:
            self.playing = True

    def game_loop(self) -> None:
        while self.playing:
            # print(self.actions['pause'])
            # get events
            self.get_events()
            # update
            self.game_world.snake.update(self.direction)
            # interactions
            self.eat_fruit(self.game_world.snake, self.game_world.fruit)
            # draw
            self.scoreboard.draw(self.score)
            self.game_world.draw()
            self.game_world.snake.draw()
            self.game_world.fruit.draw()
            while self.running and self.actions["pause"] and self.actions["start"]:
                self.get_events()
                self.draw_test(
                    "Press <SPACE> to unpause",
                    self.font_24,
                    self.color["BLACK"],
                    self.color["WHITE"],
                    center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 1.1),
                )
                pygame.display.flip()
            pygame.display.flip()

    def game_over(self) -> None:
        self.actions["restart"] = False
        self.scoreboard.save_highscore()
        while self.running and not self.actions["restart"]:
            self.get_events()
            self.draw_game_over()
            # self.draw_text(self.screen, "GAME OVER", (255, 255, 255), self.SCREEN_WIDTH/2 - 100, self.SCREEN_HEIGHT/2)
            # self.draw_text(self.screen, f"Score: {self.score}", (255, 255, 255), self.SCREEN_WIDTH/2 - 100, self.SCREEN_HEIGHT/2 + 30)
            pygame.display.flip()
        self.actions["restart"] = False
        self.new_game()
        self.playing = True

    def new_game(self):
        # reset game
        self.score = 0
        self.direction = self.directions_tile_coordinates["east"]
        # reset snake
        # self.game_world.snake.__init__(self, self.game_world)
        self.game_world = Game_world(self)
        # reset fruit
        # self.game_world.fruit.__init__(self, self.game_world)

    def get_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            # handle snakemovement
            if event.type == self.move_snake_event:
                self.game_world.snake.can_move = True

            # if event.type == pygame.KEYDOWN:
            #     if event.

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction = self.directions_tile_coordinates["north"]
        if keys[pygame.K_s]:
            self.direction = self.directions_tile_coordinates["south"]
        if keys[pygame.K_d]:
            self.direction = self.directions_tile_coordinates["east"]
        if keys[pygame.K_a]:
            self.direction = self.directions_tile_coordinates["west"]
        # contains logic for the pause
        if keys[pygame.K_SPACE]:
            self.actions["start"] = True
            if self.playing and self.actions["start"]:
                if self.actions["unpause"] and not self.actions["pause"]:
                    self.actions["pause"] = True
                if not self.actions["unpause"] and self.actions["pause"]:
                    self.actions["pause"] = False
        else:
            if self.playing and self.actions["start"]:
                if self.actions["pause"]:
                    self.actions["unpause"] = False
                else:
                    self.actions["unpause"] = True
        if keys[pygame.K_r]:
            self.actions["restart"] = True

    def eat_fruit(self, snake, fruit):
        if snake.body[0] == fruit.tile_position:
            snake.grow()
            fruit.update()
            self.score += 1
            if self.score > self.highscore:
                self.highscore = self.score
            print("FRUIT COLLISION")

    def draw_game_start(self):
        pass

    def draw_game_over(self):
        text_rows = [
            "GAME OVER",
            f"User Score: {self.score}",
            f"Highscore: {self.highscore}",
            "Press <r> to",
            "restart the game",
        ]
        text_offsets_y = [0, 100, 28, 50, 28]

        for index, text in enumerate(text_rows):
            if index == 0:
                text_surface = self.font_38.render(
                    text, True, self.color["WHITE"], self.color["BLACK"]
                )
            else:
                text_surface = self.font_24.render(
                    text, True, self.color["WHITE"], self.color["BLACK"]
                )

            text_rect = text_surface.get_rect(
                center=(
                    self.SCREEN_WIDTH / 2,
                    self.SCREEN_HEIGHT / 2 + sum(text_offsets_y[: index + 1]),
                )
            )
            # pygame.draw.rect(self.screen, (0, 0, 0), text_rect)
            self.screen.blit(text_surface, text_rect)

    def draw_test(
        self,
        text: str,
        font: pygame.font.Font,
        color: tuple[int],
        background_color: tuple[int] = None,
        **kwargs,
    ) -> None:
        text_surface = font.render(text, True, color, background_color)
        text_rect = text_surface.get_rect(**kwargs)
        self.screen.blit(text_surface, text_rect)

    # https://github.com/ChristianD37/YoutubeTutorials/blob/master/Game%20States/game.py
    def draw_text(self, text: str, color: tuple[int], x: int, y: int) -> None:
        text_surface = self.font_24.render(text, True, color, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.screen.blit(text_surface, text_rect)

    def load_font(self):
        # Create pointers to directories
        self.font_dir = "fonts"
        self.font_24 = pygame.font.Font(
            os.path.join(self.font_dir, "joystix_monospace.otf"), 24
        )
        self.font_38 = pygame.font.Font(
            os.path.join(self.font_dir, "joystix_monospace.otf"), 38
        )
        self.font_50 = pygame.font.Font(
            os.path.join(self.font_dir, "joystix_monospace.otf"), 50
        )


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_start()
        g.game_loop()
        g.game_over()
    pygame.quit()
