import math
from turtle import circle

class Circle:
    def __init__(self, radius=1):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius # pyright: ignore[reportUndefinedVariable]
    def perimeter(self):
        return 2 * math.pi * self.radius**2

input_radius = float(input("enter the radius of circle:"))
circle = Circle(input_radius)
print("area of Circle is ",circle.area())
print("the perimeter of Circle is ",circle.perimeter())

      