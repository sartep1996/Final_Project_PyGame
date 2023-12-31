import pygame as pg
from global_stuff.button import Button


def pause(screen):
    from main_menu import main_menu
    pg.init()
    paused = True

    def get_font(size): 
        return pg.font.Font('assets/fonts/Rhuma Sinera Regular.ttf', size)

    PAUSE_MENU_MOUSE_POS = pg.mouse.get_pos()

    PAUSE_MENU_TEXT = get_font(100).render("PAUSE", True, "#b68f40")
    PAUSE_MENU_RECT = PAUSE_MENU_TEXT.get_rect(center=(400, 100))

    play_image_raw = pg.image.load("assets/fonts/text_background.png")
    play_image = pg.transform.scale(play_image_raw.convert_alpha(), (300, 100))
        
    quit_image_raw = pg.image.load("assets/fonts/text_background.png")
    quit_image = pg.transform.scale(quit_image_raw.convert_alpha(), (400, 100))

    CONTINUE_BUTTON = Button(play_image, pos=(400, 280),
                text_input="CONTINUE", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")

            
    QUIT_TO_MENU = Button(quit_image, pos=(400, 380), 
                text_input="QUIT TO MENU", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")

    
    screen.blit(PAUSE_MENU_TEXT, PAUSE_MENU_RECT)

    while paused:
        screen.fill("black")
        PAUSE_MENU_MOUSE_POS = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    paused = False
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if CONTINUE_BUTTON.checkForInput(PAUSE_MENU_MOUSE_POS):
                    paused = False

                if QUIT_TO_MENU.checkForInput(PAUSE_MENU_MOUSE_POS):
                    main_menu()
                
        screen.blit(PAUSE_MENU_TEXT, PAUSE_MENU_RECT)
        CONTINUE_BUTTON.changeColor(PAUSE_MENU_MOUSE_POS)
        CONTINUE_BUTTON.update(screen)
        QUIT_TO_MENU.changeColor(PAUSE_MENU_MOUSE_POS)
        QUIT_TO_MENU.update(screen)

                
        pg.display.update()


if __name__ == "__main__":
    pause()