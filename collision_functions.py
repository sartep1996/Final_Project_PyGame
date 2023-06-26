

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
