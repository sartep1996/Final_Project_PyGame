import pygame as pg
from add_screens.pause import pause
from add_screens.death_screen import death_screen
import json
pg.mixer.init()

main_song = pg.mixer.Sound('Sounds/main_song.wav')
main_song.set_volume(0.5)


def save_game(playerx, playery, monsterx,  monstery, monster2x, monster2y, health, monster_health, monster_health2, pistol_taken):
    game_state = {
        'player_position': (playerx, playery),
        'monster_position': (monsterx, monstery),
        'monster_2_position':(monster2x, monster2y),
        'player_health': health,
        'monster_health': monster_health,
        'monster_health2': monster_health2,
        'pistol_taken': pistol_taken

    }

    with open('saves/save_game.json', 'w') as file:
        json.dump(game_state, file)
        # player.player_update(screen)

def main_game_lvl_2(game_state):

    pg.init()
    clock = pg.time.Clock()

    main_song.play()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #background imagesd
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_lvl_2 = pg.transform.scale(pg.image.load('Images/Background/bg_lvl_2.png'), (800, 600))


    from player.player_movement_refactoring import player, pistol_shot_wav
    from monster.monster_1 import monster2, monster3
    from global_stuff.global_functions import collision_with_static_object, collision_with_moving_object, overlap_with_moving_object

    from global_stuff.boundries import boundries_lvl_2, boundries

    pistol_taken = game_state['pistol_taken']

    if pistol_taken:
        player_condition = player.player_rect_pistol
    else:
        player_condition = player.player_rect

    # monsters = [monster2, monster3]
    # for monster in monsters:
    #     monster.should_follow_player = False
    #     monster.patrol_mode = True
    # monster2.monster_update_patrol(player_condition, screen)
    # monster3.monster_update_patrol(player_condition, screen)

    # monsters = [monster2, monster3]
    # for monster in monsters:
    #     monster.patrol_mode = game_state['patrol_mode']

    player_position = game_state['player_position']
    player_condition.centerx = player_position[0]
    player_condition.centery = player_position[1]
   
    monster_position = game_state['monster_position']
    monster_position3 = game_state['monster_2_position']
    monster2.monster_rect.topleft = (monster_position[0], monster_position[1])
    monster3.monster_rect.topleft = (monster_position3[0], monster_position3[1])
            
    player.health = game_state['player_health']
    monster2.monster_health = game_state['monster_health']
    monster3.monster_health = game_state['monster_health2']

    screen_rect = screen.get_rect()

    save_icon = pg.transform.scale(pg.image.load('Images/save_icon/save_icon.png').convert_alpha(), (50, 50))
    save_icon_rect = save_icon.get_rect()
    save_icon_rect.topleft = (550, 450)

    pistol_icon = pg.transform.scale(pg.image.load('Images/gun_sprites/pistol_image.png').convert_alpha(), (50, 50))
    pistol_icon_rect = pistol_icon.get_rect()
    pistol_icon_rect.topleft = (500, 100)

    pass_mark_rect = pg.Rect((500, -20, 170, 60))
    block_rect = pg.Rect(620, -20, 170, 60)

    global paused
    paused = False


    monster2.patrol_mode = True
    monster3.patrol_mode = True
    
    save_icon_visible = True
    pistol_icon_visible = True
    pistol_taken = game_state['pistol_taken']

    if pistol_taken == True:
        player_condition = player.player_rect_pistol
        pistol_icon_visible = False

        player.health = player.health
        player.movement_speed = 9
        player.is_player_image = True
        player.last_moved = "down_still"

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

            if player_condition.colliderect(save_icon_rect):
                save_game(player_condition.centerx,  player_condition.centery, monster2.monster_rect.x, monster2.monster_rect.y, monster3.monster_rect.x, monster3.monster_rect.y, player.health, monster2.monster_health, monster3.monster_health, pistol_taken)
                save_icon_visible = False
                save_icon_rect.topleft = (-500, -500)

            # player.player_rect.x, player.player_rect.y = player.player_rect_pistol.x, player.player_rect_pistol.y
            if player.player_rect.colliderect(pistol_icon_rect):
                if player_condition == player.player_rect:
                    player_condition = player.player_rect_pistol
                    player.player_rect_pistol.x, player.player_rect_pistol.y = player.player_rect.x, player.player_rect.y
                    pistol_icon_rect.topleft = (-500, -500)
                    pistol_icon_visible = False
                    pistol_taken = True
                else:
                    player_condition = player.player_rect
                    pistol_icon_visible = True

            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                print(monster2.monster_rect.topleft, monster3.monster_rect.topleft)
        
        monsters = [monster2, monster3]  

        for monster in monsters:
            if monster.monster_health > 0:
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


        boundries_lvl_2(player_condition)

        collision_with_static_object(player_condition, block_rect, 10)

        for monster in monsters:
            boundries(monster.monster_rect)

        for monster in monsters:
         collision_with_moving_object(player_condition, monster.monster_rect, 10, player.movement_speed, monster.movement_speed,  screen_rect)
        
        pg.draw.rect(screen, (0, 0, 0, 0), block_rect)
        pg.draw.rect(screen, (0, 0, 0, 0), pass_mark_rect)
        screen.blit(background_lvl_2, (0,0))
        
        if save_icon_visible:
            screen.blit(save_icon, save_icon_rect.topleft)
       
        if pistol_icon_visible:
            screen.blit(pistol_icon, pistol_icon_rect.topleft)

        if player.health == 0:
            player.draw_player_death_animation()
            main_song.stop()
            death_screen(screen)
            

        for monster in monsters:
            if monster.monster_health == 0:
                monster.should_follow_player = False
                monster.patrol_mode = False
                monster.monster_is_attacking = False
                monster.draw_monster_death_animation()
  
        for monster in monsters:
            monster.draw_monster(screen)

        if player_condition == player.player_rect_pistol:
            player.draw_pistol_player(screen)
        else:
            player.draw(screen)

        for monster in monsters:
            if player_condition.colliderect(pass_mark_rect) and monster.monster_health == 0:
                main_song.stop()
                from main_play_final import main_game_lvl_final
                main_game_lvl_final(game_state)    

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
    main_game_lvl_2(game_state)