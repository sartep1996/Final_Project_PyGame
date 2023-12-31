import pygame as pg
import time

#test player
class Player(pg.sprite.Sprite):
    def __init__(self, player_image_path_1, player_image_path_2, player_image_path_raw, player_image_up_path_1, player_image_up_path_2, player_image_path_raw_up, player_image_left_path_1, player_image_left_path_2, player_image_path_raw_left, player_image_right_path_1, player_image_right_path_2, player_image_path_raw_right, player_image_path_raw_upleft, player_image_upleft_path_1, player_image_upleft_path_2, player_image_path_raw_downleft, player_image_downleft_path_1, player_image_downleft_path_2, player_image_path_raw_upright, player_image_upright_path_1, player_image_upright_path_2, player_image_path_raw_downright, player_image_downright_path_1, player_image_downright_path_2, player_image_death_path_1, player_image_death_path_2, player_image_death_path_final, position, player_image_path_raw_p, player_image_path_1_p, player_image_path_2_p, player_image_path_raw_up_p, player_image_up_path_1_p, player_image_up_path_2_p, player_image_path_raw_lef_p, player_image_left_path_1_p, player_image_left_path_2_p, player_image_path_raw_right_p, player_image_right_path_1_p, player_image_right_path_2_p, player_image_path_raw_upleft_p, player_image_upleft_path_1_p, player_image_upleft_path_2_p, player_image_path_raw_downleft_p, player_image_downleft_path_1_p, player_image_downleft_path_2_p, player_image_path_raw_upright_p, player_image_upright_path_1_p, player_image_upright_path_2_p, player_image_path_raw_downright_p, player_image_downright_path_1_p, player_image_downright_path_2_p):
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


        #This is forplayer moving downright

        self.player_image_downright_still_raw = pg.image.load(player_image_path_raw_downright).convert_alpha()
        self.player_image_downright_1_raw = pg.image.load(player_image_downright_path_1).convert_alpha()
        self.player_image_downright_2_raw = pg.image.load(player_image_downright_path_2).convert_alpha()
        
        self.player_image_downright_still = pg.transform.scale(self.player_image_downright_still_raw, (100, 100))
        self.player_image_downright_1 = pg.transform.scale(self.player_image_downright_1_raw, (100, 100))
        self.player_image_downright_2 = pg.transform.scale(self.player_image_downright_2_raw, (100, 100))


        #This is forplayer moving downleft

        self.player_image_downleft_still_raw = pg.image.load(player_image_path_raw_downleft).convert_alpha()
        self.player_image_downleft_1_raw = pg.image.load(player_image_downleft_path_1).convert_alpha()
        self.player_image_downleft_2_raw = pg.image.load(player_image_downleft_path_2).convert_alpha()
        
        self.player_image_downleft_still = pg.transform.scale(self.player_image_downleft_still_raw, (100, 100))
        self.player_image_downleft_1 = pg.transform.scale(self.player_image_downleft_1_raw, (100, 100))
        self.player_image_downleft_2 = pg.transform.scale(self.player_image_downleft_2_raw, (100, 100))

        
        #This is forplayer moving upleft

        self.player_image_upleft_still_raw = pg.image.load(player_image_path_raw_upleft).convert_alpha()
        self.player_image_upleft_1_raw = pg.image.load(player_image_upleft_path_1).convert_alpha()
        self.player_image_upleft_2_raw = pg.image.load(player_image_upleft_path_2).convert_alpha()
        
        self.player_image_upleft_still = pg.transform.scale(self.player_image_upleft_still_raw, (100, 100))
        self.player_image_upleft_1 = pg.transform.scale(self.player_image_upleft_1_raw, (100, 100))
        self.player_image_upleft_2 = pg.transform.scale(self.player_image_upleft_2_raw, (100, 100))


         #This is for player moving upright

        self.player_image_upright_still_raw = pg.image.load(player_image_path_raw_upright).convert_alpha()
        self.player_image_upright_1_raw = pg.image.load(player_image_upright_path_1).convert_alpha()
        self.player_image_upright_2_raw = pg.image.load(player_image_upright_path_2).convert_alpha()
        
        self.player_image_upright_still = pg.transform.scale(self.player_image_upright_still_raw, (100, 100))
        self.player_image_upright_1 = pg.transform.scale(self.player_image_upright_1_raw, (100, 100))
        self.player_image_upright_2 = pg.transform.scale(self.player_image_upright_2_raw, (100, 100))


        #This when player dies
        self.player_image_death_1_raw = pg.image.load(player_image_death_path_1).convert_alpha()
        self.player_image_death_2_raw = pg.image.load(player_image_death_path_2).convert_alpha()
        self.player_image_death_final_raw = pg.image.load(player_image_death_path_final).convert_alpha()
        
        self.player_image_death_1 = pg.transform.scale(self.player_image_death_1_raw , (100, 100))
        self.player_image_death_2 = pg.transform.scale(self.player_image_death_2_raw, (100, 100))
        self.player_image_death_final= pg.transform.scale(self.player_image_death_final_raw, (100, 100))

        # The rest of the charackteristics
        self.player_rect = self.player_image_still.get_rect()
        self.player_rect.topleft = position #sets initial position
        self.is_player_image = True
        self.animation_timer = 0
        self.animation_delay = 350
        self.movement_speed = 9
        self.last_moved = ''
        self.last_frame_time = time.time()
        self.last_image = False
        self.frame_index = 0

        self.max_health = 100
        self.health = self.max_health

        
    
    def set_position(self, x, y):
        self.player_rect.topleft = (x, y)


    def player_update(self, screen):
        
        self.allow_movement = True
        self.main_player_movement()
        self.animate()
        self.draw(screen)


    def draw(self, screen):

        if self.last_moved == 'down':
            if self.is_player_image:
                screen.blit(self.player_image_still, self.player_rect)
            elif self.animation_timer >= self.animation_delay // 2:
                screen.blit(self.player_image_2, self.player_rect)
            else:
                screen.blit(self.player_image_1, self.player_rect)

        elif self.last_moved == 'downright':
            if self.is_player_image:
                screen.blit(self.player_image_downright_still, self.player_rect)
            elif self.animation_timer >= self.animation_delay // 2:
                screen.blit(self.player_image_downright_1, self.player_rect)
            else:
                screen.blit(self.player_image_downright_2, self.player_rect)

        
        elif self.last_moved == 'up':
            if self.is_player_image:
                screen.blit(self.player_image_up_still, self.player_rect)
            elif self.animation_timer >= self.animation_delay // 2:
                screen.blit(self.player_image_up_2, self.player_rect)
            else:
                screen.blit(self.player_image_up_1, self.player_rect)

        
        elif self.last_moved == 'upleft':
            if self.is_player_image:
                screen.blit(self.player_image_upright_still, self.player_rect)
            elif self.animation_timer >= self.animation_delay // 2:
                screen.blit(self.player_image_upright_1, self.player_rect)
            else:
                screen.blit(self.player_image_upright_2, self.player_rect)

        elif self.last_moved == 'left':
            if self.is_player_image:
                screen.blit(self.player_image_left_still, self.player_rect)
            elif self.animation_timer >= self.animation_delay // 2:
                screen.blit(self.player_image_left_2, self.player_rect)
            else:
                screen.blit(self.player_image_left_1, self.player_rect)

        elif self.last_moved == 'upright':
            if self.is_player_image:
                screen.blit(self.player_image_upleft_still, self.player_rect)
            elif self.animation_timer >= self.animation_delay // 2:
                screen.blit(self.player_image_upleft_1, self.player_rect)
            else:
                screen.blit(self.player_image_upleft_2, self.player_rect)

        elif self.last_moved == 'right':
            if self.is_player_image:
                screen.blit(self.player_image_right_still, self.player_rect)
            elif self.animation_timer >= self.animation_delay // 2:
                screen.blit(self.player_image_right_2, self.player_rect)
            else:
                screen.blit(self.player_image_right_1, self.player_rect)

        elif self.last_moved == 'downleft':
            if self.is_player_image:
                screen.blit(self.player_image_downleft_still, self.player_rect)
            elif self.animation_timer >= self.animation_delay // 2:
                screen.blit(self.player_image_downleft_1, self.player_rect)
            else:
                screen.blit(self.player_image_downleft_2, self.player_rect)

        elif self.is_player_image:
                screen.blit(self.player_image_still, self.player_rect)


        elif self.last_moved == self.player_image_death_1:
            screen.blit(self.player_image_death_1, self.player_rect)
        
        elif self.last_moved == self.player_image_death_2:
            screen.blit(self.player_image_death_2, self.player_rect)

        elif self.last_moved == self.player_image_death_final:
            screen.blit(self.player_image_death_final, self.player_rect)


    def main_player_movement(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            if key[pg.K_w]:
                diagonal_speed = self.movement_speed / 1.414
                self.player_rect.move_ip(-diagonal_speed, -diagonal_speed)
                self.is_player_image = False
                self.last_moved= 'upleft'
            
            elif key[pg.K_s]:
                diagonal_speed = self.movement_speed / 1.414
                self.player_rect.move_ip(-diagonal_speed, diagonal_speed)
                self.is_player_image = False
                self.last_moved= 'downleft'
            else:
                self.player_rect.move_ip(-self.movement_speed, 0)
                self.is_player_image = False
                self.last_moved = 'left'
       
        elif key[pg.K_d]:
            if key[pg.K_w]:
                diagonal_speed = self.movement_speed / 1.414
                self.player_rect.move_ip(diagonal_speed, -diagonal_speed)
                self.is_player_image = False
                self.last_moved = 'upright'
            elif key[pg.K_s]:
                diagonal_speed = self.movement_speed / 1.414
                self.player_rect.move_ip(diagonal_speed, diagonal_speed)
                self.is_player_image = False
                self.last_moved = 'downright'
            else:
                self.player_rect.move_ip(self.movement_speed, 0)
                self.is_player_image = False
                self.last_moved = 'right'
       
        elif key[pg.K_w]:
            self.player_rect.move_ip(0, -self.movement_speed)
            self.is_player_image = False
            self.last_moved = 'up'
        elif key[pg.K_s]:
            self.player_rect.move_ip(0, self.movement_speed)
            self.is_player_image = False
            self.last_moved = 'down'
    
        else:
            self.is_player_image = True
            
        
     #responsible for animating charackter movement   
    def animate(self):
        current_time = time.time()
        delta_time = current_time - self.last_frame_time
        self.last_frame_time = current_time

        if not self.is_player_image and self.last_moved:
            self.animation_timer += delta_time * 700
            if self.animation_timer >= self.animation_delay:
                self.animation_timer = 0
                self.is_player_image = True


    def draw_health_bar(self, screen, x, y):        

        bar_width = 100
        bar_height = 10
        fill_color = (0, 255, 0)
        outline_color = (255, 255, 255)
        draining_health_fill = (255, 0, 0)
        if self.health <0: self.health = 0
        ratio = self.health  / self.max_health 

        outline_rect = pg.Rect(x - 3, y - 3 , bar_width + 6, bar_height + 6)
        pg.draw.rect(screen, outline_color, outline_rect )

        health_bar_rect = pg.Rect(x, y, bar_width, bar_height)
        pg.draw.rect(screen, draining_health_fill, health_bar_rect)
       
        fill_width = bar_width * ratio
        fill_rect = pg.Rect(x, y, fill_width, bar_height)
        pg.draw.rect(screen, fill_color, fill_rect)


    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0

        return self.health

    
    def draw_player_death_animation(self):
        self.is_player_image = False
        death_duration = 400
        animation_time = pg.time.get_ticks() % (3 * death_duration)

        if self.last_image:
            self.movement_speed = 0
            self.last_moved = self.player_image_death_final

        else:
            self.frame_index = animation_time // death_duration
            self.movement_speed = 0
            if self.frame_index == 0:
                self.last_moved = self.player_image_death_1
                self.movement_speed = 0
            elif self.frame_index == 1:
                self.last_moved = self.player_image_death_2
                self.last_image = True
            
    def reset(self, x, y):
        self.set_position( x, y)
        self.player_rect.topleft = (x, y)
        self.health = 100
    
# UNARMED
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

player_image_path_raw_upleft= 'Images/Player_sprites/player_upleft_still.png'
player_image_upleft_path_1 = 'Images/Player_sprites/player_upleft_1.png'
player_image_upleft_path_2 = 'Images/Player_sprites/player_upleft_2.png'

player_image_path_raw_downleft= 'Images/Player_sprites/player_downleft_still.png'
player_image_downleft_path_1 = 'Images/Player_sprites/player_downleft_1.png'
player_image_downleft_path_2 = 'Images/Player_sprites/player_downleft_2.png'

player_image_path_raw_upright= 'Images/Player_sprites/player_upright_still.png'
player_image_upright_path_1 = 'Images/Player_sprites/player_upright_1.png'
player_image_upright_path_2 = 'Images/Player_sprites/player_upright_2.png'

player_image_path_raw_downright= 'Images/Player_sprites/player_downright_still.png'
player_image_downright_path_1 = 'Images/Player_sprites/player_downright_1.png'
player_image_downright_path_2 = 'Images/Player_sprites/player_downright_2.png'

player_image_death_path_1 = 'Images/Player_sprites/player_death_1.png'
player_image_death_path_2 = 'Images/Player_sprites/player_death_2.png'
player_image_death_path_final = 'Images/Player_sprites/player_death_final.png'
# UNARMED


# ARMED
player_image_path_raw_p = 'Images/Player_sprites_pistol/player_down_still_p.png'
player_image_path_1_p = 'Images/Player_sprites_pistol/player_down_1_p.png'
player_image_path_2_p = 'Images/Player_sprites_pistol/player_down_2_p.png'

player_image_path_raw_up_p = 'Images/Player_sprites_pistol/player_up_still_p.png'
player_image_up_path_1_p = 'Images/Player_sprites_pistol/player_up_1_p.png'
player_image_up_path_2_p = 'Images/Player_sprites_pistol/player_up_2_p.png'

player_image_path_raw_lef_p= 'Images/Player_sprites_pistol/player_left_still_p.png'
player_image_left_path_1_p = 'Images/Player_sprites_pistol/player_left_1_p.png'
player_image_left_path_2_p = 'Images/Player_sprites_pistol/player_left_2_p.png'

player_image_path_raw_right_p = 'Images/Player_sprites_pistol/player_right_still_p.png'
player_image_right_path_1_p = 'Images/Player_sprites_pistol/player_right_1_p.png'
player_image_right_path_2_p = 'Images/Player_sprites_pistol/player_right_2_p.png'

player_image_path_raw_upleft_p = 'Images/Player_sprites_pistol/player_upleft_still_p.png'
player_image_upleft_path_1_p = 'Images/Player_sprites_pistol/player_upleft_1_p.png'
player_image_upleft_path_2_p = 'Images/Player_sprites_pistol/player_upleft_2_p.png'

player_image_path_raw_downleft_p = 'Images/Player_sprites_pistol/player_downleft_still_p.png'
player_image_downleft_path_1_p = 'Images/Player_sprites_pistol/player_downleft_1_p.png'
player_image_downleft_path_2_p = 'Images/Player_sprites_pistol/player_downleft_2_p.png'

player_image_path_raw_upright_p = 'Images/Player_sprites_pistol/player_upright_still_p.png'
player_image_upright_path_1_p = 'Images/Player_sprites_pistol/player_upright_1_p.png'
player_image_upright_path_2_p = 'Images/Player_sprites_pistol/player_upright_2_p.png'

player_image_path_raw_downright_p= 'Images/Player_sprites/player_downright_still_p.png'
player_image_downright_path_1_p = 'Images/Player_sprites/player_downright_1_p.png'
player_image_downright_path_2_p = 'Images/Player_sprites/player_downright_2_p.png'
# ARMED

player = Player(player_image_path_1, player_image_path_2, player_image_path_raw, player_image_up_path_1, player_image_up_path_2, player_image_path_raw_up, player_image_left_path_1, player_image_left_path_2, player_image_path_raw_left, player_image_right_path_1, player_image_right_path_2, player_image_path_raw_right, player_image_path_raw_upleft, player_image_upleft_path_1, player_image_upleft_path_2, player_image_path_raw_downleft, player_image_downleft_path_1, player_image_downleft_path_2, player_image_path_raw_upright, player_image_upright_path_1, player_image_upright_path_2, player_image_path_raw_downright, player_image_downright_path_1, player_image_downright_path_2,player_image_death_path_1, player_image_death_path_2, player_image_death_path_final,  (50, 50), player_image_path_raw_p, player_image_path_1_p, player_image_path_2_p, player_image_path_raw_up_p, player_image_up_path_1_p, player_image_up_path_2_p, player_image_path_raw_lef_p, player_image_left_path_1_p, player_image_left_path_2_p, player_image_path_raw_right_p, player_image_right_path_1_p, player_image_right_path_2_p, player_image_path_raw_upleft_p, player_image_upleft_path_1_p, player_image_upleft_path_2_p, player_image_path_raw_downleft_p, player_image_downleft_path_1_p, player_image_downleft_path_2_p, player_image_path_raw_upright_p, player_image_upright_path_1_p, player_image_upright_path_2_p, player_image_path_raw_downright_p, player_image_downright_path_1_p, player_image_downright_path_2_p )