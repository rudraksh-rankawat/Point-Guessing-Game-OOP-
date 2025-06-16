from point import Point
class Rectangle:
    def __init__(self, lowleft: Point, upright: Point):
        self.lowleft = lowleft
        self.upright = upright

    def get_area(self) -> float:
        return (self.upright.x - self.lowleft.x) * \
                (self.upright.y - self.lowleft.y)
