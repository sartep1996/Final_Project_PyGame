import pygame as pg

pg.init()
clock = pg.time.Clock()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BOUNDRY_LEFT = 25
BOUNDRY_TOP = 25
BOUNDRY_RIGHT = SCREEN_WIDTH - 25
BOUNDRY_BOTTOM = SCREEN_HEIGHT - 25
#creates a game screen
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#background image
original_background_lvl_1 = pg.image.load('Images/Background/bg_lvl_1.png')
background_lvl_1 = pg.transform.scale(original_background_lvl_1, (800, 600))

from player_movement import player


run = True
while run:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    player.main_player_movement()
    player.animate()

    if player.player_rect.left < BOUNDRY_LEFT:
        player.player_rect.left = BOUNDRY_LEFT
    if player.player_rect.right > BOUNDRY_RIGHT:
        player.player_rect.right = BOUNDRY_RIGHT 
    if player.player_rect.top < BOUNDRY_TOP:
        player.player_rect.top = BOUNDRY_TOP 
    if player.player_rect.bottom > BOUNDRY_BOTTOM:
       player.player_rect.bottom = BOUNDRY_BOTTOM

    #black screen fill for default, all images are on top of it
    screen.fill((0, 0, 0))
    #adding background of level 1
    screen.blit(background_lvl_1, (0,0))
   
    
    player.draw(screen)

   
    
    pg.display.update()


    #this part of code is responsible for boundries
    # pg.display.update()

pg.quit()