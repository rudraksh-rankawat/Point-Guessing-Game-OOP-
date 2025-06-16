from random import randint
import turtle


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def falls_in_reactangle(self, rectangle) -> bool:
        if rectangle.lowleft.x < self.x < rectangle.upright.x and \
                rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False
        
class Rectangle:
    def __init__(self, lowleft: Point, upright: Point):
        self.lowleft = lowleft
        self.upright = upright

    def get_area(self) -> float:
        return (self.upright.x - self.lowleft.x) * \
                (self.upright.y - self.lowleft.y)
    

class RectangleOnCanvas(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.lowleft.x, self.lowleft.y)
        canvas.pendown()
        canvas.forward(self.upright.x - self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.lowleft.y)
        canvas.left(90)
        canvas.forward(self.upright.x - self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.lowleft.y)
        turtle.done()
    


if __name__ == "__main__":
    #randomly generated rectangle
    rectangle = RectangleOnCanvas(Point(randint(40, 100), randint(30,100)),
                           Point(randint(101,200), randint(101,200)))
    print(f"Rectangle Coordinates: {rectangle.lowleft.x, rectangle.lowleft.y} and {rectangle.upright.x, rectangle.upright.y}")

    rectangle.draw(turtle.Turtle())


    #ask user to guess a point
    print("Guess a point which lies in the above rectangle:")
    user_point = Point(float(input("Guess X coordinate:")),
                    float(input("Guess Y coordinate: ")))

    #ask user to guess the area of rectangle
    user_area = float(input("Guess the area:"))
    
    #print if user point falls in rectangle or not
    print(f"Does the point lie in the rectangle: {"Yes" if user_point.falls_in_reactangle(rectangle) else "No"}")

    #print the difference between user's guessed aread vs real area
    print("Your area was off by:", user_area - rectangle.get_area())

