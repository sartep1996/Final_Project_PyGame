import pygame as pg
import time
from boundries import BOUNDRY_RIGHT, BOUNDRY_LEFT, BOUNDRY_BOTTOM, BOUNDRY_TOP
import math



class Monster1(pg.sprite.Sprite):
    def __init__(self, x, y, speed, monster_image_down_path_1, monster_image_down_path_2, monster_image_path_raw_down, monster_image_up_path_1, monster_image_up_path_2, monster_image_path_raw_up, monster_image_left_path_1, monster_image_left_path_2, monster_image_path_raw_left, monster_image_right_path_1, monster_image_right_path_2, monster_image_path_raw_right, position ):
        super().__init__()
        self.monster_image_still = pg.transform.scale(pg.image.load(monster_image_path_raw_down).convert_alpha(), (100, 100))

        # This is for the player when he is moving down / and any other direction for now

        self.monster_image_down_still = pg.transform.scale(pg.image.load(monster_image_path_raw_down).convert_alpha(), (100, 100))
        self.monster_image_down_1 = pg.transform.scale(pg.image.load(monster_image_down_path_1).convert_alpha(), (100, 100))
        self.monster_image_down_2 = pg.transform.scale(pg.image.load(monster_image_down_path_2).convert_alpha(), (100, 100))
        
        # This is for player when he is moving up
        self.monster_image_up_still = pg.transform.scale(pg.image.load(monster_image_path_raw_up).convert_alpha(), (100, 100))
        self.monster_image_up_1 = pg.transform.scale(pg.image.load(monster_image_up_path_1).convert_alpha(), (100, 100))
        self.monster_image_up_2 = pg.transform.scale(pg.image.load(monster_image_up_path_2).convert_alpha(), (100, 100))

        # This is for player when he is moving left
        self.monster_image_left_still = pg.transform.scale(pg.image.load(monster_image_path_raw_left).convert_alpha(), (100, 100))
        self.monster_image_left_1 = pg.transform.scale(pg.image.load(monster_image_left_path_1).convert_alpha(), (100, 100))
        self.monster_image_left_2 = pg.transform.scale(pg.image.load(monster_image_left_path_2).convert_alpha(), (100, 100))
        
        #This is for player moving right
       
        self.monster_image_right_still = pg.transform.scale(pg.image.load(monster_image_path_raw_right).convert_alpha(), (100, 100))
        self.monster_image_right_1 = pg.transform.scale(pg.image.load(monster_image_right_path_1).convert_alpha(), (100, 100))
        self.monster_image_right_2 = pg.transform.scale(pg.image.load(monster_image_right_path_2).convert_alpha(), (100, 100))
        
        # The rest of the charackteristics
        self.monster_rect = self.monster_image_still.get_rect()
        self.monster_rect.topleft = position #sets initial position
        self.is_monster_image = True
        self.animation_timer = 0
        self.animation_delay = 350
        self.movement_speed = 4
        self.last_moved = ''
        self.last_frame_time = time.time()
        self.should_follow_player = False
        self.patrol_mode = True
        self.check_collision = True


        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1
        self.direction_y = 0

    def set_position(self, x, y):
        self.monster_rect.topleft = (x, y)


    def monster_update(self, player_rect):
        self.x += self.speed * self.direction
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

        self.monster_collides_with(player_rect)
    
        # else:
        #     if player_rect.left > self.monster_rect.right:
        #         self.direction = 1
        #         self.last_moved = BOUNDRY_RIGHT
        #     elif player_rect.right < self.monster_rect.left:
        #         self.direction = -1
        #         self.last_moved = BOUNDRY_LEFT
        #     else:
        #         self.direction = 0
        #         # Determine the appropriate still image based on player's vertical position
        #         if player_rect.top < self.monster_rect.top:
        #             self.last_moved = self.monster_image_up_still
        #         elif player_rect.bottom > self.monster_rect.bottom:
        #             self.last_moved = self.monster_image_down_still
            
        #     self.x += self.speed * self.direction
        #     self.monster_rect.x = self.x
        #     self.y += self.speed * self.direction
        #     self.monster_rect.y = self.y

        
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

        else:
            screen.blit(self.monster_image_down_still, self.monster_rect)

    def monster_collides_with(self, player_rect):
        if self.monster_rect.colliderect(player_rect):
            self.should_follow_player = True
            
            player_center = player_rect.center
            monster_center = self.monster_rect.center

            dx = player_center[0] - monster_center[0]
            dy = player_center[1] - monster_center[1]

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

            self.monster_follow_player(player_rect)
            # self.should_follow_player = True
            
            


    # def monster_follow_player(self, player_rect):
    #     player_center = player_rect.center
    #     monster_center = self.monster_rect.center

    #     dx = player_center[0] - monster_center[0]
    #     dy = player_center[1] - monster_center[1]

    #     if abs(dx) > abs(dy):
    #         if dx > 0:
    #             self.direction = 1
    #             dx = min(dx, self.movement_speed)
    #         else:
    #             self.direction = 2
    #             dx = max(dx, -self.movement_speed)
    #         dy = 0
            
    #     else:
    #         if dy > 0:
    #             self.direction_y = 1
    #             dx = min(dx, self.movement_speed)
    #         else:
    #             self.direction_y = -1
    #             dx = max(dx, self.movement_speed)
    #         dx = 0

    #     self.x += self.speed + self.direction
    #     self.monster_rect.x = self.x

    def monster_follow_player(self, player_rect):
        dx = player_rect.centerx - self.monster_rect.centerx
        dy = player_rect.centery - self.monster_rect.centery
        distance = math.hypot (dx, dy)

        if distance != 0:
            direction_x = dx / distance
            direction_y = dy / distance
        else:
            direction_x = 0
            direction_y = 0

        if  self.should_follow_player:
            new_x = self.monster_rect.x + direction_x * self.speed
            new_y = self.monster_rect.y + direction_y * self.speed

            new_rect = pg.Rect(new_x, new_y, self.monster_rect.width, self.monster_rect.height)
            if not new_rect.colliderect(player_rect):
                self.monster_rect.x = new_x
                self.monster_rect.y = new_y
       
        


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

monster_image_path_raw_down = 'Images/Monster_1_sprites/monster_down_still.png'
monster_image_down_path_1 = 'Images/Monster_1_sprites/monster_down_1.png'
monster_image_down_path_2 = 'Images/Monster_1_sprites/monster_down_2.png'

monster_image_path_raw_up = 'Images/Monster_1_sprites/monster_up_still.png'
monster_image_up_path_1 = 'Images/Monster_1_sprites/monster_up_1.png'
monster_image_up_path_2 = 'Images/Monster_1_sprites/monster_up_2.png'

monster_image_path_raw_left= 'Images/Monster_1_sprites/monster_left_still.png'
monster_image_left_path_1 = 'Images/Monster_1_sprites/monster_left_1.png'
monster_image_left_path_2 = 'Images/Monster_1_sprites/monster_left_2.png'

monster_image_path_raw_right= 'Images/Monster_1_sprites/monster_right_still.png'
monster_image_right_path_1 = 'Images/Monster_1_sprites/monster_right_1.png'
monster_image_right_path_2 = 'Images/Monster_1_sprites/monster_right_2.png'

monster1 = Monster1(5, 5, 5, monster_image_down_path_1, monster_image_down_path_2, monster_image_path_raw_down, monster_image_up_path_1, monster_image_up_path_2, monster_image_path_raw_up, monster_image_left_path_1, monster_image_left_path_2, monster_image_path_raw_left, monster_image_right_path_1, monster_image_right_path_2, monster_image_path_raw_right, (50, 50))