from boundries import *

def collision_with_static_object(obj1, obj2, coltol):
    if obj1.colliderect(obj2):
        if abs(obj1.right - obj2.left) < coltol:
            obj1.right = obj2.left
        elif abs(obj1.left - obj2.right) < coltol:
            obj1.left = obj2.right

        if abs(obj1.bottom - obj2.top) < coltol:
            obj1.bottom = obj2.top
        elif abs(obj1.top - obj2.bottom) < coltol:
            obj1.top = obj2.bottom


def collision_with_moving_object(obj1, obj2, coltol, player_speed, monster_speed, screenrect):
    if obj1.colliderect(obj2):
        if abs(obj1.right - obj2.left) < coltol:
            obj1.right = obj2.left
        elif abs(obj1.left - obj2.right) < coltol:
            obj1.left = obj2.right

        if abs(obj1.bottom - obj2.top) < coltol:
            obj1.bottom = obj2.top
        elif abs(obj1.top - obj2.bottom) < coltol:
            obj1.top = obj2.bottom

    if obj1.colliderect(obj2):
        if player_speed >= monster_speed:
            if obj1.right > obj2.left and obj1.left < obj2.left:
                obj1.right = obj2.left
            elif obj1.left < obj2.right and obj1.right > obj2.right:
                obj1.left = obj2.right

    if obj1.colliderect(obj2):
        if player_speed >= monster_speed:
            if obj1.bottom > obj2.top and obj1.top < obj2.top:
                obj1.bottom = obj2.top
            elif obj1.top < obj2.bottom and obj1.bottom > obj2.bottom:
                obj1.top = obj2.bottom


    if not screenrect.contains(obj1):

        if obj1.left < BOUNDRY_LEFT:
            obj1.left = BOUNDRY_LEFT
        elif obj1.right > BOUNDRY_RIGHT:
            obj1.right = BOUNDRY_RIGHT
        if obj1.top < BOUNDRY_TOP:
            obj1.top = BOUNDRY_TOP
        elif obj1.bottom > BOUNDRY_BOTTOM:
            obj1.bottom = BOUNDRY_BOTTOM

    # Check for boundary collision with obj2
    if not screenrect.contains(obj2):

        if obj2.left < BOUNDRY_LEFT:
            obj2.left = BOUNDRY_LEFT
        elif obj2.right > BOUNDRY_RIGHT:
            obj2.right = BOUNDRY_RIGHT
        if obj2.top < BOUNDRY_TOP:
            obj2.top = BOUNDRY_TOP
        elif obj2.bottom > BOUNDRY_BOTTOM:
            obj2.bottom = BOUNDRY_BOTTOM
