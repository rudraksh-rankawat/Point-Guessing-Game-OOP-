from rectangle import Rectangle
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def falls_in_reactangle(self, rectangle: Rectangle) -> bool:
        if rectangle.lowleft.x < self.x < rectangle.upright.x and \
                rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False