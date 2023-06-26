import pygame as pg


# background plane
plane_b_object_unscaled = pg.image.load("Images/Background_objects/background_plane.png").convert_alpha()
plane_b_object = pg.transform.scale(plane_b_object_unscaled, (300, 170))


object_x = 0
object_y = 0
#

