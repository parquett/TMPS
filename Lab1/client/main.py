from factory import VehicleFactory
from models import VehicleBuilder, VehicleDirector
from utilities import SingletonServiceCenter

factory = VehicleFactory()

car = factory.get_vehicle("car")
car.create()

bike = factory.get_vehicle("bike")
bike.create()

builder = VehicleBuilder()
director = VehicleDirector(builder)

director.build_sports_car()
sports_car = builder.get_product()
print(sports_car)

builder.reset()
director.build_bike()
bike = builder.get_product()
print(bike)

service_center1 = SingletonServiceCenter()
service_center1.register_vehicle("Car")

service_center2 = SingletonServiceCenter()
service_center2.register_vehicle("Bike")

print(service_center1 is service_center2)
