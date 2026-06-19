# polymorphism   = poly  = many , morphe = forms
# this is polymorphism using inheritance
#inheritandce = an object could be treated of the same type as a parent class

from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius) -> None:
        self.radius = radius

    def area(self)-> None:
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def area(self) -> None:
        return self.side * self.side

        

class Triangle(Shape):
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height
    def area(self)-> None:
        return self.height * self.base * 0.5  
class Pizza(Circle):
    def __init__(self, radius, toppings) -> None:
        super().__init__(radius) #super consider of the parent
        self.toppings = toppings

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza(5, "pepporina")]

for shape in shapes:
    print(f"{shape.area()}cm^2")