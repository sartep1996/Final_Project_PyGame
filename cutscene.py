import pygame as pg
import time
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font_file = "assets/fonts/Rhuma Sinera Regular.ttf"  # Replace with your font file's name
font = pg.font.Font(font_file, 36)
text = "Pagaliau, Laivas! Galiu keliauti namo"

def draw_black_bars(screen):
    # Draw black bars on the top of the screen
    bar_height = SCREEN_HEIGHT // 4
    top_bar = pg.Surface((SCREEN_WIDTH, bar_height))
    top_bar.fill((BLACK))
    screen.blit(top_bar, (0, 0))
    pg.display.update()


def display_text(screen):
    # Display the text in the center of the screen above the black bars
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8))
    screen.blit(text_surface, text_rect)
    pg.display.update()

def create_cutscene_sprite(screen):
    sprite_image = pg.image.load("your_sprite_image.png") 
    sprite_image.set_alpha(0)
    sprite_rect = sprite_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    for alpha in range(0, 256, 5):
        sprite_image.set_alpha(alpha)
        screen.fill(BLACK) 
        draw_black_bars()
        screen.blit(sprite_image, sprite_rect)
        pg.display.update()
        pg.time.delay(30)  # Delay between each frame update (adjust for desired speed)

    sprite_image.set_alpha(255)

    return sprite_image

def move_sprite_to(sprite, position):
    sprite.topleft = position

def wait_for_input_or_duration(duration):
    pass

def remove_sprite(sprite):
    pass


# Main function to run the cutscene
def run_cutscene(player_rect, ship_rect, screen):

    if player_rect.collidedict(ship_rect):
        draw_black_bars(screen)
        display_text(text)
        sprite = create_cutscene_sprite()
        remove_sprite(sprite)


if __name__ == "__main__":
    run_cutscene()
