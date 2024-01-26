import os, time, pygame
# Load our scenes
# from states.title import Title
from game_world import Game_world
from scoreboard import Scoreboard

class Game():
    def __init__(self):
        pygame.init()
        
        # screen dimension
        self.SCREEN_WIDTH: int = 584 # 584 for right width
        self.SCREEN_HEIGHT: int = 550
        
        # set up screen surface
        self.screen: pygame.surface = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        
        # create background
        self.scoreboard = Scoreboard(self)
        
        # create game world
        self.game_world = Game_world(self)
        
        # events
        self.directions_tile_coordinates: dict = {"north": [0, - 1], "east": [1, 0], "south": [0, 1], "west": [- 1, 0]}
        self.direction: list[int] = self.directions_tile_coordinates["east"]
        self.actions: dict = {"restart": False}
        self.running, self.playing = True, True
        # create periodic event for snake movement
        self.snake_move_timer: int = 100
        self.move_snake_event: pygame.USEREVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.move_snake_event, self.snake_move_timer)
        
        # load font
        self.load_font()
        
        # scores
        self.score = 0
        self.highscore = self.scoreboard.get_highscore()
        
    def game_loop(self) -> None:
        while self.playing:
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
            pygame.display.flip()
            
    def game_over(self) -> None:
        self.actions['restart'] = False
        self.scoreboard.save_highscore()
        while (self.running and not self.actions['restart']):
            self.get_events()
            self.draw_game_over()
            # self.draw_text(self.screen, "GAME OVER", (255, 255, 255), self.SCREEN_WIDTH/2 - 100, self.SCREEN_HEIGHT/2)
            # self.draw_text(self.screen, f"Score: {self.score}", (255, 255, 255), self.SCREEN_WIDTH/2 - 100, self.SCREEN_HEIGHT/2 + 30)
            pygame.display.flip()
        self.actions['restart'] = False
        self.new_game()
        self.playing = True
    
    def new_game(self):
        # reset game
        self.score = 0
        self.direction = self.directions_tile_coordinates['east']
        # reset snake 
        self.game_world.snake.__init__(self, self.game_world)
        # reset fruit
        self.game_world.fruit.__init__(self, self.game_world)
    
    def get_events(self) -> None:            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                
            # handle snakemovement
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
        if keys[pygame.K_r]:
            self.actions['restart'] = True

    def eat_fruit(self, snake, fruit):
        if (snake.body[0] == fruit.tile_position):
            snake.grow()
            fruit.update()
            self.score += 1
            if self.score > self.highscore:
                self.highscore = self.score
            print("FRUIT COLLISION")
        
    def draw_game_over(self):
        text_rows = ["GAME OVER", f"User Score: {self.score}", f"Highscore: {self.highscore}", "Press <r> to", "restart the game"]
        text_offsets_y = [0, 100, 28, 50, 28] 
        WHITE: tuple[int] = (255, 255, 255)
        BLACK: tuple[int] = (0, 0, 0)
        
        self.font.size 
        for index, text in enumerate(text_rows):
            if index == 0:
                text_surface = self.font_game_over.render(text, True, WHITE, BLACK)
            else:
                text_surface = self.font.render(text, True, WHITE, BLACK)

            text_rect = text_surface.get_rect(center = (self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2 + sum(text_offsets_y[:index + 1])))
            # pygame.draw.rect(self.screen, (0, 0, 0), text_rect)
            self.screen.blit(text_surface, text_rect)
    
    # modified from github.ChristianD37/YoutubeTutorials/game.py
    def draw_text(self, text: str, color: tuple[int], x: int, y: int) -> None:
        text_surface = self.font.render(text, True, color,)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.screen.blit(text_surface, text_rect)
        
    def load_font(self):
        # Create pointers to directories 
        self.font_dir = "fonts"
        self.font = pygame.font.Font(os.path.join(self.font_dir, "joystix_monospace.otf"), 24)
        self.font_game_over = pygame.font.Font(os.path.join(self.font_dir, "joystix_monospace.otf"), 38)
    
if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()
        g.game_over()
    pygame.quit()
    

