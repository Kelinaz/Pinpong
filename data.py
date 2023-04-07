import pygame
import os 

abs_path = os.path.abspath(__file__+ "/..") + "\\image\\"

setting_win = {
    "WIDTH": 250,
    "HEIGHT": 250
}



wall1 = pygame.image.load("image\\1.png")
wall2 = pygame.image.load("image\\2.png")
ball = pygame.image.load("image\\ball.png")