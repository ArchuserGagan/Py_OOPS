#in multilevel parent can inherit from other parent




class Animal:
    def __init__(self, name) -> None:
        self.name = name
    def eat(self) -> None:
        print(f"{self.name}  can sleep")

    def sleep(self) -> None:
        print(f"{self.name} can sleep")



class Prey(Animal):
    def flee(self) -> None :
        print(f"{self.name} is fleeeing ")

# parent inherting from parent animal is parent of prey and predator and prey and predetar are parents to other
class Predator(Animal):
    def hunt(self) -> None:
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("tony")
hawk = Hawk("baldo")
fish = Fish("dimitrius")

hawk.hunt()
rabbit.flee()
fish.hunt()
fish.flee()
fish.eat()
rabbit.sleep()
hawk.sleep()