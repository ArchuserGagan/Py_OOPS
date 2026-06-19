

class Animal:
    def __init__(self, name) -> None :
        self.name = name
        self.is_alive = True

    def eat(self) -> None :
        print(f"{self.name} is sleeping")

    def sleep(self) -> None :
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self) -> None :
        print("woof")
    

class Cat(Animal):
    def speak(self) -> None:
        print("meow")

class Mouse(Animal):
    def speak(self) -> None:

        print("squeak")



dog = Dog("scooby")
cat = Cat("smut")
mouse = Mouse("mickey")


print(dog.name)
print(dog.is_alive)
dog.eat()
cat.sleep() 
cat.speak()
mouse.speak()
dog.speak()