import pygame as pg
import time
import math
# Image data for sprite loading

SHOOTING_DISTANCE  = 500
pistol_shot_wav = pg.mixer.Sound('Sounds/Pistol_Shot.wav')
pistol_shot_wav.set_volume(0.5)
flash_timer = 0
flash_duration = 0.2



image_data = {
    'still': {
        'path': 'Images/Player_sprites/player_down_still.png',
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
    },
    'flash': {
        'path': 'Images/Flash/pistol_flash.png',
        'frames': 1,
        'size': (100, 100)

}}

pistol_image_data = {
    'still': {
        'path': 'Images/Player_sprites_pistol/pistol_player_down_stillp.png',
        'size': (100, 100),
        'frames': 1
    },
    'down': {
        'path': 'Images/Player_sprites_pistol/pistol_player_down_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'up': {
        'path': 'Images/Player_sprites_pistol/pistol_player_up_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'up_still': {
        'path': 'Images/Player_sprites_pistol/pistol_player_up_still.png',
        'frames': 1,
        'size': (100, 100)
    },
    'left': {
        'path': 'Images/Player_sprites_pistol/pistol_player_left_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'left_still': {
        'path': 'Images/Player_sprites_pistol/pistol_player_left_still.png',
        'frames': 1,
        'size': (100, 100)
    },
    'right': {
        'path': 'Images/Player_sprites_pistol/pistol_player_right_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'right_still': {
        'path': 'Images/Player_sprites_pistol/pistol_player_right_still.png',
        'frames': 1,
        'size': (100, 100)
    },
    'downleft': {
        'path': 'Images/Player_sprites_pistol/pistol_player_downleft_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'downleft_still': {
        'path': 'Images/Player_sprites_pistol/pistol_player_downleft_still.png',
        'frames': 1,
        'size': (100, 100)
    },
    'upleft': {
        'path': 'Images/Player_sprites_pistol/pistol_player_upleft_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'upleft_still': {
        'path': 'Images/Player_sprites_pistol/pistol_player_upleft_still.png',
        'frames': 1,
        'size': (100, 100)
    },
    'downright': {
        'path': 'Images/Player_sprites_pistol/pistol_player_downright_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'downright_still': {
        'path': 'Images/Player_sprites_pistol/pistol_player_downright_still.png',
        'frames': 1,
        'size': (100, 100)
    },
    'upright': {
        'path': 'Images/Player_sprites_pistol/pistol_player_upright_{}.png',
        'frames': 2,
        'size': (100, 100)
    },
    'upright_still': {
        'path': 'Images/Player_sprites_pistol/pistol_player_upright_still.png',
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
    },
    'flash': {
        'path': 'Images/Flash/pistol_flash.png',
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

# def load_and_scale_images(image_path, size):
#     image = pg.image.load(image_path).convert_alpha()
#     image = pg.transform.scale(image, size)
#     return [image]


# Player class
class Player(pg.sprite.Sprite):
    def __init__(self, image_data, position):
        super().__init__()


        self.player_rect = pg.Rect(position, image_data['still']['size'])
        self.player_rect.topleft = position
        self.player_rect_pistol = pg.Rect(position, pistol_image_data['still']['size'])
        self.player_rect_pistol.topleft = position
       
        self.flash_rect = pg.Rect(position, image_data['flash']['size'])
        self.flash_rect.topleft = position
        self.is_player_image = True
        self.animation_timer = 0
        self.animation_delay = 350
        self.movement_speed = 9
        self.last_moved = ''
        self.last_frame_time = time.time()
        self.last_image = False
        self.frame_index = 0
        self.max_health = 200
        self.health = self.max_health
        self.pistol_damage = 5 
        self.close_to_shoot = False

        self.images = {}
        self.pistol_images = {}

        for key, data in image_data.items():
            if data['frames'] == 1:
                self.images[key] = load_and_scale_images(data['path'], 1, data['size'])[0]
            else:
                self.images[key] = load_and_scale_images(data['path'], data['frames'], data['size'])

        for key, data in pistol_image_data.items():
            if data['frames'] == 1:
                self.pistol_images[key] = load_and_scale_images(data['path'], 1, data['size'])[0]
            else:
                self.pistol_images[key] = load_and_scale_images(data['path'], data['frames'], data['size'])

    def set_position_helper(self, playerrect, x, y):
        playerrect = (x, y)

    def set_position_pistol(self, x, y):
        self.set_position_helper(self.player_rect_pistol, x, y)

    def set_position(self, x, y):
        self.set_position_helper(self.player_rect, x, y)

    def player_update(self, screen):
        self.player_update_helper(self.main_player_movement, screen)

    def player_update_pistol(self, screen):
        self.player_update_helper(self.main_player_movement_pistol, screen)

    def player_update_helper(self, movement_function, screen):
        self.allow_movement = True
        movement_function()
        self.draw(screen)
        self.animate()

    def draw_helper(self, screen, image_data, rect):
        if self.last_moved in image_data:
            image_list = image_data[self.last_moved]
            if isinstance(image_list, list):  # Check if image_list is a list
                image_index = int(self.animation_timer // (self.animation_delay / len(image_list))) % len(image_list)
                image = image_list[image_index]
            else:  # If image_list is a single image, use it directly
                image = image_list
            screen.blit(image, rect)
        else:
            screen.blit(image_data['still'], rect)

    def draw(self, screen):
        self.draw_helper(screen, self.images, self.player_rect)

    def draw_pistol_player(self, screen):
        self.draw_helper(screen, self.pistol_images, self.player_rect_pistol)


    def draw_flash(self, screen, delta_time):
        global flash_duration, flash_timer

        if flash_timer > 0:
            self.flash_rect.center = self.player_rect_pistol.center
            screen.blit(self.pistol_images['flash'], self.player_rect_pistol)
            flash_timer -= delta_time/1000

        if flash_timer <= 0:
            flash_timer = flash_duration


    #responsible for player movement
    def handle_movement(self, rect):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            if key[pg.K_w]:
                diagonal_speed = self.movement_speed / 1.414
                rect.move_ip(-diagonal_speed, -diagonal_speed)
                self.is_player_image = False
                self.last_moved = 'upleft'
            elif key[pg.K_s]:
                diagonal_speed = self.movement_speed / 1.414
                rect.move_ip(-diagonal_speed, diagonal_speed)
                self.is_player_image = False
                self.last_moved = 'downleft'
            else:
                rect.move_ip(-self.movement_speed, 0)
                self.is_player_image = False
                self.last_moved = 'left'
        elif key[pg.K_d]:
            if key[pg.K_w]:
                diagonal_speed = self.movement_speed / 1.414
                rect.move_ip(diagonal_speed, -diagonal_speed)
                self.is_player_image = False
                self.last_moved = 'upright'
            elif key[pg.K_s]:
                diagonal_speed = self.movement_speed / 1.414
                rect.move_ip(diagonal_speed, diagonal_speed)
                self.is_player_image = False
                self.last_moved = 'downright'
            else:
                rect.move_ip(self.movement_speed, 0)
                self.is_player_image = False
                self.last_moved = 'right'
        elif key[pg.K_w]:
            rect.move_ip(0, -self.movement_speed)
            self.is_player_image = False
            self.last_moved = 'up'
        elif key[pg.K_s]:
            rect.move_ip(0, self.movement_speed)
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

    def main_player_movement(self):
        self.handle_movement(self.player_rect)

    def main_player_movement_pistol(self):
        self.handle_movement(self.player_rect_pistol)


    def main_player_movement_pistol(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            if key[pg.K_w]:
                diagonal_speed = self.movement_speed / 1.414
                self.player_rect_pistol.move_ip(-diagonal_speed, -diagonal_speed)
                self.is_player_image = False
                self.last_moved = 'upleft'

            elif key[pg.K_s]:
                diagonal_speed = self.movement_speed / 1.414
                self.player_rect_pistol.move_ip(-diagonal_speed, diagonal_speed)
                self.is_player_image = False
                self.last_moved = 'downleft'
            else:
                self.player_rect_pistol.move_ip(-self.movement_speed, 0)
                self.is_player_image = False
                self.last_moved = 'left'

        elif key[pg.K_d]:
            if key[pg.K_w]:
                diagonal_speed = self.movement_speed / 1.414
                self.player_rect_pistol.move_ip(diagonal_speed, -diagonal_speed)
                self.is_player_image = False
                self.last_moved = 'upright'
            elif key[pg.K_s]:
                diagonal_speed = self.movement_speed / 1.414
                self.player_rect_pistol.move_ip(diagonal_speed, diagonal_speed)
                self.is_player_image = False
                self.last_moved = 'downright'
            else:
                self.player_rect_pistol.move_ip(self.movement_speed, 0)
                self.is_player_image = False
                self.last_moved = 'right'
        elif key[pg.K_w]:
            self.player_rect_pistol.move_ip(0, -self.movement_speed)
            self.is_player_image = False
            self.last_moved = 'up'
        elif key[pg.K_s]:
            self.player_rect_pistol.move_ip(0, self.movement_speed)
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
            

    def is_facing_monster(self, monster_rect):
        dx = monster_rect.center[0] - self.player_rect_pistol.centerx
        dy = monster_rect.center[1] - self.player_rect_pistol.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance <= SHOOTING_DISTANCE:
            tolerance = 0.7  # Adjust the tolerance value as needed
            
            if self.last_moved == 'left' or self.last_moved == 'left_still':
                return dx < 0 and abs(dy) < abs(dx) * (1 - tolerance)
            elif self.last_moved == 'right' or self.last_moved == 'right_still':
                return dx > 0 and abs(dy) < abs(dx) * (1 - tolerance)
            elif self.last_moved == 'up' or self.last_moved == 'up_still':
                return dy < 0 and abs(dx) < abs(dy) * (1 - tolerance)
            elif self.last_moved == 'down' or self.last_moved == 'down_still':
                return dy > 0 and abs(dx) < abs(dy) * (1 - tolerance)
            elif self.last_moved == 'upleft' or self.last_moved == 'upleft_still':
                return dx < 0 and dy < 0 and abs(dx) > abs(dy)
            elif self.last_moved == 'upright' or self.last_moved == 'upright_still':
                return dx > 0 and dy < 0 and abs(dx) > abs(dy)
            elif self.last_moved == 'downleft' or self.last_moved == 'downleft_still':
                return dx < 0 and dy > 0 and abs(dx) > abs(dy)
            elif self.last_moved == 'downright' or self.last_moved == 'downright_still':
                return dx > 0 and dy > 0 and abs(dx) > abs(dy)
            
        return False


    def damage(self):
        return self.pistol_damage
            

player = Player(image_data, (50, 50))

