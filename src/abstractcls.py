#abstract class meant for inherited, abstractmethods are meant for overriden
##abs class can be use to like check like in this eg vehicle should able to go and stop so if only car etc class have both stop and go fx only then it will run or it will crash
#we cant define fx in abs class
from abc import ABC, abstractclassmethod # we are importing abstaract class and method from abc



class Vehical(ABC):


    @abstractclassmethod
    def go(self) -> None:
        pass

    @abstractclassmethod
    def stop(self) -> None:
        pass

class Car(Vehical):


    def go(self) -> None:
        print("you drive the car")

    def stop(self) -> None:
        print("you stop the car")

class Motorcycle(Vehical):


    def go(self) -> None:
        print("you drive the motorcycle")

    def stop(self) -> None:
        print("you stop the motorcycle")


car = Car()
motorcycle = Motorcycle()
car.go()
motorcycle.stop()

