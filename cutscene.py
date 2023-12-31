import pygame as pg
import time

pg.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font_file = "assets/fonts/Rhuma Sinera Regular.ttf"  # Replace with your font file's name
font = pg.font.Font(font_file, 36)
text = "Pagaliau, Laivas! Galiu keliauti namo"

def draw_black_bars(screen):
    # Draw black bars on the top of the screen
    top_bar_height = SCREEN_HEIGHT // 4
    bottom_bar_height = SCREEN_HEIGHT // 4
    top_bar = pg.Surface((SCREEN_WIDTH, top_bar_height))
    bottom_bar = pg.Surface((SCREEN_WIDTH, bottom_bar_height))
    top_bar.fill(BLACK)
    bottom_bar.fill(BLACK)

    screen.blit(top_bar, (0, 0))
    screen.blit(bottom_bar, (0, SCREEN_HEIGHT - bottom_bar_height))
    pg.display.update()


def display_text(screen):
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8))
    screen.blit(text_surface, text_rect)
    pg.display.update()

def create_cutscene_sprite(screen):
    sprite_image = pg.image.load("Images/Background_objects/cutscene_sprite.png") 
    sprite_image.set_alpha(0)
    sprite_rect = sprite_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    sprite_rect.topleft = (0, 30)

    for alpha in range(0, 256, 5):
        sprite_image.set_alpha(alpha)
        screen.blit(sprite_image, sprite_rect)
        pg.time.delay(30)

    sprite_image.set_alpha(255)
    pg.display.update()

    return sprite_image


def move_sprite_to(sprite, position):
    sprite.topleft = position

def wait_for_input_or_duration(duration):
    pass

def remove_sprite(sprite):
    pass


# Main function to run the cutscene
def run_cutscene(screen):
    running = True
    clock = pg.time.Clock()
    draw_black_bars(screen)
    display_text(screen)
    create_cutscene_sprite(screen)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    running = False
    
        pg.display.update()
        clock.tick(30)
            


if __name__ == "__main__":
    run_cutscene()
