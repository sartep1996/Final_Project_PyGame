import pygame as pg 
import sys

pg.init()

SCREEN = pg.display.set_mode((800, 600))
pg.display.set_caption("MENU")

BACKGROUNG = pg.image.load('Images/Background/menu_background.png')

from main_play import main_game_lvl_1
from button import Button


def get_font(size): # Returns Press-Start-2P in the desired size
    return pg.font.Font('assets/fonts/Rhuma Sinera Regular.ttf', size)


def main_menu():
    while True:
        SCREEN.blit(BACKGROUNG, (0, 0))

        MENU_MOUSE_POS = pg.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(540, 100))
    


        play_image_raw = pg.image.load("assets/fonts/Play Butto for game.png")
        play_image = pg.transform.scale(play_image_raw.convert_alpha(), (300, 100))
        
        quit_image_raw = pg.image.load("assets/fonts/Quit button for game.png")
        quit_image = pg.transform.scale(quit_image_raw.convert_alpha(), (300, 100))
        
        
        PLAY_BUTTON = Button(play_image, pos=(340, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
        # OPTIONS_BUTTON = Button(image=pg.image.load("assets/Options Rect.png"), pos=(640, 400), 
        #                     text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(quit_image, pos=(340, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_game_lvl_1()
            
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.update()

main_menu()