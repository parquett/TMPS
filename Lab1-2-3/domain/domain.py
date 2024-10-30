from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def create(self):
        pass

class Car(Vehicle):
    def create(self):
        print("Car created.")

class Bike(Vehicle):
    def create(self):
        print("Bike created.")
