import pygame as pg
import time

# Image data for sprite loading

image_data = {
    'still': {
        'path': 'Images/Player_sprites/player_still.png',
        'size': (100, 100),
        'frames': 1
    },
    'down': {
        'path': 'Images/Player_sprites/player_down_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'up': {
        'path': 'Images/Player_sprites/player_up_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'up_still': {
        'path': 'Images/Player_sprites/player_up_still.png',
        'frames': 1,
        'size': (100, 100)
    },
    'left': {
        'path': 'Images/Player_sprites/player_left_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'left_still': {
        'path': 'Images/Player_sprites/player_left_still.png',
        'frames': 1,
        'size': (100, 100)
    },
    'right': {
        'path': 'Images/Player_sprites/player_right_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'right_still': {
        'path': 'Images/Player_sprites/player_right_still.png',
        'frames': 1,
        'size': (100, 100)
    },
    'downleft': {
        'path': 'Images/Player_sprites/player_downleft_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'downleft_still': {
        'path': 'Images/Player_sprites/player_downleft_still.png',
        'frames': 1,
        'size': (100, 100)
    },
    'upleft': {
        'path': 'Images/Player_sprites/player_upleft_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'upleft_still': {
        'path': 'Images/Player_sprites/player_upleft_still.png',
        'frames': 1,
        'size': (100, 100)
    },
    'downright': {
        'path': 'Images/Player_sprites/player_downright_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'downright_still': {
        'path': 'Images/Player_sprites/player_downright_still.png',
        'frames': 1,
        'size': (100, 100)
    },
    'upright': {
        'path': 'Images/Player_sprites/player_upright_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'upright_still': {
        'path': 'Images/Player_sprites/player_upright_still.png',
        'frames': 1,
        'size': (100, 100)
    },
    'death_1': {
        'path': 'Images/Player_sprites/player_death_1.png',
        'frames': 1,
        'size': (100, 100)
    },
    'death_2': {
        'path': 'Images/Player_sprites/player_death_2.png',
        'frames': 1,
        'size': (100, 100)
    },
    'death_final': {
        'path': 'Images/Player_sprites/player_death_final.png',
        'frames': 1,
        'size': (100, 100)
}}



# Helper function to load and scale the images
def load_and_scale_images(image_path, frames, size):
    images = []
    if frames == 1:
        image = pg.image.load(image_path).convert_alpha()
        image = pg.transform.scale(image, size)
        images.append(image)
    else:
        for i in range(1, frames + 1):
            image = pg.image.load(image_path.format(i)).convert_alpha()
            image = pg.transform.scale(image, size)
            images.append(image)
    return images

