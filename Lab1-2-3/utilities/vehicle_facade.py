from factory import VehicleFactory
from models import VehicleBuilder, VehicleDirector
from utilities import SingletonServiceCenter

class VehicleManagementFacade:
    def __init__(self):
        self.factory = VehicleFactory()
        self.builder = VehicleBuilder()
        self.director = VehicleDirector(self.builder)
        self.service_center = SingletonServiceCenter()

    def create_and_register_vehicle(self, vehicle_type):
        # Create the vehicle
        vehicle = self.factory.get_vehicle(vehicle_type)
        vehicle.create()

        # Register the vehicle
        self.service_center.register_vehicle(vehicle_type)

    def build_and_register_sports_car(self):
        self.director.build_sports_car()
        sports_car = self.builder.get_product()
        print(sports_car)
        self.service_center.register_vehicle("Sports Car")

    def build_and_register_bike(self):
        self.director.build_bike()
        bike = self.builder.get_product()
        print(bike)
        self.service_center.register_vehicle("Bike")
