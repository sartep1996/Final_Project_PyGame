import pygame as pg
from pause import pause
import json
from cutscene import run_cutscene


    

def main_game_lvl_final(game_state):

    

    pg.init()
    pg.mixer.init()
    clock = pg.time.Clock()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #background imagesd
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_lvl_2 = pg.transform.scale(pg.image.load('Images/Background/bg_lvl_final.png'), (800, 600))


    from player_movement_refactoring import player, pistol_shot_wav
    from monster_1 import monster2, monster3
    from global_functions import collision_with_static_object, collision_with_moving_object
    from boundries import boundries_lvl_final, boundries

    pistol_taken = game_state['pistol_taken']

    if pistol_taken:
        player_condition = player.player_rect_pistol
    else:
        player_condition = player.player_rect

    player_condition.topleft = (100, 500)
   
            
    player_health = game_state['player_health']
    player.health = player_health
  
    side_rect_left = pg.Rect((0, 400, 25, 200))

    side_rect_right = pg.Rect((775, 400, 25, 200))

    ship = pg.transform.scale(pg.image.load("Images/Background_objects/ship.png"), (250, 250))
    ship_rect = ship.get_rect()
    ship_rect.topleft = (400, 50)

 
    global paused
    paused = False

    pistol_taken = game_state['pistol_taken']

    if pistol_taken == True:
        player_condition = player.player_rect_pistol    

    run = True
    while run:
        clock.tick(60)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    paused = True
                    pause(screen)
                else:
                    if paused:
                       paused = False
                       player.player_update_pistol(screen)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and player_condition == player.player_rect_pistol:
                    pistol_shot_wav.play()
                    print(monster2.monster_rect.x, monster2.monster_rect.y )
                    print(monster3.monster_rect.x, monster3.monster_rect.y )



        collision_with_static_object(player_condition, side_rect_left, 10)
        collision_with_static_object(player_condition, side_rect_right, 10)
        collision_with_static_object(player_condition, ship_rect, 10 )

        
        player.main_player_movement_pistol()
        player.player_update(screen)

        
        boundries_lvl_final(player_condition)

        pg.draw.rect(screen, (0, 0, 0, 0), side_rect_right)
        pg.draw.rect(screen, (0, 0, 0, 0), side_rect_left)

        screen.fill((0, 0, 0))
        screen.blit(background_lvl_2, (0,0))
        screen.blit(ship, ship_rect)

        # if player_condition.colliderect(ship_rect):
        #     run_cutscene(player_condition, ship_rect, screen)
        
        if ship_rect.colliderect(player_condition):
            run_cutscene(screen)


        if player.health == 0:
            player.draw_player_death_animation()


        if player_condition == player.player_rect_pistol:
            player.draw_pistol_player(screen)
        else:
            player.draw(screen)

        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and player_condition == player.player_rect_pistol:
            delta_time = clock.tick(60)
            player.draw_flash(screen, delta_time)

        player.draw_health_bar(screen, 10, 10)

        


        pg.display.update()


        
    pg.quit()

if __name__ == "__main__":

    def load_game():
        with open('saves/save_game.json', 'r') as file:
            game_state = json.load(file)
        
        return game_state

    game_state = load_game()
    main_game_lvl_final(game_state)
