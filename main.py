import pygame 
from data import *
from classes import *
pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("PinPongi")

def run():
    walll1 = Walll(20, 50, wall1)
    walll2 = Walll(180, 50, wall2)
    game = True
    while game:
        window.blit(walll1.image, (walll1.x, walll1.y))
        window.blit(walll2.image, (walll2.x, walll2.y))
        walll1.walll_move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_w:
                    walll1.move["UP"] = True
                if event.type == pygame.K_s:
                    walll1.move["DOWN"] = True
            if event.type == pygame.KEYUP:
                if event.type == pygame.K_w:
                    walll1.move["UP"] = False
                if event.type == pygame.K_s:
                    walll1.move["DOWN"] = False

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_UP:
                    walll2.move["UP"] = True
                if event.type == pygame.K_DOWN:
                    walll2.move["DOWN"] = True
            if event.type == pygame.KEYUP:
                if event.type == pygame.K_UP:
                    walll2.move["UP"] = False
                if event.type == pygame.K_DOWN:
                    walll2.move["DOWN"] = False
            

        

        pygame.display.flip()
run()     
