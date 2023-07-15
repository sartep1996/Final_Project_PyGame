import pygame as pg
from pause import pause
import json


def save_game(playerx, playery, monsterx,  monstery, health, monster_health):
    game_state = {
        'player_position': (playerx, playery),
        'monster_position': (monsterx, monstery),
        'player_health': health,
        'monster_health': monster_health
    }

    with open('saves/save_game.json', 'w') as file:
        json.dump(game_state, file)
        # player.player_update(screen)

def main_game_lvl_1(game_state):

    

    pg.init()
    pg.mixer.init()
    clock = pg.time.Clock()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #background imagesd
    original_background_lvl_1 = pg.image.load('Images/Background/bg_lvl_1.png')
    background_lvl_1 = pg.transform.scale(original_background_lvl_1, (800, 600))


    from player_movement_refactoring import player, pistol_shot_wav
    from monster_1 import monster1
    from background_objects import plane_b_object
    from global_functions import collision_with_static_object, collision_with_moving_object
    from boundries import boundries_lvl_1, boundries

    player_condition = player.player_rect
    player.player_rect.x, player.player_rect.y = player.player_rect_pistol.x, player.player_rect_pistol.y

    player_position = game_state['player_position']
    player_condition.centerx = player_position[0]
    player_condition.centery = player_position[1]
   
    monster_position = game_state['monster_position']
    monster1.monster_rect.x = monster_position[0]
    monster1.monster_rect.y = monster_position[1]
        
    player_health = game_state['player_health']
    monster_health = game_state['monster_health']

    player.health = player_health
    monster1.monster_health = monster_health

    screen_rect = screen.get_rect()
    plane_b_object_rect = plane_b_object.get_rect()
    plane_b_object_rect.topleft = (40, 400)

    save_icon = pg.transform.scale(pg.image.load('Images/save_icon/save_icon.png').convert_alpha(), (50, 50))
    save_icon_rect = save_icon.get_rect()
    save_icon_rect.topleft = (400, 450)

    pistol_icon = pg.transform.scale(pg.image.load('Images/gun_sprites/pistol_image.png').convert_alpha(), (50, 50))
    pistol_icon_rect = pistol_icon.get_rect()
    pistol_icon_rect.topleft = (500, 100)

    pass_mark_rect = pg.Rect((570, -20, 170, 60))

    global paused
    paused = False

    

    save_icon_visible = False
    pistol_icon_visible = False

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
                    print(monster1.monster_rect.x, monster1.monster_rect.y )

            # if player_condition.colliderect(save_icon_rect):
            #     save_game(player_condition.centerx,  player_condition.centery, monster1.monster_rect.x, monster1.monster_rect.y, player.health, monster1.monster_health)
            #     save_icon_visible = False

            # # player.player_rect.x, player.player_rect.y = player.player_rect_pistol.x, player.player_rect_pistol.y
            # if player.player_rect.colliderect(pistol_icon_rect):
            #     if player_condition == player.player_rect:
            #         player_condition = player.player_rect_pistol
            #         player.player_rect_pistol.x, player.player_rect_pistol.y = player.player_rect.x, player.player_rect.y

            #         pistol_icon_visible = False
            #     else:
            #         player_condition = player.player_rect
            #         pistol_icon_visible = True


        
        if monster1.monster_attack_player(player_condition , screen):
            damage = monster1.monster_attack_player(player_condition, screen)
            if damage > 0:
                player.take_damage(damage)
        

        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            if player_condition == player.player_rect_pistol:
                if player.is_facing_monster(monster1.monster_rect):
                    damage = player.damage()
                    if damage > 0:
                        monster1.take_damage(damage)


        monster1.monster_update_patrol(player_condition, screen)

        player.main_player_movement_pistol()
        player.player_update(screen)


        boundries_lvl_1(player_condition)
        boundries(monster1.monster_rect)

        collision_with_static_object(player_condition, plane_b_object_rect, 10)
        collision_with_static_object(monster1.monster_rect, plane_b_object_rect, 10)
        collision_with_moving_object(player_condition, monster1.monster_rect, 10, player.movement_speed, monster1.movement_speed,  screen_rect)

        
        
        screen.fill((0, 0, 0))
        screen.blit(background_lvl_1, (0,0))
        
        screen.blit(plane_b_object, plane_b_object_rect) 
        monster1.draw_monster(screen)
        monster1.draw_health_bar(screen, 690, 10)

        pg.draw.rect(screen, (10, 0, 50, 0), pass_mark_rect)

        if save_icon_visible:
            screen.blit(save_icon, save_icon_rect.topleft)
       
        if pistol_icon_visible:
            screen.blit(pistol_icon, pistol_icon_rect.topleft)
        
        
        if player.health == 0:
            player.draw_player_death_animation()

        # if monster1.monster_health == 0:
        #     monster1.should_follow_player = False
        #     monster1.patrol_mode = False
        #     monster1.monster_is_attacking = False
        #     monster1.draw_monster_death_animation()
            

        
        player.draw(screen)

        # keys = pg.key.get_pressed()
        # if keys[pg.K_SPACE] and player_condition == player.player_rect_pistol:
        #     delta_time = clock.tick(60)
        #     player.draw_flash(screen, delta_time)

        player.draw_health_bar(screen, 10, 10)

        with open('saves/save_game.json', 'r') as file:
            game_state = json.load(file)

        if player_condition.colliderect(pass_mark_rect):
            from main_play_2 import main_game_lvl_2
            main_game_lvl_2(game_state)

        pg.display.update()


        
    pg.quit()

if __name__ == "__main__":

    def load_game():
        with open('saves/new_game.json', 'r') as file:
            game_state = json.load(file)
        
        return game_state

    game_state = load_game()
    main_game_lvl_1(game_state)
