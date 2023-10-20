# Prevents a user from creating an object of that class
# abstract class = a class which containts one or more abstract methods.
# abstract method = a method that has a declaration but does not have an impementation

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")
    def stop(self):
        print("You stopped the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("You stopped the moto")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()


car.go()
motorcycle.go()

car.stop()
motorcycle.stop()