import pygame
from data import *
from random import * 
from time import *
pygame.init()
#arial = pygame.font.Font(None, 50)


class Wall(pygame.Rect):
    def __init__(self, x, y, image, speed, width = 10, height = 50):
        super().__init__(x,y,width,height)
        self.move = {"UP":False, "DOWN":False}
        self.points = 0
        self.image = image 
        self.speed = speed

    def wall_move(self):
        if self.move["UP"] and self.y > 0:
            self.y -= self.speed
        elif self.move["DOWN"] and self.y + self.height < setting_win["HEIGHT"]:
            self.y += self.speed


#lass Menu():
#   def __init__(self):
#       self._option_surfaces = []
#       self._callbacks = []
#       self._current_option_index = []
#   def append_option(self, option, callback):
#       self._option_surfaces.append(arial.render(option, True, (0, 250, 0)))
#       self._callbacks.append(callback)
#   def switch(self, direction):
#       self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))
#   def select(self):
#       self._callbacks[self._current_option_index]()
#   def draw(self, surf, x, y, option_y_padding):
#       for i, option in enumerate(self._option_surfaces):
#           option_rect = option.get_rect()
#           option_rect.topleft = (x,y + i * option_y_padding)
#           if i == self._current_option_index:
#               pygame.draw.rect(surf, (0, 100, 0), option_rect)
#           surf.blit(option, option_rect)
#






class Ball(pygame.Rect):
    def __init__(self, x, y ,image,speed_x,speed_y, width = 5, height = 5):
        super().__init__(x, y, width, height)
        self.image = image
        self.speed_x = speed_x
        self.speed_x = choice([self.speed_x, -self.speed_x])
        self.speed_y = speed_y


    def ball_move(self, wall1, wall2, right_or_left, up_or_down, game):
        #if right_or_left == 1:
       #    print("1")
        #    self.x -= self.speed_x
        #    if self.colliderect(wall1):
        #        print("6")
        #        self.speed_x *= -1
        #        if up_or_down == 3:
        #            self.speed_y *= -1
        #        if up_or_down == 4:
        #            pass
        #        right_or_left = 0
#
        #elif right_or_left == 2:
        #    print("2")
        #    self.x += self.speed_x
        #    if self.colliderect(wall2):
        #        print("7")
        #        self.speed_x *= -1
        #        if up_or_down == 3:
        #            self.speed_y *= -1
        #        if up_or_down == 4:
        #            pass
        #        right_or_left = 0 

        if self.y == 0:
            self.speed_y *= -1
        elif self.y == setting_win["HEIGHT"] - self.height:
            self.speed_y *= -1
        elif self.x >= setting_win["WIDTH"] - self.width:
            wall1.points +=1
            self.x = 120
            self.y = 120
            sleep(2)
        elif self.x == 0:
            wall2.points += 1
            self.x = 120
            self.y = 120
            sleep(2)

        if self.colliderect(wall1):
            self.speed_x *= -1
            self.speed_y *= 1
        elif self.colliderect(wall2):
            self.speed_x *= -1
            self.speed_y *= 1
        
        #if right_or_left == 0:
        self.y += self.speed_y
        self.x += self.speed_x

        





        #if right_or_left == 1:
        #    self.speed_x *= -1
        #    self.x += self.speed_x
        #    self.y += self.speed_y
        #    if self.colliderect(wall):
        #        self.speed_x *= -1
        #        if up_or_down == 3:
        #            if self.speed_y < 0:
        #                self.speed_y *= -1
        #            self.y += self.speed_y
        #        elif up_or_down == 4:
        #            if self.speed_y < 0:
        #                self.speed_y *= -1
        #            self.y += self.speed_y
        #    elif self.colliderect(wall2):
        #        self.speed_x *= -1
        #        if up_or_down == 3:
        #            if self.speed_y < 0:
        #                self.speed_y *= -1
        #            self.y += self.speed_y
        #        elif up_or_down == 4:
        #            if self.speed_y < 0:
        #                self.speed_y *= -1
        #            self.y += self.speed_y

       # if right_or_left == 1:
       #     self.x += -self.speed_x
       # if up_or_down == 3:
       #         self.speed_y *= -1
       # if up_or_down == 4:
       #         self.speed_y *= 1
       # if self.colliderect(wall):
       #     self.x += self.speed_x
#
       #     self.y += self.speed_y
       # if self.colliderect(wall2):
       #     self.speed_x *= -1
       #     
       #     
#
#
       #     
#
       # elif right_or_left == 2:
       #     self.x += self.speed_x

        #if self.colliderect(wall):
        #    if up_or_down == 3:
        #        self.speed_y = 1
        #        self.speed_y *= -1
        #    elif up_or_down == 4:
        #        self.speed_y = 1
        #        self.speed_y *= -1
        #    self.y += self.speed_y
        #    self.x += self.speed_x
        #elif self.colliderect(wall2):
        #    if up_or_down == 3:
        #        self.speed_y = 1
        #        self.speed_y *= -1
        #        self.y += self.speed_y
        #    elif up_or_down == 4:
        #        self.speed_y = 1
        #        self.speed_y *= -1
        #        self.y += self.speed_y
        #    self.x -= self.speed_x
#
        #if self.y == setting_win["HEIGHT"]:
        #    self.y *= -1
        #self.x += self.speed_x
        #self.y += self.speed_y


#class Menu(pygame.Rect):
#    def __init__(self, x, y, width, height, image):
#        super().init(x,y,width,height)
#        self.image = image
#        mx, my = pygame.mouse.get_pos()
#        click = False 
#
#    def button_click(self, window, mx, my, click):
#        if self.collidepoint((mx, my)):
#            if click:
#                pass
#        if self.collidepoint((mx,my)):
#            if click:
#                pass
        


        


