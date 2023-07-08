import pygame as pg
from button import Button
from main_menu import main_menu, SCREEN




def pause(screen):
    pg.init()
    paused = True

    def get_font(size): 
        return pg.font.Font('assets/fonts/Rhuma Sinera Regular.ttf', size)



    PAUSE_MENU_MOUSE_POS = pg.mouse.get_pos()

    PAUSE_MENU_TEXT = get_font(100).render("PAUSE", True, "#b68f40")
    PAUSE_MENU_RECT = PAUSE_MENU_TEXT.get_rect(center=(540, 100))

    play_image_raw = pg.image.load("assets/fonts/Play Butto for game.png")
    play_image = pg.transform.scale(play_image_raw.convert_alpha(), (300, 100))
        
    quit_image_raw = pg.image.load("assets/fonts/Quit button for game.png")
    quit_image = pg.transform.scale(quit_image_raw.convert_alpha(), (300, 100))

    CONTINUE_BUTTON = Button(play_image, pos=(340, 250),
                text_input="CONTINUE", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")

            
    QUIT_TO_MENU = Button(quit_image, pos=(340, 550), 
                text_input="QUIT TO MENU", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")

    
    SCREEN.blit(PAUSE_MENU_TEXT, PAUSE_MENU_RECT)

    while paused:
        PAUSE_MENU_MOUSE_POS = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    paused = False
                    return True
                



            if event.type == pg.MOUSEBUTTONDOWN:
                if CONTINUE_BUTTON.checkForInput(PAUSE_MENU_MOUSE_POS):
                    paused = False
          
        
                if QUIT_TO_MENU.checkForInput(PAUSE_MENU_MOUSE_POS):
                    return
                
        screen.blit(PAUSE_MENU_TEXT, PAUSE_MENU_RECT)
        CONTINUE_BUTTON.changeColor(PAUSE_MENU_MOUSE_POS)
        CONTINUE_BUTTON.update(screen)
        QUIT_TO_MENU.changeColor(PAUSE_MENU_MOUSE_POS)
        QUIT_TO_MENU.update(screen)

                
        pg.display.update()



if __name__ == "__main__":
    pause()