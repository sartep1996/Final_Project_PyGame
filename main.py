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
player.set_position(350, 350)
from monster_1 import monster1
monster1.set_position(200, 200)
from background_objects import plane_b_object
from global_functions import collision_with_static_object, collision_with_moving_object, player_taking_damage
from boundries import boundries

screen_rect = screen.get_rect()
plane_b_object_rect = plane_b_object.get_rect()
plane_b_object_rect.topleft = (40, 400)
# monster1_rect = monster1.get_rect()


run = True
while run:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    player.player_update(screen)

    if monster1.monster_attack_player(player.player_rect, screen):
        damage = monster1.monster_attack_player(player.player_rect, screen)
        if damage > 0:
            player.take_damage(damage)

    monster1.monster_update(player.player_rect, screen)
    boundries(player.player_rect)
    boundries(monster1.monster_rect)
    collision_with_static_object(player.player_rect, plane_b_object_rect, 10)
    collision_with_static_object(monster1.monster_rect, plane_b_object_rect, 10)
    collision_with_moving_object(player.player_rect, monster1.monster_rect, 10, player.movement_speed, monster1.movement_speed,  screen_rect)
    
    print(player.health)
    
    #black screen fill for default, all images are on top of it
    screen.fill((0, 0, 0))
    #adding background of level 1
    screen.blit(background_lvl_1, (0,0))
    screen.blit(plane_b_object, plane_b_object_rect)
    # screen.blit(monster1, monster1.monster_rect)
    monster1.draw_monster(screen)
    
    player.draw(screen)
    player.draw_health_bar(screen, 10, 10)
   
    pg.display.update()
    
pg.quit()
