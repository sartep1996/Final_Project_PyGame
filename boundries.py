
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BOUNDRY_LEFT = 25
BOUNDRY_TOP = 25
BOUNDRY_RIGHT = SCREEN_WIDTH - 25
BOUNDRY_BOTTOM = SCREEN_HEIGHT - 25

def boundries(object):
    if object.left < BOUNDRY_LEFT:
        object.left = BOUNDRY_LEFT
    if object.right > BOUNDRY_RIGHT:
        object.right = BOUNDRY_RIGHT 
    if object.top < BOUNDRY_TOP:
        object.top = BOUNDRY_TOP 
    if object.bottom > BOUNDRY_BOTTOM:
       object.bottom = BOUNDRY_BOTTOM



def boundries_lvl_1(object):
    if object.left < BOUNDRY_LEFT:
        object.left = BOUNDRY_LEFT
    if object.right > BOUNDRY_RIGHT:
        object.right = BOUNDRY_RIGHT 
    if object.top < BOUNDRY_TOP  and object.left < SCREEN_WIDTH - 300:
        object.top = BOUNDRY_TOP 
    if object.bottom > BOUNDRY_BOTTOM:
       object.bottom = BOUNDRY_BOTTOM

def boundries_lvl_2(object):
    if object.left < BOUNDRY_LEFT:
        object.left = BOUNDRY_LEFT
    if object.right > BOUNDRY_RIGHT:
        object.right = BOUNDRY_RIGHT 
    if object.top < BOUNDRY_TOP and object.left < SCREEN_WIDTH - 350:
        object.top = BOUNDRY_TOP 
    if object.bottom > BOUNDRY_BOTTOM:
       object.bottom = BOUNDRY_BOTTOM



def boundries_lvl_final(object):
    BOUNDRY_TOP = 200
    BOUNDRY_RIGHT = SCREEN_WIDTH
    BOUNDRY_LEFT = 0
    if object.left < BOUNDRY_LEFT:
        object.left = BOUNDRY_LEFT
    if object.right > BOUNDRY_RIGHT:
        object.right = BOUNDRY_RIGHT 
    if object.top < BOUNDRY_TOP:
        object.top = BOUNDRY_TOP 
    if object.bottom > BOUNDRY_BOTTOM:
       object.bottom = BOUNDRY_BOTTOM
