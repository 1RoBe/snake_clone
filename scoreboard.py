import pygame
import shelve

class Scoreboard:
    def __init__(self, game):
        self.game = game
        self.color = (255, 0, 0)
    
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
        pass
            
    def draw(self, score):
        WHITE: tuple[int] = (255, 255, 255)
        BLACK: tuple[int] = (0, 0, 0)
        # background
        self.game.screen.fill(self.color)
        # score
        self.game.draw_text(f"Score: {self.game.score}", BLACK, self.game.game_world.MARGIN_LEFT - 2, 7)
        self.game.draw_text(f"Highscore: {self.game.highscore}", BLACK, self.game.game_world.MARGIN_LEFT + 250, 7)
        # self.game.draw_text(self.game.screen, f"Score: {self.game.score}", (255, 255, 255), self.game.game_world.MARGIN_LEFT - 2, 7)

    
    # def get_highscore(self) -> int:
    #     with shelve.open('highscore') as hs_db:
    #         if hs_db['highscore'] == None:
    #                 return 0
    #         else:
    #             return hs_db['highscore']

            
    
    