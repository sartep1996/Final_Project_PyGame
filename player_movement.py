import pygame as pg
import time

#test player
class Player(pg.sprite.Sprite):
    def __init__(self, player_image_path_1, player_image_path_2, player_image_path_raw, player_image_up_path_1, player_image_up_path_2, player_image_path_raw_up, player_image_left_path_1, player_image_left_path_2, player_image_path_raw_left, player_image_right_path_1, player_image_right_path_2, player_image_path_raw_right, position ):
        super().__init__()
        self.player_still_raw = pg.image.load(player_image_path_raw).convert_alpha()

        # This is for the player when he is moving down / and any other direction for now
        self.player_image_still = pg.transform.scale(self.player_still_raw, (100, 100))
        self.player_image_1_raw = pg.image.load(player_image_path_1).convert_alpha()
        self.player_image_2_raw = pg.image.load(player_image_path_2).convert_alpha()
        self.player_image_1 = pg.transform.scale(self.player_image_1_raw, (100, 100))
        self.player_image_2 = pg.transform.scale(self.player_image_2_raw, (100, 100))

        # This is for player when he is moving up
        self.player_image_up_still_raw = pg.image.load(player_image_path_raw_up).convert_alpha()
        self.player_image_up_1_raw = pg.image.load(player_image_up_path_1).convert_alpha()
        self.player_image_up_2_raw = pg.image.load(player_image_up_path_2).convert_alpha()
        
        self.player_image_up_still = pg.transform.scale(self.player_image_up_still_raw, (100, 100))
        self.player_image_up_1 = pg.transform.scale(self.player_image_up_1_raw, (100, 100))
        self.player_image_up_2 = pg.transform.scale(self.player_image_up_2_raw, (100, 100))

        # This is for player when he is moving left
        self.player_image_left_still_raw = pg.image.load(player_image_path_raw_left).convert_alpha()
        self.player_image_left_1_raw = pg.image.load(player_image_left_path_1).convert_alpha()
        self.player_image_left_2_raw = pg.image.load(player_image_left_path_2).convert_alpha()
        
        self.player_image_left_still = pg.transform.scale(self.player_image_left_still_raw, (100, 100))
        self.player_image_left_1 = pg.transform.scale(self.player_image_left_1_raw, (100, 100))
        self.player_image_left_2 = pg.transform.scale(self.player_image_left_2_raw, (100, 100))

        #This is for player moving right

        self.player_image_right_still_raw = pg.image.load(player_image_path_raw_right).convert_alpha()
        self.player_image_right_1_raw = pg.image.load(player_image_right_path_1).convert_alpha()
        self.player_image_right_2_raw = pg.image.load(player_image_right_path_2).convert_alpha()
        
        self.player_image_right_still = pg.transform.scale(self.player_image_right_still_raw, (100, 100))
        self.player_image_right_1 = pg.transform.scale(self.player_image_right_1_raw, (100, 100))
        self.player_image_right_2 = pg.transform.scale(self.player_image_right_2_raw, (100, 100))







        self.player_rect = self.player_image_still.get_rect()
        self.player_rect.topleft = position #sets initial position
        self.is_player_image = True
        self.animation_timer = 0
        self.animation_delay = 200
        self.movement_speed = 5
        self.last_moved = ''
        self.last_frame_time = time.time()
    


  

    def draw(self, screen):

        if self.last_moved == 'down':
            if self.is_player_image:
                screen.blit(self.player_image_still, self.player_rect)
            elif self.animation_timer >= self.animation_delay // 2:
                screen.blit(self.player_image_2, self.player_rect)
            else:
                screen.blit(self.player_image_1, self.player_rect)
        
        elif self.last_moved == 'up':
            if self.is_player_image:
                screen.blit(self.player_image_up_still, self.player_rect)
            elif self.animation_timer >= self.animation_delay // 2:
                screen.blit(self.player_image_up_2, self.player_rect)
            else:
                screen.blit(self.player_image_up_1, self.player_rect)

        elif self.last_moved == 'left':
            if self.is_player_image:
                screen.blit(self.player_image_left_still, self.player_rect)
            elif self.animation_timer >= self.animation_delay // 2:
                screen.blit(self.player_image_left_2, self.player_rect)
            else:
                screen.blit(self.player_image_left_1, self.player_rect)

        elif self.last_moved == 'right':
            if self.is_player_image:
                screen.blit(self.player_image_right_still, self.player_rect)
            elif self.animation_timer >= self.animation_delay // 2:
                screen.blit(self.player_image_right_2, self.player_rect)
            else:
                screen.blit(self.player_image_right_1, self.player_rect)

        elif self.is_player_image:
                screen.blit(self.player_image_still, self.player_rect)





    #responsible for player movement
    def main_player_movement(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.player_rect.move_ip(-self.movement_speed, 0)
            self.is_player_image = False
            self.last_moved = 'left'
        else:
            self.is_player_image = True
        
        if key[pg.K_d]:
            self.player_rect.move_ip(self.movement_speed, 0)
            self.is_player_image = False
            self.last_moved = 'right'
        if key[pg.K_w]:
            self.player_rect.move_ip(0, -self.movement_speed)
            self.is_player_image = False
            self.last_moved = 'up'
        if key[pg.K_s]:
            self.player_rect.move_ip(0, self.movement_speed)
            self.is_player_image = False
            self.last_moved = 'down'
    
            
        
    def animate(self):
        current_time = time.time()
        delta_time = current_time - self.last_frame_time
        self.last_frame_time = current_time

        if not self.is_player_image and self.last_moved:
            self.animation_timer += delta_time * 700
            if self.animation_timer >= self.animation_delay:
                self.animation_timer = 0
                self.is_player_image = True
        # self.animation_timer += pg.time.get_ticks() # gets elapsed time
        # if self.animation_timer >= self.animation_delay:
        #     self.is_player_image = not self.is_player_image #toggles between sprites
        #     self.animation_timer = 0 #resets timer


player_image_path_raw = 'Images/Player_sprites/player_still.png'
player_image_path_1 = 'Images/Player_sprites/player_down_1.png'
player_image_path_2 = 'Images/Player_sprites/player_down_2.png'

player_image_path_raw_up = 'Images/Player_sprites/player_up_still.png'
player_image_up_path_1 = 'Images/Player_sprites/player_up_1.png'
player_image_up_path_2 = 'Images/Player_sprites/player_up_2.png'

player_image_path_raw_left= 'Images/Player_sprites/player_left_still.png'
player_image_left_path_1 = 'Images/Player_sprites/player_left_1.png'
player_image_left_path_2 = 'Images/Player_sprites/player_left_2.png'

player_image_path_raw_right= 'Images/Player_sprites/player_right_still.png'
player_image_right_path_1 = 'Images/Player_sprites/player_right_1.png'
player_image_right_path_2 = 'Images/Player_sprites/player_right_2.png'






player = Player(player_image_path_1, player_image_path_2, player_image_path_raw, player_image_up_path_1, player_image_up_path_2, player_image_path_raw_up, player_image_left_path_1, player_image_left_path_2, player_image_path_raw_left, player_image_right_path_1, player_image_right_path_2, player_image_path_raw_right, (50, 50))

