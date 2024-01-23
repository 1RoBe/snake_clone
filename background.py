import pygame

class Background:
    def __init__(self, game):
        self.game = game
        self.color = (255, 0, 0)
        
    def draw_background(self):
        self.game.screen.fill(self.color)