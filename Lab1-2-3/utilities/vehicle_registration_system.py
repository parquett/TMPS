from utilities import Subject


class VehicleRegistrationSystem(Subject):
    def __init__(self):
        self._observers = []  # List of observers
        self._latest_vehicle = None  # State to track the latest registered vehicle

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._latest_vehicle)

    def register_vehicle(self, vehicle):
        self._latest_vehicle = vehicle
        print(f"Vehicle {vehicle} registered in the system.")
        self.notify()  # Notify all observers
