from factory import VehicleFactory
from models import VehicleBuilder, VehicleDirector
from utilities import (SingletonServiceCenter, LuxuryPackageDecorator, SportsPackageDecorator,
                       ExternalVehicleService, VehicleServiceAdapter, VehicleManagementFacade)

# Initialize the Facade
vehicle_facade = VehicleManagementFacade()

# Create and register a basic car using Facade
vehicle_facade.create_and_register_vehicle("car")

# Create and register a sports car with Facade
vehicle_facade.build_and_register_sports_car()

# Create and register a bike using Facade
vehicle_facade.build_and_register_bike()

# Demonstrate Decorator Pattern
basic_car = vehicle_facade.factory.get_vehicle("car")
luxury_car = LuxuryPackageDecorator(basic_car)
sports_car = SportsPackageDecorator(basic_car)

print("Creating a luxury car:")
luxury_car.create()

print("\nCreating a sports car:")
sports_car.create()

# Demonstrate Adapter Pattern
external_service = ExternalVehicleService()
adapter = VehicleServiceAdapter(external_service)
adapter.register_vehicle("Luxury Car", {"wheels": 4, "engine": "V12", "color": "Red"})

# Demonstrate Singleton
service_center1 = SingletonServiceCenter()
service_center2 = SingletonServiceCenter()
print("\nAre service_center1 and service_center2 the same instance?")
print(service_center1 is service_center2)
