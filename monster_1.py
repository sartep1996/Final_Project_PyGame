import pygame as pg
import time
from boundries import BOUNDRY_RIGHT, BOUNDRY_LEFT, BOUNDRY_BOTTOM, BOUNDRY_TOP



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
        self.movement_speed = 5
        self.last_moved = ''
        self.last_frame_time = time.time()


        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1


    def monster_update(self, playerrect):
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

        self.monster_collides_with(playerrect)

        
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


    def monster_collides_with(self, playerrect):
        if self.monster_rect.colliderect(playerrect):
            
            if self.direction == 1 and self.monster_rect.right > playerrect.left:
                self.direction = 0
                self.monster_rect.right = playerrect.left
                self.last_moved = self.monster_image_left_still
            
            elif self.direction == -1 and self.monster_rect.left < playerrect.right:
                self.direction = 0
                self.monster_rect.left = playerrect.right
                self.last_moved = self.monster_image_right_still

            elif self.direction == 1 and self.monster_rect.top > playerrect.bottom:
                self.direction = 0
                self.monster_rect.bottom = playerrect.top
                self.last_moved = self.monster_image_up_still

            elif self.direction == -1 and self.monster_rect.top < playerrect.bottom:
                self.direction = 0
                self.monster_rect.top = playerrect.bottom
                self.last_moved = self.monster_image_down_still

            
            

            # if self.monster_rect.bottom > playerrect.top and self.speed > 0:
            #     self.speed = 0
            #     self.monster_rect.bottom = playerrect.top 
            # elif self.monster_rect.top < playerrect.bottom and self.speed < 0:
            #     self.speed = 0
            #     self.monster_rect.top = playerrect.bottom

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