# Imports
import sys, threading
import pygame as pg

pg.init()



# Screen and font
screen = pg.display.set_mode((800, 600))

loading_background = pg.transform.scale(pg.image.load('Images/Background/loading_backgroun.png'), (800, 600))

pg.display.set_caption("Loading")


# Clock
CLOCK = pg.time.Clock()

# Work
WORK = 10000000

# Loading BG
LOADING_BG = pg.transform.scale(pg.image.load("Images/Loading_Bar/loading_bar_background.png").convert_alpha(), (680, 60))
LOADING_BG_RECT = LOADING_BG.get_rect(center=(400, 500))

# Loading Bar and variables
loading_bar = pg.transform.scale(pg.image.load("Images/Loading_Bar/loading_bar.png").convert_alpha(), (60, 60))
loading_bar_rect = loading_bar.get_rect(midleft=(80, 300))
loading_finished = False
loading_progress = 0
loading_bar_width = 8

def doWork():
    global loading_finished, loading_progress

    for i in range(WORK):
        math_equation = 523687 / 789456 * 89456
        loading_progress = i 

    loading_finished = True

threading.Thread(target=doWork).start()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill("Dark green")
    screen.blit(loading_background, (0,0))

    loading_bar_width = loading_progress / WORK * 640

    loading_bar = pg.transform.scale(loading_bar, (int(loading_bar_width), 60))
    loading_bar_rect = loading_bar.get_rect(midleft=(80, 500))

    screen.blit(LOADING_BG, LOADING_BG_RECT)
    screen.blit(loading_bar, loading_bar_rect)


    pg.display.update()
    CLOCK.tick(60)

    

