import pygame
import shelve

class Scoreboard:
    def __init__(self, game):
        self.game = game
        self.color: dict = {"BLACK": (0, 0, 0), "WHITE": (255, 255, 255), "RED": (255, 0, 0)}
    
    def get_highscore(self) -> int:
        with shelve.open('highscore') as hs_db:
            try:
                return hs_db['highscore'] if hs_db['highscore'] else 0
            except:
                hs_db['highscore'] = 0
                return 0
            
    def save_highscore(self):
        with shelve.open('highscore') as hs_db:
            hs_db['highscore'] = self.game.highscore
            
    def draw(self, score):
        self.game.screen.fill(self.color["RED"])
        pygame.draw.rect(self.game.screen, self.color['BLACK'], 
                         (self.game.game_world.MARGIN_LEFT - self.game.game_world.BORDER_WIDTH, 
                          5, 
                          self.game.game_world.FIELD_WIDTH + 2 * self.game.game_world.BORDER_WIDTH, 35))
        self.game.draw_text(f"Score: {self.game.score}", self.color["WHITE"], self.game.game_world.MARGIN_LEFT - 2, 7)
        self.game.draw_text(f"Highscore: {self.game.highscore}", self.color["WHITE"], self.game.game_world.MARGIN_LEFT + 250, 7)


            
    
    