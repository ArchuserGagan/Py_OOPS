#more than one parents
# in multi inheritance a class can have more then one parent

class Prey:
    def flee(self) -> None :
        print("i am  fleeeing ")


class Predator:
    def hunt(self) -> None:
        print("i am hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

hawk.hunt()
rabbit.flee()
fish.hunt()
fish.flee()