# Player class
class Player(pg.sprite.Sprite):
    def __init__(self, image_data, position):
        super().__init__()

        self.player_rect = pg.Rect(position, image_data['still']['size'])
        self.player_rect.topleft = position
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

        self.images = {}

        # Load and scale the images
        for key, data in image_data.items():
            if data['frames'] == 1:
                self.images[key] = load_and_scale_images(data['path'], 1, data['size'])[0]
            else:
                self.images[key] = load_and_scale_images(data['path'], data['frames'], data['size'])


        # Other draw logic...

    # Other methods...
    def set_position(self, x, y):
        self.player_rect.topleft = (x, y)

    def player_update(self, screen):
        
        self.allow_movement = True
        self.main_player_movement()
        self.animate()
        self.draw(screen)


    def draw(self, screen):
        if self.last_moved in self.images:
            image_list = self.images[self.last_moved]
            if isinstance(image_list, list):  # Check if image_list is a list
                image_index = int(self.animation_timer // (self.animation_delay / len(image_list))) % len(image_list)
                image = image_list[image_index]
            else:  # If image_list is a single image, use it directly
                image = image_list
            screen.blit(image, self.player_rect)
        else:
            screen.blit(self.images['still'], self.player_rect)




  #responsible for player movement
    def main_player_movement(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            if key[pg.K_w]:
                diagonal_speed = self.movement_speed / 1.414
                self.player_rect.move_ip(-diagonal_speed, -diagonal_speed)
                self.is_player_image = False
                self.last_moved = 'upleft'

            elif key[pg.K_s]:
                diagonal_speed = self.movement_speed / 1.414
                self.player_rect.move_ip(-diagonal_speed, diagonal_speed)
                self.is_player_image = False
                self.last_moved = 'downleft'
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
        # Player is not moving
            self.is_player_image = True
            if self.last_moved == 'left':
                self.last_moved = 'left_still'
            elif self.last_moved == 'right':
                self.last_moved = 'right_still'
            elif self.last_moved == 'up':
                self.last_moved = 'up_still'
            elif self.last_moved == 'down':
                self.last_moved = 'down_still'
            elif self.last_moved == 'upleft':
                self.last_moved = 'upleft_still'
            elif self.last_moved == 'upright':
                self.last_moved = 'upright_still'
            elif self.last_moved == 'downleft':
                self.last_moved = 'downleft_still'
            elif self.last_moved == 'downright':
                self.last_moved = 'downright_still'
            
        
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
            self.last_moved = "death_final"

        else:
            self.frame_index = animation_time // death_duration
            self.movement_speed = 0
            if self.frame_index == 0:
                self.last_moved = "death_1"
                self.movement_speed = 0
            elif self.frame_index == 1:
                self.last_moved = "death_2"
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


# # ARMED
# player_image_path_raw_p = 'Images/Player_sprites_pistol/player_down_still_p.png'
# player_image_path_1_p = 'Images/Player_sprites_pistol/player_down_1_p.png'
# player_image_path_2_p = 'Images/Player_sprites_pistol/player_down_2_p.png'

# player_image_path_raw_up_p = 'Images/Player_sprites_pistol/player_up_still_p.png'
# player_image_up_path_1_p = 'Images/Player_sprites_pistol/player_up_1_p.png'
# player_image_up_path_2_p = 'Images/Player_sprites_pistol/player_up_2_p.png'

# player_image_path_raw_lef_p= 'Images/Player_sprites_pistol/player_left_still_p.png'
# player_image_left_path_1_p = 'Images/Player_sprites_pistol/player_left_1_p.png'
# player_image_left_path_2_p = 'Images/Player_sprites_pistol/player_left_2_p.png'

# player_image_path_raw_right_p = 'Images/Player_sprites_pistol/player_right_still_p.png'
# player_image_right_path_1_p = 'Images/Player_sprites_pistol/player_right_1_p.png'
# player_image_right_path_2_p = 'Images/Player_sprites_pistol/player_right_2_p.png'

# player_image_path_raw_upleft_p = 'Images/Player_sprites_pistol/player_upleft_still_p.png'
# player_image_upleft_path_1_p = 'Images/Player_sprites_pistol/player_upleft_1_p.png'
# player_image_upleft_path_2_p = 'Images/Player_sprites_pistol/player_upleft_2_p.png'

# player_image_path_raw_downleft_p = 'Images/Player_sprites_pistol/player_downleft_still_p.png'
# player_image_downleft_path_1_p = 'Images/Player_sprites_pistol/player_downleft_1_p.png'
# player_image_downleft_path_2_p = 'Images/Player_sprites_pistol/player_downleft_2_p.png'

# player_image_path_raw_upright_p = 'Images/Player_sprites_pistol/player_upright_still_p.png'
# player_image_upright_path_1_p = 'Images/Player_sprites_pistol/player_upright_1_p.png'
# player_image_upright_path_2_p = 'Images/Player_sprites_pistol/player_upright_2_p.png'

# player_image_path_raw_downright_p= 'Images/Player_sprites/player_downright_still_p.png'
# player_image_downright_path_1_p = 'Images/Player_sprites/player_downright_1_p.png'
# player_image_downright_path_2_p = 'Images/Player_sprites/player_downright_2_p.png'

# ARMED










player = Player(image_data, (50, 50))
