import pygame as pg
from pause import pause
import json


def save_game(playerx, playery, monsterx,  monstery, monster2x, monster2y, health, monster_health, monster_health2):
    game_state = {
        'player_position': (playerx, playery),
        'monster_position': (monsterx, monstery),
        'monster_2_position':(monster2x, monster2y),
        'player_health': health,
        'monster_health': monster_health,
        'monster_health2': monster_health2

    }

    with open('saves/save_game.json', 'w') as file:
        json.dump(game_state, file)
        # player.player_update(screen)

def main_game_lvl_2(game_state):

    

    pg.init()
    pg.mixer.init()
    clock = pg.time.Clock()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #background imagesd
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_lvl_2 = pg.transform.scale(pg.image.load('Images/Background/bg_lvl_2.png'), (800, 600))


    from player_movement_refactoring import player, pistol_shot_wav
    from monster_1 import monster2, monster3
    from global_functions import collision_with_static_object, collision_with_moving_object
    from boundries import boundries_lvl_1, boundries

    player_condition = player.player_rect

    player_position = game_state['player_position']
    player_condition.centerx = player_position[0]
    player_condition.centery = player_position[1]
   
    monster_position = game_state['monster_position']
    monster2.monster_rect.centerx = monster_position[0]
    monster2.monster_rect.centery = monster_position[1]

    monster_position3 = game_state['monster_2_position']
    monster3.monster_rect.centerx = monster_position3[0]
    monster3.monster_rect.centery = monster_position3[1]
        
    player_health = game_state['player_health']
    monster2_health = game_state['monster_health']
    monster3_health = game_state['monster_health2']

    # player.set_position_pistol(player.player_rect_pistol.x, player.player_rect_pistol.y)
    # monster1.set_position(monsterx, monstery)
    player.health = player_health
    monster2.monster_health = monster2_health
    monster3.monster_health = monster3_health

    screen_rect = screen.get_rect()

    save_icon = pg.transform.scale(pg.image.load('Images/save_icon/save_icon.png').convert_alpha(), (50, 50))
    save_icon_rect = save_icon.get_rect()
    save_icon_rect.topleft = (400, 450)

    pistol_icon = pg.transform.scale(pg.image.load('Images/gun_sprites/pistol_image.png').convert_alpha(), (50, 50))
    pistol_icon_rect = pistol_icon.get_rect()
    pistol_icon_rect.topleft = (500, 100)

    pass_mark_rect = pg.Rect((570, -20, 170, 60))

    global paused
    paused = False

    

    save_icon_visible = True
    pistol_icon_visible = True

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

            if player_condition.colliderect(save_icon_rect):
                save_game(player_condition.centerx,  player_condition.centery, monster2.monster_rect.x, monster2.monster_rect.y, monster3.monster_rect.x, monster3.monster_rect.y, player.health, monster2.monster_health, monster3.monster_health)
                save_icon_visible = False

            # player.player_rect.x, player.player_rect.y = player.player_rect_pistol.x, player.player_rect_pistol.y
            if player.player_rect.colliderect(pistol_icon_rect):
                if player_condition == player.player_rect:
                    player_condition = player.player_rect_pistol
                    player.player_rect_pistol.x, player.player_rect_pistol.y = player.player_rect.x, player.player_rect.y
                    pistol_icon_rect.topleft = (-100, -100)
                    pistol_icon_visible = False
                else:
                    player_condition = player.player_rect
                    pistol_icon_visible = True


        
        monsters = [monster2, monster3]  

        for monster in monsters:
            damage = monster.monster_attack_player(player_condition, screen)
            if damage > 0:
                player.take_damage(damage)
        
        

        for monster in monsters:
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                if player.is_facing_monster(monster.monster_rect):
                    damage = player.damage()
                    if damage > 0:
                            monster.take_damage(damage)


        monster2.monster_update_patrol(player_condition, screen)
        monster3.monster_update_patrol(player_condition, screen)

        player.main_player_movement_pistol()
        player.player_update(screen)


        boundries_lvl_1(player_condition)

        for monster in monsters:
            boundries(monster.monster_rect)

        for monster in monsters:
         collision_with_moving_object(player_condition, monster.monster_rect, 10, player.movement_speed, monster.movement_speed,  screen_rect)
        
        screen.fill((0, 0, 0))
        screen.blit(background_lvl_2, (0,0))
        
        for monster in monsters:
            monster.draw_monster(screen)

        pg.draw.rect(screen, (0, 0, 0, 0), pass_mark_rect)

        
        if save_icon_visible:
            screen.blit(save_icon, save_icon_rect.topleft)
       
        if pistol_icon_visible:
            screen.blit(pistol_icon, pistol_icon_rect.topleft)
        
        
        if player.health == 0:
            player.draw_player_death_animation()

        for monster in monsters:
            if monster.monster_health == 0:
                monster.should_follow_player = False
                monster.patrol_mode = False
                monster.monster_is_attacking = False
                monster.draw_monster_death_animation()
            

        if player_condition == player.player_rect_pistol:
            player.draw_pistol_player(screen)
        else:
            player.draw(screen)

        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and player_condition == player.player_rect_pistol:
            delta_time = clock.tick(60)
            player.draw_flash(screen, delta_time)

        player.draw_health_bar(screen, 10, 10)

        

        if player.player_rect_pistol.colliderect(pass_mark_rect):
            from main_play_2 import main_game_lvl_2
            main_game_lvl_2()

        pg.display.update()


        
    pg.quit()

if __name__ == "__main__":

    def load_game():
        with open('saves/save_game.json', 'r') as file:
            game_state = json.load(file)
        
        return game_state

    game_state = load_game()
    main_game_lvl_2(game_state)
