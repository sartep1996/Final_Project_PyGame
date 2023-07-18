import pygame as pg

loading_progress = 0
pg.mixer.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((800, 600))
loading_finished = False

loading_background = pg.transform.scale(pg.image.load('Images/Background/loading_backgroun.png'), (800, 600))

frame_index = 0
while not loading_finished:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    if not loading_finished:
        loading_progress += 1
        if loading_progress >= 100:  
            loading_finished = True

    screen.fill("#0d0e2e")
    screen.blit(loading_background, (0,0))


    loading_bar_width = loading_progress / 100 * 640

    loading_bar = pg.Surface((loading_bar_width, 60))
    loading_bar.fill((255, 255, 255))
    screen.blit(loading_bar, (80, 500))

    frame_filename = f"loading_frame_{frame_index:04d}.png"
    pg.image.save(screen, frame_filename)

    pg.display.update()
    clock.tick(60)

    frame_index += 1
