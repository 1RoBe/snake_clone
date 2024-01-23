import os, time, pygame
# Load our scenes
from states.title import Title

class Game():
        def __init__(self):
            pygame.init()
            
            # tiles
            self.TILE_SIZE: int = 32
            self.TILES_X: int = 17
            self.TILES_Y: int = 15
            # maybe name it Field coords
            self.TILE_DIMENSION: list[list[int], 
                                      list[int]] = [[0, self.TILES_X - 1], 
                                                    [0, self.TILES_X - 1]]
            # window
            self.MARGIN_LEFT: int = 20
            self.MARGIN_RIGHT: int = 20
            self.MARGIN_TOP: int = 100
            self.MARGIN_BOTTOM: int = 20
            
            # game field
            self.FIELD_WIDTH: int = self.TILE_SIZE * self.TILES_X
            self.FIELD_HEIGHT: int = self.TILE_SIZE * self.TILES_Y
            self.FIELD_DIMENSION: list[list[int], 
                                       list[int]] = [[self.MARGIN_LEFT,
                                                      self.MARGIN_LEFT + self.FIELD_WIDTH],
                                                     [self.MARGIN_TOP,
                                                      self.MARGIN_TOP + self.FIELD_HEIGHT]]
            # game dimension
            self.GAME_WIDTH: int = self.MARGIN_LEFT + self.FIELD_WIDTH + self.MARGIN_RIGHT
            self.GAME_HEIGHT: int = self.MARGIN_TOP + self.FIELD_HEIGHT + self.MARGIN_BOTTOM
            
            # screen dimension
            self.SCREEN_WIDTH: int = self.GAME_WIDTH
            self.SCREEN_HEIGHT: int = self.GAME_HEIGHT
            
            # set up canvas and screen
            self.game_canvas = pygame.Surface((self.SCREEN_HEIGHT, self.SCREEN_HEIGHT))
            self.screen = pygame.display.set_mode((self.SCREEN_HEIGHT, self.SCREEN_HEIGHT))
            
            # create timer for choppy snake movemnt
            self.snake_move_timer: int = 150
            move_snake_event: pygame.USEREVENT = pygame.USEREVENT + 1
            pygame.time.set_timer(move_snake_event, self.snake_move_timer)
            
            
            self.running, self.playing = True, True
            self.actions = {"left": False, "right": False, "up" : False, "down" : False, "action1" : False, "action2" : False, "start" : False}
            self.dt, self.prev_time = 0, 0
            self.state_stack = []
            self.load_assets()
            self.load_states()

        def game_loop(self):
            while self.playing:
                self.get_dt()
                self.get_events()
                self.update()
                self.render()

        def get_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                        self.running = False
                    if event.key == pygame.K_a:
                        self.actions['left'] = True
                    if event.key == pygame.K_d:
                        self.actions['right'] = True
                    if event.key == pygame.K_w:
                        self.actions['up'] = True
                    if event.key == pygame.K_s:
                        self.actions['down'] = True
                    if event.key == pygame.K_p:
                        self.actions['action1'] = True
                    if event.key == pygame.K_o:
                        self.actions['action2'] = True    
                    if event.key == pygame.K_RETURN:
                        self.actions['start'] = True  

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.actions['left'] = False
                    if event.key == pygame.K_d:
                        self.actions['right'] = False
                    if event.key == pygame.K_w:
                        self.actions['up'] = False
                    if event.key == pygame.K_s:
                        self.actions['down'] = False
                    if event.key == pygame.K_p:
                        self.actions['action1'] = False
                    if event.key == pygame.K_o:
                        self.actions['action2'] = False
                    if event.key == pygame.K_RETURN:
                        self.actions['start'] = False  

        def update(self):
            self.state_stack[-1].update(self.dt,self.actions)

        def render(self):
            self.state_stack[-1].render(self.game_canvas)
            # Render current state to the screen
            # self.screen.blit(pygame.transform.scale(self.game_canvas,(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
            self.screen.blit(self.game_canvas, (0,0))
            pygame.display.flip()


        def get_dt(self):
            now = time.time()
            self.dt = now - self.prev_time
            self.prev_time = now

        def draw_text(self, surface, text, color, x, y):
            text_surface = self.font.render(text, True, color)
            #text_surface.set_colorkey((0,0,0))
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            surface.blit(text_surface, text_rect)

        def load_assets(self):
            # Create pointers to directories 
            self.assets_dir = os.path.join("assets")
            # self.sprite_dir = os.path.join(self.assets_dir, "sprites")
            self.font_dir = os.path.join(self.assets_dir, "font")
            self.font= pygame.font.Font(os.path.join(self.font_dir, "joystix_monospace.otf"), 20)

        def load_states(self):
            self.title_screen = Title(self)
            self.state_stack.append(self.title_screen)

        def reset_keys(self):
            for action in self.actions:
                self.actions[action] = False


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()