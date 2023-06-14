import pygame as pg

#test player
class Player:
    def __init__(self, player_image_path_1, player_image_path_2, position ): 
        self.player_image_1_raw = pg.image.load(player_image_path_1).convert_alpha()
        self.player_image_2_raw = pg.image.load(player_image_path_2).convert_alpha()
        self.player_image_1 = pg.transform.scale(self.player_image_1_raw, (100, 100))
        self.player_image_2 = pg.transform.scale(self.player_image_2_raw, (100, 100))
        self.player_rect = self.player_image_1.get_rect()
        self.player_rect.topleft = position #sets initial position
        self.is_player_image1 = True
        self.animation_timer = 0
        self.animation_delay = 200000
        self.movement_speed = 5


    #this part is responsible for switching between two images
    def draw(self, screen):    
        # sprite_surface.fill((0, 0, 0))
        if self.is_player_image1:
            screen.blit(self.player_image_1, self.player_rect)
        else:
            screen.blit(self.player_image_2, self.player_rect)

    #responsible for player movement
    def main_player_movement(self):
        key = pg.key.get_pressed()
        if key[pg.K_a] == True:
            self.player_rect.move_ip(-self.movement_speed, 0)
            self.is_player_image1 = not self.is_player_image1 
        if key[pg.K_d] == True:
            self.player_rect.move_ip(self.movement_speed, 0)
            self.is_player_image1 = not self.is_player_image1
        if key[pg.K_w] == True:
            self.player_rect.move_ip(0, -self.movement_speed)
            self.is_player_image1 = not self.is_player_image1
        if key[pg.K_s] == True:
            self.player_rect.move_ip(0, self.movement_speed)
            self.is_player_image1 = not self.is_player_image1

        
        
    def animate(self):
        self.animation_timer += pg.time.get_ticks() # gets elapsed time
        if self.animation_timer >= self.animation_delay:
            self.is_player_image1 = not self.is_player_image1 #toggles between sprites
            self.animation_timer = 0 #resets timer


player_image_path_1 = 'Images/Player_sprites/player_down_1.png'
player_image_path_2 = 'Images/Player_sprites/player_down_2.png'

player = Player(player_image_path_1, player_image_path_2, (50, 50))

