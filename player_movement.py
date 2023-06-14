import pygame as pg

#test player
class Player:
    def __init__(self, player_image_path_1, player_image_path_2, position ):
        self.player_still_raw = pg.image.load(player_image_path_raw).convert_alpha()
        self.player_image_still = pg.transform.scale(self.player_still_raw, (100, 100))
        self.player_image_1_raw = pg.image.load(player_image_path_1).convert_alpha()
        self.player_image_2_raw = pg.image.load(player_image_path_2).convert_alpha()
        self.player_image_1 = pg.transform.scale(self.player_image_1_raw, (100, 100))
        self.player_image_2 = pg.transform.scale(self.player_image_2_raw, (100, 100))
        self.player_rect = self.player_image_still.get_rect()
        self.player_rect.topleft = position #sets initial position
        self.is_player_image = True
        self.animation_timer = 0
        self.animation_delay = 200
        self.movement_speed = 5
        self.last_moved = ''


    #this part is responsible for switching between two images
    def draw(self, screen):    
        # sprite_surface.fill((0, 0, 0))
        if self.is_player_image:
            screen.blit(self.player_image_still, self.player_rect)
        elif self.animation_timer >= self.animation_delay // 2:
            screen.blit(self.player_image_2, self.player_rect)
        else:
            screen.blit(self.player_image_1, self.player_rect)


    #responsible for player movement
    def main_player_movement(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.player_rect.move_ip(-self.movement_speed, 0)
            self.is_player_image = False
            self.last_moved = 'left'
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
        if not self.is_player_image and self.last_moved:
            self.animation_timer += 1
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

player = Player(player_image_path_1, player_image_path_2, (50, 50))

