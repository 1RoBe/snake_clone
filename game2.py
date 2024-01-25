import os, time, pygame
# Load our scenes
# from states.title import Title
from game_world import Game_world
from background import Background

class Game():
    def __init__(self):
        pygame.init()
        
        # screen dimension
        self.SCREEN_WIDTH: int = 584 # 584 for right width
        self.SCREEN_HEIGHT: int = 600
        
        # set up screen surface
        self.screen: pygame.surface = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        
        # create background
        self.background = Background(self)
        
        # create game world
        self.game_world = Game_world(self)
        
        # events
        self.directions_tile_coordinates: dict = {"north": [0, - 1], "east": [1, 0], "south": [0, 1], "west": [- 1, 0]}
        self.direction: list[int] = self.directions_tile_coordinates["east"]
        self.running, self.playing = True, True
        
        # create periodic event for snake movement
        self.snake_move_timer: int = 150
        self.move_snake_event: pygame.USEREVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.move_snake_event, self.snake_move_timer)
        
        # load font
        self.load_font()
        
        self.score = 0
        
        
        
    def game_loop(self) -> None:
        while self.playing:
            # get events
            self.get_events()
            # update
            self.game_world.snake.update(self.direction)
            # interactions
            self.eat_fruit(self.game_world.snake, self.game_world.fruit)
            # draw 
            self.background.draw_background()
            self.game_world.draw_border()
            self.game_world.snake.draw()
            self.game_world.fruit.draw()
            self.draw_text(self.screen, f"Score {self.score}", (255, 255, 255), 70, 20)
            pygame.display.flip()
            
    def get_events(self) -> None:            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                # pygame.quit()
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

    def eat_fruit(self, snake, fruit):
        if (snake.body[0] == fruit.tile_position):
            snake.grow()
            fruit.update()
            self.score += 1
            print("FRUIT COLLISION")

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        #text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)
    
    def load_font(self):
        # Create pointers to directories 
        self.font_dir = "fonts"
        self.font= pygame.font.Font(os.path.join(self.font_dir, "joystix_monospace.otf"), 20)

    # def update():
    #     draw_field_border(screen)
    #     snake.draw()
    #     fruit.draw()
    #     eat_fruit.draw()
    
if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()
    
    

