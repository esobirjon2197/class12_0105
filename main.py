

# 11-m
import math

class Shape:
    def __init__(self, name, color, border):
        self.name = name
        self.color = color
        self.border = border

    def area(self):
        print("Aniqlanmagan")


class Circle(Shape):
    def __init__(self, name, color, border, radius, diameter):
        super().__init__(name, color, border)
        self.radius = radius
        self.diameter = diameter

    def area(self):
        super().area()
        print("Yuza:", math.pi * self.radius ** 2)


c = Circle("Doira", "Ko‘k", "Qalin", 5, 10)
c.area()
