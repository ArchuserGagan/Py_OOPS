#duck typing = another way to achieve polymorphism besides inheritance
# object must have minimium necessary attributes/methods
# "if it looks like a duck and quacks like a duck then it must be a duck "


class Animal:
    alive = True

class Dog(Animal):
    def speak(self) -> None:
        print("woof!")

class Cat(Animal):
    def speak(self) -> None:
        print("Meow")

class Car:
    alive = False   # car has minimum  req to be animal so we can treatit like a duck 
    def speak(self) -> None:
        print("honk!")
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)