from utilities import (SingletonServiceCenter, LuxuryPackageDecorator, SportsPackageDecorator,
                       ExternalVehicleService, VehicleServiceAdapter, CommandInvoker, CreateVehicleCommand,
                       BuildBikeCommand, BuildSportsCarCommand)
from utilities.vehicle_facade import VehicleManagementFacade

# Initialize the Facade
vehicle_facade = VehicleManagementFacade()

# Initialize the command invoker
invoker = CommandInvoker()

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

# Demonstrate Command Pattern
invoker.add_command(CreateVehicleCommand(vehicle_facade, "car"))
invoker.add_command(BuildSportsCarCommand(vehicle_facade))
invoker.add_command(BuildBikeCommand(vehicle_facade))
invoker.execute_commands()
