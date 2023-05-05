import pygame
import os 
import json

abs_path = os.path.abspath(__file__+ "/..") + "\\image\\"
history = dict()
with open("history.json", "r", encoding = "utf-8") as file:
    history = json.load(file)

setting_win = {
    "WIDTH": 250,
    "HEIGHT": 250,
    "FPS": 60
}

back_to_menu = pygame.image.load("image\\back_to_menu.png")
history_screen = pygame.image.load("image\\history_screen.png")
board_image = pygame.image.load("image\\board.png")
wall1_image = pygame.image.load("image\\1.png")
wall2_image = pygame.image.load("image\\2.png")
ball_image = pygame.image.load("image\\ball.png")