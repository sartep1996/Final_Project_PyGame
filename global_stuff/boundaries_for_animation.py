
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BOUNDRY_LEFT = 25
BOUNDRY_TOP = 0
BOUNDRY_RIGHT = SCREEN_WIDTH - 25
BOUNDRY_BOTTOM = SCREEN_HEIGHT - 25


def boundries1(object):
    if object.left < BOUNDRY_LEFT:
        object.left = BOUNDRY_LEFT
    if object.right > BOUNDRY_RIGHT:
        object.right = BOUNDRY_RIGHT 
    if object.top < BOUNDRY_TOP:
        object.top = BOUNDRY_TOP 
    if object.bottom > BOUNDRY_BOTTOM:
       object.bottom = BOUNDRY_BOTTOM