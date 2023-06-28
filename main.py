import pygame as pg

pg.init()
clock = pg.time.Clock()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#background imagesd
original_background_lvl_1 = pg.image.load('Images/Background/bg_lvl_1.png')
background_lvl_1 = pg.transform.scale(original_background_lvl_1, (800, 600))


from player_movement import player
from monster_1 import monster1
from background_objects import plane_b_object
from collision_functions import collision_with_static_object
from boundries import boundries


plane_b_object_rect = plane_b_object.get_rect()
plane_b_object_rect.topleft = (40, 400)


run = True
while run:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    player.main_player_movement()
    player.animate()
    
    monster1.monster_update()
    monster1.monster_animate()

    boundries(player.player_rect)
    boundries(monster1.monster_rect)
    

    collision_with_static_object(player.player_rect, plane_b_object_rect, 10)
    
        
    #black screen fill for default, all images are on top of it
    screen.fill((0, 0, 0))
    #adding background of level 1
    screen.blit(background_lvl_1, (0,0))

    screen.blit(plane_b_object, plane_b_object_rect)
   
    
    monster1.draw_monster(screen)
    player.draw(screen)
   
    
    pg.display.update()
    
pg.quit()