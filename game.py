import os
import pygame
from pygame import freetype
from game_world import Game_world
from scoreboard import Scoreboard

# The concept of the different game states is inspired by https://github.com/ChristianD37/YoutubeTutorials/blob/master/Game%20States/game.py
# This game uses the joystix monospace font, which is free for personal and comercial use

class Game:
    """Initializes pygame contains the gameloops.

    Initializes pygame, game_world object and scoreboard object. Contains the game_start, game_loop and game_over loops
    to evaluate events and react accordingly. Handles the snake fruit interaction.

    Attributes:
        SCREEN_WIDTH: a constant int that defines screen width
        SCREEN_HEIGHT: a constant int that defines screen height
        screen: pygame surface that id defined by SCREEN_WITH and SCREEN_HEIGHT
        scoreboard: initiates Scoreboard class that to retrieve and save the score
        directions_tile_coordinates: a dict that contains the possible directions in tile coordinates
        direction: a list containing the direction that is assinged via a keyboard input
        running: a bool that indicates if the program is running or not
        playing: a bool that indicates if game is in the game_loop() state
        snake_move_timer: an int specifying the time interval between move_snake_events
        move_snake_event: a pygame.USEREVENT creating a custom userevent to move the snake
        color: a dict that contains the colors used in the game class
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
        self.running = True
        self.playing = False
        # create periodic event for snake movement
        self.snake_move_timer: int = 100
        self.move_snake_event: pygame.USEREVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.move_snake_event, self.snake_move_timer)

        # load font
        self.load_font()

        # colors
        self.color: dict = {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "RED": (255, 0, 0),
        }

    def game_start(self) -> None:
        """method to create the starting menu"""
        self.scoreboard.draw()
        self.game_world.draw()
        self.game_world.snake.draw()
        self.game_world.fruit.draw()
        while self.running and not self.actions["start"]:
            self.get_events()
            self.draw_text(
                "RETRO SNAKE",
                self.font_50,
                self.color["WHITE"],
                self.color["BLACK"],
                center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 4),
            )
            self.draw_text(
                "by Ron Bellemann",
                self.font_24,
                self.color["WHITE"],
                self.color["BLACK"],
                center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 3.05),
            )
            self.draw_text(
                "to start or pause the game",
                self.font_24,
                self.color["WHITE"],
                self.color["BLACK"],
                center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 1.2835),
            )
            self.draw_text(
                "Press <SPACE>",
                self.font_24,
                self.color["WHITE"],
                self.color["BLACK"],
                center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 1.2),
            )
            pygame.display.flip()
        if self.running:
            self.playing = True

    def game_loop(self) -> None:
        """method for creating the main gameloop and the pause menu"""
        while self.playing:
            # get events
            self.get_events()
            # update snake position with self.direction
            self.game_world.snake.update(self.direction)
            # interactions
            self.eat_fruit(self.game_world.snake, self.game_world.fruit)
            # draw
            self.scoreboard.draw()
            self.game_world.draw()
            self.game_world.snake.draw()
            self.game_world.fruit.draw()
            while self.running and self.actions["pause"] and self.actions["start"]:
                self.get_events()
                self.draw_text(
                    "Press <SPACE> to unpause",
                    self.font_24,
                    self.color["BLACK"],
                    self.color["WHITE"],
                    center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 1.1),
                )
                pygame.display.flip()
            pygame.display.flip()

    def game_over(self) -> None:
        """method to create and display the gameover menu with the score and highscore"""
        print("Before loop: ", "restart ", self.actions['restart'], "running ", self.running)
        self.actions["restart"] = False
        self.scoreboard.save_highscore()
        while self.running and not self.actions["restart"]:
            self.get_events()
            self.draw_game_over()
            pygame.display.flip()
        print("after loop: ", "restart ", self.actions['restart'], "running ", self.running)
        self.actions["restart"] = False
        self.new_game()
        self.playing = True
        

    def new_game(self):
        """method to reset the game"""
        self.direction = self.directions_tile_coordinates["east"]
        self.scoreboard.reset_score()
        self.game_world.snake.reset()
        self.game_world.fruit.update()
        

    def get_events(self) -> None:
        """method for getting pygame events e.g. keyboard inputs and the custom snake_move event"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == self.move_snake_event:
                self.game_world.snake.can_move = True

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
        """method for updating snake, food and scoreboard object in case the snake collides with the fruit"""
        if snake.body[0] == fruit.tile_position:
            snake.grow()
            fruit.update()
            self.scoreboard.score += 1
            if self.scoreboard.score > self.scoreboard.highscore:
                self.scoreboard.highscore = self.scoreboard.score

    def draw_game_over(self):
        """method for drawing game_over menu"""
        self.draw_text(
            "GAME OVER",
            self.font_50,
            self.color["WHITE"],
            self.color["BLACK"],
            center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2),
        )
        self.draw_text(
            f"User Score: {self.scoreboard.score}",
            self.font_24,
            self.color["WHITE"],
            self.color["BLACK"],
            center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2 + 70),
        )
        self.draw_text(
            f"Highscore: {self.scoreboard.highscore}",
            self.font_24,
            self.color["WHITE"],
            self.color["BLACK"],
            center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2 + 98),
        )
        self.draw_text(
            "To restart the game",
            self.font_24,
            self.color["WHITE"],
            self.color["BLACK"],
            center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2 + 178),
        )
        self.draw_text(
            "Press <r>",
            self.font_24,
            self.color["WHITE"],
            self.color["BLACK"],
            center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2 + 206),
        )

    # def draw_text(
    #     self,
    #     text: str,
    #     font: pygame.font.Font,
    #     color: tuple[int],
    #     background_color: tuple[int] = None,
    #     **kwargs,
    # ) -> None:
    #     """method for writing text and blitting it on the screen"""
    #     text_surface = font.render(text, True, color, background_color)
    #     text_rect = text_surface.get_rect(**kwargs)
    #     self.screen.blit(text_surface, text_rect)
    
    def draw_text(
        self,
        text: str,
        font: pygame.font.Font,
        color: tuple[int],
        background_color: tuple[int] = None,
        **kwargs,
    ) -> None:
        """method for writing text and blitting it on the screen"""
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**kwargs)
        # print(text_rect.x, text_rect.width)
        if background_color:
            pygame.draw.rect(self.screen, background_color, (text_rect.x - 3, text_rect.y - 3, text_rect.width + 6, text_rect.height + 6))
        self.screen.blit(text_surface, text_rect)



    def load_font(self):
        """loads fonts at different sizes from directory"""
        # Create pointers to directories
        self.font_dir = "fonts"
        self.font_24 = pygame.font.Font(
            os.path.join(self.font_dir, "arcade-legacy.otf"), 21
        )
        self.font_38 = pygame.font.Font(
            os.path.join(self.font_dir, "arcade-legacy.otf"), 38
        )
        self.font_50 = pygame.font.Font(
            os.path.join(self.font_dir, "arcade-legacy.otf"), 46
        )

if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_start()
        g.game_loop()
        g.game_over()
    pygame.quit()
