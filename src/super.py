#super() = function used in a child class to call methods from a parent class (superclass)
# allows yu to extend the functionality of the inherited methods


class Shape():
    def __init__(self, color, isfilled) -> None:
        self.color = color
        self.isfilled = isfilled

    def describe(self) -> None:
        print(f"it is {self.color} and {'filled' if self.isfilled else 'not filled'}")



class Circle(Shape):
    def __init__(self, color, isfilled, radius) -> None:
        super().__init__(color, isfilled)
        self.radius = radius
    def describe(self) -> None:
        super().describe()
        print(f"area of circle is {3.14 * self.radius * self.radius}cm^sq")   # this is called method overriding
        


class Square(Shape):
    def __init__(self, color, isfilled, width) -> None:
        super().__init__(color, isfilled)
        self.width = width
    def describe(self) -> None:
        super().describe()
        print(f"area of square is {self.width * self.width}cm^sq")   # this is called method overriding

class Triangle(Shape):
    def __init__(self, color, isfilled, height, width) -> None:
        super().__init__(color, isfilled)
        self.height = height
        self.width = width
    def describe(self) -> None:
        super().describe()
        print(f"area of triangle is {self.width * self.height / 2}cm^sq")   # this is called method overriding


circle = Circle("red", True, 5)
print(circle.color)
print(circle.isfilled)
print(circle.radius)
circle.describe()
square = Square("blue", False, 7)
print(square.width)
print(square.color)
print(square.isfilled)

square.describe()
triangle = Triangle("yellow", True, 8, 7)
print(triangle.color)
print(triangle.width)
print(triangle.height)
print(triangle.isfilled)
triangle.describe()