import pygame 
from data import *
from classes import *
from random import*
from time import *
pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("PinPongi")
click = False
def menu():
    global replay
    replay = False
    global menu_while
    menu_while = True
    clock = pygame.time.Clock()
    button_1 = pygame.Rect(50, 20, 150, 50)
    button_2 = pygame.Rect(50, 90, 150 , 50)
    button_3 = pygame.Rect(50, 160, 150, 50)
    font_text = pygame.font.Font(None, 25)
    while menu_while:
        window.blit(board_image,(0,0))
        mx, my = pygame.mouse.get_pos()
        
        if button_1.collidepoint((mx,my)):
            if click:
                menu_while = False
                run()
        if button_2.collidepoint((mx,my)):
            if click:
                pass
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()

        if replay == True:
            menu_while = False
            run()

        pygame.draw.rect(window, (0, 255, 170), button_1)
        pygame.draw.rect(window, (255, 255, 0), button_2)
        pygame.draw.rect(window, (255, 0, 0), button_3)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu_while = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                if event.button == 2:
                    click = True
        window.blit(font_text.render(f"Quit", True, (0,0,0)), (105, 175))
        window.blit(font_text.render(f"Play", True, (0,0,0)), (105, 35))
        window.blit(font_text.render(f"History", True, (0,0,0)), (100, 105))
        pygame.display.flip()
        clock.tick(setting_win["FPS"])
            




def run():
    wall1_obj = Wall(20, 90, wall1_image, 2)
    wall2_obj = Wall(220, 90, wall2_image, 2)
    ball_obj = Ball(120, 120, ball_image, 1, 1)
    right_or_left = randint(1, 2)
    up_or_down = randint(3,4)
    clock = pygame.time.Clock()
    font_text = pygame.font.Font(None, 25)
    global replay
    replay = False


    #menu = Menu()
    #menu.append_option("Play with friend", lambda: print("Play with friend"))
    #menu.append_option("QUIT", quit)
    game = True
    while game:
        window.blit(board_image,(0,0))
        window.blit(wall1_obj.image, (wall1_obj.x, wall1_obj.y))
        window.blit(wall2_obj.image, (wall2_obj.x, wall2_obj.y))
        window.blit(ball_obj.image, (ball_obj.x, ball_obj.y))
        window.blit(font_text.render(f"Points 1: {wall1_obj.points}", True, (255, 0, 0)), (setting_win["WIDTH"] - 245, 10))
        window.blit(font_text.render(f"Points 2: {wall2_obj.points}", True, (0, 0, 250)), (setting_win["WIDTH"] - 90, 10))
        wall1_obj.wall_move()
        wall2_obj.wall_move()
        ball_obj.ball_move(wall1_obj, wall2_obj, right_or_left, up_or_down, game)
        #menu.draw(window, 20, 20, 10)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    wall1_obj.move["UP"] = True
                if event.key == pygame.K_s:
                    wall1_obj.move["DOWN"] = True
                if event.key == pygame.K_UP:
                    wall2_obj.move["UP"] = True
                if event.key == pygame.K_DOWN:
                    wall2_obj.move["DOWN"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    wall1_obj.move["UP"] = False
                if event.key == pygame.K_s:
                    wall1_obj.move["DOWN"] = False
                if event.key == pygame.K_UP:
                    wall2_obj.move["UP"] = False
                if event.key == pygame.K_DOWN:
                    wall2_obj.move["DOWN"] = False
            #if event.type == pygame.MOUSEBUTTONDOWN:


                
            
        if wall1_obj.points == 2:
            window.blit(font_text.render(f"Перший граець виграв", True, (255, 0,0)), (30, 140))
            replay = True
            game = False
            menu()
        if wall2_obj.points == 2:
            window.blit(font_text.render(f"Другий граець виграв", True, (255, 0,0)), (30, 140))
            replay = True
            game= False
            menu()
        pygame.display.flip()
        clock.tick(setting_win["FPS"])
menu()    
