import os, time, pygame
# Load our scenes
# from states.title import Title
from game_world import Game_world
from background import Background

class Game():
    def __init__(self):
        pygame.init()
        
        # # tiles
        # self.TILE_SIZE: int = 32
        # self.TILES_X: int = 17
        # self.TILES_Y: int = 15
        # # maybe name it Field coords
        # self.TILE_DIMENSION: list[list[int], 
        #                             list[int]] = [[0, self.TILES_X - 1], 
        #                                         [0, self.TILES_X - 1]]
        # # window
        # self.MARGIN_LEFT: int = 20
        # self.MARGIN_RIGHT: int = 20
        # self.MARGIN_TOP: int = 100
        # self.MARGIN_BOTTOM: int = 20
        
        # # game field
        # self.FIELD_WIDTH: int = self.TILE_SIZE * self.TILES_X
        # self.FIELD_HEIGHT: int = self.TILE_SIZE * self.TILES_Y
        # self.FIELD_DIMENSION: list[list[int], 
        #                             list[int]] = [[self.MARGIN_LEFT,
        #                                             self.MARGIN_LEFT + self.FIELD_WIDTH],
        #                                             [self.MARGIN_TOP,
        #                                             self.MARGIN_TOP + self.FIELD_HEIGHT]]
        
        # screen dimension
        self.SCREEN_WIDTH: int = 584
        self.SCREEN_HEIGHT: int = 600
        
        # set up canvas and screen
        # self.game_canvas = pygame.Surface((self.SCREEN_HEIGHT, self.SCREEN_HEIGHT))
        self.screen: pygame.surface = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        
        # create timer for choppy snake movemnt
        self.snake_move_timer: int = 150
        move_snake_event: pygame.USEREVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(move_snake_event, self.snake_move_timer)
        
        self.running, self.playing = True, True
        self.actions = {"left": False, "right": False, "up" : False, "down" : False, "action1" : False, "action2" : False, "start" : False}
        self.dt, self.prev_time = 0, 0
        
        # create background
        self.background = Background(self)
        
        # create game field
        self.game_world = Game_world(self)
        
    def game_loop(self):
        while self.playing:
            self.get_events()
            self.background.draw_background()
            self.game_world.draw_border()

            pygame.display.flip()
            # self.update()
            
    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                pygame.quit()
        #     if event.type == move_snake_event:
        #         snake.update_tile_position_body()
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     snake.set_direction(1)
        # if keys[pygame.K_d]:
        #     snake.set_direction(2)
        # if keys[pygame.K_s]:
        #     snake.set_direction(3)
        # if keys[pygame.K_a]:
        #     snake.set_direction(4)
        
    # def update():
    #     draw_field_border(screen)
    #     snake.draw()
    #     fruit.draw()
    #     eat_fruit.draw()
    
if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()