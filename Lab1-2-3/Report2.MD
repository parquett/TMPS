# Structural Design Patterns  
**Author**: Martiniuc Artiom

## Objectives:
1. Study and understand Structural Design Patterns.
2. Choose a domain, define its main classes/models/entities and identify appropriate structural patterns.
3. Use structural design patterns to organize and extend functionality in a sample project.

## Domain: Vehicle Manufacturing

In this project, we demonstrate the implementation of three structural design patterns: **Facade**, **Adapter**, and **Decorator** in the domain of **Vehicle Manufacturing**. These patterns are used to manage the creation, registration, and enhancement of vehicles like cars and bikes, focusing on organizing interactions and extending functionality within the system.

## Used Design Patterns:
- **Facade**: Simplifies interactions by providing a unified interface (`VehicleManagementFacade`) to manage vehicle creation and registration processes.
- **Adapter**: Allows integration with an external service for vehicle registration through an adapter (`VehicleServiceAdapter`), adapting its interface to work with our system.
- **Decorator**: Adds dynamic functionality to vehicle objects, allowing flexible customization by adding features like a luxury package or a sports package.

---

## Implementation

The **Vehicle Manufacturing** system involves multiple key classes and patterns that work together to provide a flexible and extensible structure:

- **Facade** is used in the `VehicleManagementFacade` class, which provides a simplified interface for vehicle creation and registration, hiding the complexity of multiple interactions.
- **Adapter** is implemented through `VehicleServiceAdapter`, which enables integration with an external vehicle registration system by adapting its interface to match our system’s requirements.
- **Decorator** is implemented with `LuxuryPackageDecorator` and `SportsPackageDecorator`, allowing for the dynamic addition of features to vehicle objects without altering their structure.

### Code Snippets

#### Facade Pattern - `VehicleManagementFacade`
The `VehicleManagementFacade` class simplifies the client’s interaction with vehicle creation and registration by consolidating various functionalities.

```python
from factory.factory import VehicleFactory
from models.models import VehicleBuilder, VehicleDirector
from utilities.singleton import SingletonServiceCenter

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
```
#### Adapter Pattern - `VehicleServiceAdapter`
The `VehicleServiceAdapter` allows integration with an external vehicle registration service by adapting the interface
of the external system to match the requirements of our system.

```python
class ExternalVehicleService:
    def external_register(self, vehicle_type, details):
        print(f"External Service: Registering {vehicle_type} with details: {details}")

class VehicleServiceAdapter:
    def __init__(self, external_service):
        self.external_service = external_service

    def register_vehicle(self, vehicle_type, details):
        # Adapting the external service to match our system's interface
        self.external_service.external_register(vehicle_type, details)
```

### Decorator Pattern - `LuxuryPackageDecorator and SportsPackageDecorator`
The Decorator pattern allows dynamic enhancement of vehicle objects, providing additional features such as luxury 
or sports packages.

```python
from domain.base import Vehicle

class VehicleDecorator(Vehicle):
    def __init__(self, vehicle):
        self._vehicle = vehicle

    def create(self):
        self._vehicle.create()

class LuxuryPackageDecorator(VehicleDecorator):
    def create(self):
        super().create()
        print("Adding luxury package.")

class SportsPackageDecorator(VehicleDecorator):
    def create(self):
        super().create()
        print("Adding sports package.")

```

## Conclusion/Screenshots/Results
Output: 
```commandline
Car created.
Adding luxury package.
Bike created.
Adding sports package.
Vehicle with 4 wheels and V8 engine
Vehicle Car registered.
Vehicle Bike registered.
External Service: Registering Luxury Car with details: {'wheels': 4, 'engine': 'V12', 'color': 'Red'}
True

```

- The Facade pattern simplifies complex processes by providing a unified interface for vehicle creation and registration.
- The Adapter pattern enables seamless integration with external systems, adapting their interfaces to fit our system’s requirements.
- The Decorator pattern allows dynamic customization of vehicles, adding features like luxury and sports packages without modifying the underlying classes.