from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, vehicle):
        pass


class ExternalServiceObserver(Observer):
    def update(self, vehicle):
        print(f"External Service notified: Vehicle {vehicle} has been registered.")


class ManagerObserver(Observer):
    def update(self, vehicle):
        print(f"Manager notified: Vehicle {vehicle} has been added to the system.")
