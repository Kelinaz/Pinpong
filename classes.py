import pygame
from data import *

class Walll(pygame.Rect):
    def __init__(self, x, y, image, width = 10, height = 50, step = 2):
        super().__init__(width, height, x, y)
        self.move = {"UP":False, "DOWN":False}
        self.x = x
        self.y = y
        self.image = image 

    def walll_move(self):
        if self.move["UP"] and self.y > 0:
            self.y -= self.step
        elif self.move["DOWN"] and self.y - self.height < setting_win["HEIGHT"]:
            self.y += self.step
    
