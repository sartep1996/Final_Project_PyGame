import pygame as pg
import time
from boundries import BOUNDRY_RIGHT, BOUNDRY_LEFT, BOUNDRY_BOTTOM, BOUNDRY_TOP

CLOSE_DISTANCE_THRESHOLD = 140

class Monster1(pg.sprite.Sprite):
    def __init__(self, x, y, speed, monster_image_down_path_1, monster_image_down_path_2, monster_image_path_raw_down, monster_image_up_path_1, monster_image_up_path_2, monster_image_path_raw_up, monster_image_left_path_1, monster_image_left_path_2, monster_image_path_raw_left, monster_image_right_path_1, monster_image_right_path_2, monster_image_path_raw_right, monster_image_down_path_attack, monster_image_up_path_attack, monster_image_left_path_attack, monster_image_right_path_attack, monster_image_death_path_1, monster_image_death_path_2, monster_image_death_path_final, position  ):
        super().__init__()
        self.monster_image_still = pg.transform.scale(pg.image.load(monster_image_path_raw_down).convert_alpha(), (100, 100))

        # This is for the player when he is moving down / and any other direction for now

        self.monster_image_down_still = pg.transform.scale(pg.image.load(monster_image_path_raw_down).convert_alpha(), (100, 100))
        self.monster_image_down_1 = pg.transform.scale(pg.image.load(monster_image_down_path_1).convert_alpha(), (100, 100))
        self.monster_image_down_2 = pg.transform.scale(pg.image.load(monster_image_down_path_2).convert_alpha(), (100, 100))
        self.monster_image_down_attack =  pg.transform.scale(pg.image.load(monster_image_down_path_attack).convert_alpha(), (100, 100))
        
        # This is for player when he is moving up
        self.monster_image_up_still = pg.transform.scale(pg.image.load(monster_image_path_raw_up).convert_alpha(), (100, 100))
        self.monster_image_up_1 = pg.transform.scale(pg.image.load(monster_image_up_path_1).convert_alpha(), (100, 100))
        self.monster_image_up_2 = pg.transform.scale(pg.image.load(monster_image_up_path_2).convert_alpha(), (100, 100))
        self.monster_image_up_attack =  pg.transform.scale(pg.image.load(monster_image_up_path_attack).convert_alpha(), (100, 100))


        # This is for player when he is moving left
        self.monster_image_left_still = pg.transform.scale(pg.image.load(monster_image_path_raw_left).convert_alpha(), (100, 100))
        self.monster_image_left_1 = pg.transform.scale(pg.image.load(monster_image_left_path_1).convert_alpha(), (100, 100))
        self.monster_image_left_2 = pg.transform.scale(pg.image.load(monster_image_left_path_2).convert_alpha(), (100, 100))
        self.monster_image_left_attack =  pg.transform.scale(pg.image.load(monster_image_left_path_attack).convert_alpha(), (100, 100))

        
        #This is for player moving right
       
        self.monster_image_right_still = pg.transform.scale(pg.image.load(monster_image_path_raw_right).convert_alpha(), (100, 100))
        self.monster_image_right_1 = pg.transform.scale(pg.image.load(monster_image_right_path_1).convert_alpha(), (100, 100))
        self.monster_image_right_2 = pg.transform.scale(pg.image.load(monster_image_right_path_2).convert_alpha(), (100, 100))
        self.monster_image_right_attack =  pg.transform.scale(pg.image.load(monster_image_right_path_attack).convert_alpha(), (100, 100))

        
        self.monster_image_death_1 = pg.transform.scale(pg.image.load(monster_image_death_path_1).convert_alpha(), (100, 100))
        self.monster_image_death_2 = pg.transform.scale(pg.image.load(monster_image_death_path_2).convert_alpha(), (100, 100))
        self.monster_image_death_final = pg.transform.scale(pg.image.load(monster_image_death_path_final).convert_alpha(), (100, 100))

        
        # The rest of the charackteristics
        self.monster_rect = self.monster_image_still.get_rect()
        self.monster_rect.topleft = position #sets initial position
        self.is_monster_image = True
        self.animation_timer = 0
        self.animation_delay = 150
        self.movement_speed = 2
        self.last_moved = ''
        self.last_frame_time = time.time()
        self.should_follow_player = False
        self.patrol_mode = True
        self.monster_is_attacking = False
        self.attack_damage = 0
        self.should_reset_patrol = False
        self.max_health = 100
        self.monster_health = self.max_health
        self.death_position = pg.Rect(*position, self.monster_rect.width, self.monster_rect.height)
                
        self.last_image = False
        self.frame_index = 0


        
        # self.check_collision = True


        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1
        self.direction_y = 0


    def reset_states(self):
        self.should_follow_player = False
        self.patrol_mode = True
        self.monster_is_attacking = False
        self.should_reset_patrol = False

    def set_position(self, x, y):
        self.monster_rect.topleft = (x, y)


    def monster_update(self, player_rect, screen):

        
        # self.should_reset_patrol = True
        
        # if self.should_reset_patrol:
        #     self.patrol_mode = True 
        
        self.monster_patrol_left_right()
        
        if self.should_follow_player:
            self.monster_follow_player(player_rect)
        self.monster_animate_when_following(player_rect)

        self.close_distance(player_rect)
        
        self.monster_collides_with(player_rect)
        
        self.monster_animate()
        
        if self.monster_is_attacking:
            self.monster_attack_player(player_rect, screen)
            self.monster_is_attacking = False
        
        self.monster_animate_when_following(player_rect)

        if self.monster_health == 0:
            self.draw_monster_death_animation()
            return
    '''
    def monster_update is main function that is responsible for updating monster, it has all the other functions, responsible for monster behaviour
    '''
    

    def monster_patrol_left_right(self):
        
        if self.patrol_mode:
            self.x += self.movement_speed * self.direction
            self.monster_rect.x = self.x 
        
        
    
        if self.direction == -1:
            self.last_moved = BOUNDRY_LEFT
        elif self.direction == 1:
            self.last_moved = BOUNDRY_RIGHT
        

        if self.monster_rect.right > BOUNDRY_RIGHT:
            self.x = BOUNDRY_RIGHT -self.monster_rect.width
            self.direction = -1
        elif self.monster_rect.left < BOUNDRY_LEFT:
            self.x = BOUNDRY_LEFT 
            self.direction = 1
        
    def draw_monster(self, screen):
        if self.last_moved == BOUNDRY_LEFT or self.last_moved == self.monster_image_right_still:
            if self.direction != 0 and not self.is_monster_image:
                if self.animation_timer < self.animation_delay / 2:
                    screen.blit(self.monster_image_left_1, self.monster_rect)
                else:
                    screen.blit(self.monster_image_left_2, self.monster_rect)
            else:
                screen.blit(self.monster_image_left_still, self.monster_rect)
        
        elif self.last_moved == BOUNDRY_RIGHT or self.last_moved == self.monster_image_left_still:
            if self.direction != 0 and not self.is_monster_image:
                if self.animation_timer < self.animation_delay / 2:
                    screen.blit(self.monster_image_right_1, self.monster_rect)
                else:
                    screen.blit(self.monster_image_right_2, self.monster_rect)
            else:
                screen.blit(self.monster_image_right_still, self.monster_rect)

        elif self.last_moved == BOUNDRY_TOP or self.last_moved == self.monster_image_up_still:
            if self.direction != 0 and not self.is_monster_image:
                if self.animation_timer < self.animation_delay / 2:
                    screen.blit(self.monster_image_up_1, self.monster_rect)
                else:
                    screen.blit(self.monster_image_up_2, self.monster_rect)
            else:
                screen.blit(self.monster_image_up_still, self.monster_rect)


        elif self.last_moved == BOUNDRY_BOTTOM or self.last_moved == self.monster_image_down_still:
            if self.direction != 0 and not self.is_monster_image:
                if self.animation_timer < self.animation_delay / 2:
                    screen.blit(self.monster_image_down_1, self.monster_rect)
                else:
                    screen.blit(self.monster_image_down_2, self.monster_rect)
            else:
                screen.blit(self.monster_image_down_still, self.monster_rect)

        elif self.last_moved == self.monster_image_left_attack:
            screen.blit(self.monster_image_left_attack, self.monster_rect)

        elif self.last_moved == self.monster_image_right_attack:
            screen.blit(self.monster_image_right_attack, self.monster_rect)

        elif self.last_moved == self.monster_image_up_attack:
            screen.blit(self.monster_image_up_attack, self.monster_rect)

        elif self.last_moved == self.monster_image_down_attack:
            screen.blit(self.monster_image_down_attack, self.monster_rect)

        
        if self.last_moved == self.monster_image_death_1:
            screen.blit(self.monster_image_death_1, self.monster_rect)
        
        elif self.last_moved == self.monster_image_death_2:
            screen.blit(self.monster_image_death_2, self.monster_rect)

        elif self.last_moved == self.monster_image_death_final:
            screen.blit(self.monster_image_death_final, self.monster_rect)



    def draw_health_bar(self, screen, x, y):        

        bar_width = 100
        bar_height = 10
        fill_color = (0, 255, 0)
        outline_color = (255, 255, 255)
        draining_health_fill = (255, 0, 0)
        if self.monster_health <0: self.monster_health = 0
        ratio = self.monster_health  / self.max_health 

        outline_rect = pg.Rect(x - 3, y - 3 , bar_width + 6, bar_height + 6)
        pg.draw.rect(screen, outline_color, outline_rect )

        health_bar_rect = pg.Rect(x, y, bar_width, bar_height)
        pg.draw.rect(screen, draining_health_fill, health_bar_rect)
       
        fill_width = bar_width * ratio
        fill_rect = pg.Rect(x, y, fill_width, bar_height)
        pg.draw.rect(screen, fill_color, fill_rect)


    def take_damage(self, amount):
        self.monster_health -= amount
        if self.monster_health <= 0:
            self.monster_health = 0

        return self.monster_health


    def monster_collides_with(self, player_rect):
        if self.monster_rect.colliderect(player_rect):
            self.should_follow_player = True
            self.patrol_mode = False

            dx = player_rect.center[0] - self.monster_rect.center[0]
            dy = player_rect.center[1] - self.monster_rect.center[1]

            if abs(dx) > abs(dy):
                if dx > 0:
                    self.direction = 0
                    self.last_moved = self.monster_image_left_still
                else:
                    self.direction = 0
                    self.last_moved = self.monster_image_right_still
            else:
                if dy > 0:
                    self.direction = 0
                    self.last_moved = self.monster_image_down_still
                else:
                    self.direction = 0
                    self.last_moved = self.monster_image_up_still
        



    def monster_follow_player(self, player_rect):
            LERP_FACTOR      = 0.05
            minimum_distance = 125
            maximum_distance = 150
            stop_distance = 70
            gap_factor = 5
            speed_factor = 0.25

            
            player_vector = pg.math.Vector2(player_rect.center)
            monster_vector = pg.math.Vector2(self.monster_rect.center)
            new_monster_vector = pg.math.Vector2(self.monster_rect.center)
        
            distance = monster_vector.distance_to(player_vector)
            direction_vector = player_vector - monster_vector
            
            if distance > minimum_distance:
                direction_vector /= distance
                min_step = max(0, distance - maximum_distance * gap_factor)
                max_step = max(stop_distance, distance - minimum_distance)
                step_distance = min_step + (max_step - min_step) * LERP_FACTOR
                step_distance *= speed_factor
                new_monster_vector = monster_vector + direction_vector * step_distance

        
                    
            self.monster_rect.center = (new_monster_vector.x, new_monster_vector.y)

            
            self.folowing_monster_sprites_update(player_rect, distance)


        



    def folowing_monster_sprites_update(self, player_rect, distance):
        dx = player_rect.center[0] - self.monster_rect.center[0]
        dy = player_rect.center[1] - self.monster_rect.center[1]

        if abs(dx) > abs(dy):
            if dx > 0:
                self.direction = 1
                self.last_moved = self.monster_image_left_still
            else:
                self.direction = -1
                self.last_moved = self.monster_image_right_still
        else:
            if dy > 0:
                self.direction = 1
                self.last_moved = self.monster_image_down_still
            else:
                self.direction = -1
                self.last_moved = self.monster_image_up_still

        player_vector = pg.math.Vector2(player_rect.center)
        monster_vector = pg.math.Vector2(self.monster_rect.center)
        player_distance = player_vector.distance_to(monster_vector)

        if player_distance < CLOSE_DISTANCE_THRESHOLD:
            self.monster_is_attacking = True
        else:
            self.monster_is_attacking = False

        
    def close_distance(self, player_rect):
        player_vector = pg.math.Vector2(player_rect.center)
        monster_vector = pg.math.Vector2(self.monster_rect.center)
        player_distance = player_vector.distance_to(monster_vector)

        if player_distance < CLOSE_DISTANCE_THRESHOLD:
            self.monster_is_attacking = True
            self.should_follow_player = True
        else:
            self.monster_is_attacking = False
        

    

    def monster_attack_player(self, player_rect, screen):
        attack_duration = 400
        player_vector = pg.math.Vector2(player_rect.center)
        monster_vector = pg.math.Vector2(self.monster_rect.center)
        player_distance = player_vector.distance_to(monster_vector)

        self.monster_is_attacking = True
        
        dx = player_rect.center[0] - self.monster_rect.center[0]
        dy = player_rect.center[1] - self.monster_rect.center[1]
        
        if player_distance < CLOSE_DISTANCE_THRESHOLD:
            if abs(dx) > abs(dy):
                if dx > 0:
                    self.direction = 0
                    time_since_attack = pg.time.get_ticks() % (2 * attack_duration)
                    if time_since_attack < attack_duration:
                        self.last_moved = self.monster_image_right_attack
                    else:
                        self.last_moved = self.monster_image_left_still
                else:
                    self.direction = 0
                    time_since_attack = pg.time.get_ticks() % (2 * attack_duration)
                    if time_since_attack < attack_duration:
                        self.last_moved = self.monster_image_left_attack
                    else:
                        self.last_moved = self.monster_image_right_still
            else:
                if dy > 0:
                    self.direction = 0
                    time_since_attack = pg.time.get_ticks() % (2 * attack_duration)
                    if time_since_attack < attack_duration:
                        self.last_moved = self.monster_image_down_attack
                    else:
                        self.last_moved = self.monster_image_down_still
                else:
                    self.direction = 0
                    time_since_attack = pg.time.get_ticks() % (2 * attack_duration)
                    if time_since_attack < attack_duration:
                        self.last_moved = self.monster_image_up_attack
                    else:
                        self.last_moved = self.monster_image_up_still
            
            self.attack_damage = 0
            return self.attack_damage 
         
                
        return 0


     #responsible for animating charackter movement   
    def monster_animate(self):
        current_time = time.time()
        delta_time = current_time - self.last_frame_time
        self.last_frame_time = current_time

        if self.direction != 0:
            self.animation_timer += delta_time * 700
            if self.animation_timer >= self.animation_delay:
                self.animation_timer = 0  # Reset the timer
                self.is_monster_image = not self.is_monster_image  # Toggle the image
        else:
            self.is_monster_image = True
            self.animation_timer = 0  # Reset the timer



    def monster_animate_when_following(self, player_rect):
        current_time = time.time()
        delta_time = current_time - self.last_frame_time
        self.last_frame_time = current_time

        if self.direction != 0:
            self.animation_timer += delta_time * 700
            if self.animation_timer >= self.animation_delay:
                self.animation_timer = 0  # Reset the timer
                self.is_monster_image = not self.is_monster_image  # Toggle the image
        else:
            self.is_monster_image = True
            self.animation_timer = 0  # Reset the timer

        player_vector = pg.math.Vector2(player_rect.center)
        monster_vector = pg.math.Vector2(self.monster_rect.center)
        player_distance = player_vector.distance_to(monster_vector)
        if player_distance < CLOSE_DISTANCE_THRESHOLD:
            self.is_monster_image = False


    def draw_monster_death_animation(self):
        self.monster_is_attacking = False
        self.patrol_mode = True
        self.is_monster_image = False
        self.should_follow_player = False
        death_duration = 400
        self.movement_speed = 0
        animation_time = pg.time.get_ticks() % (3 * death_duration)

        if self.last_image:
            self.movement_speed = 0
            self.last_moved = self.monster_image_death_final

        else:
            self.frame_index = animation_time // death_duration
            self.movement_speed = 0
            if self.frame_index == 0:
                self.last_moved = self.monster_image_death_1
                self.movement_speed = 0
            elif self.frame_index == 1:
                self.last_moved = self.monster_image_death_2
                self.last_image = True
        
        # self.monster_rect = self.death_position

    
    def reset(self, player_rect, screen, x, y):
        self.set_position(x, y)
        self.should_reset_patrol = True
        self.patrol_mode = True
        self.monster_update(player_rect, screen)



monster_image_path_raw_down = 'Images/Monster_1_sprites/monster_down_still.png'
monster_image_down_path_1 = 'Images/Monster_1_sprites/monster_down_1.png'
monster_image_down_path_2 = 'Images/Monster_1_sprites/monster_down_2.png'
monster_image_down_path_attack = 'Images/Monster_1_sprites/monster_down_attack.png'

monster_image_path_raw_up = 'Images/Monster_1_sprites/monster_up_still.png'
monster_image_up_path_1 = 'Images/Monster_1_sprites/monster_up_1.png'
monster_image_up_path_2 = 'Images/Monster_1_sprites/monster_up_2.png'
monster_image_up_path_attack = 'Images/Monster_1_sprites/monster_up_attack.png'

monster_image_path_raw_left= 'Images/Monster_1_sprites/monster_left_still.png'
monster_image_left_path_1 = 'Images/Monster_1_sprites/monster_left_1.png'
monster_image_left_path_2 = 'Images/Monster_1_sprites/monster_left_2.png'
monster_image_left_path_attack = 'Images/Monster_1_sprites/monster_left_attack.png'


monster_image_path_raw_right= 'Images/Monster_1_sprites/monster_right_still.png'
monster_image_right_path_1 = 'Images/Monster_1_sprites/monster_right_1.png'
monster_image_right_path_2 = 'Images/Monster_1_sprites/monster_right_2.png'
monster_image_right_path_attack = 'Images/Monster_1_sprites/monster_right_attack.png'


monster_image_death_path_1 = 'Images/Monster_1_sprites/monster_death_1.png'
monster_image_death_path_2 = 'Images/Monster_1_sprites/monster_death_2.png'
monster_image_death_path_final = 'Images/Monster_1_sprites/monster_death_final.png'


monster1 = Monster1(5, 5, 5, monster_image_down_path_1, monster_image_down_path_2, monster_image_path_raw_down, monster_image_up_path_1, monster_image_up_path_2, monster_image_path_raw_up, monster_image_left_path_1, monster_image_left_path_2, monster_image_path_raw_left, monster_image_right_path_1, monster_image_right_path_2, monster_image_path_raw_right, monster_image_down_path_attack, monster_image_up_path_attack, monster_image_left_path_attack, monster_image_right_path_attack, monster_image_death_path_1, monster_image_death_path_2, monster_image_death_path_final, (50, 50))