# Creational Design Patterns  
**Author**: Martiniuc Artiom

## Objectives:
1. Study and understand the Creational Design Patterns.
2. Choose a domain, define its main classes/models/entities and choose the appropriate instantiation mechanisms.
3. Use some creational design patterns for object instantiation in a sample project.

## Domain: Vehicle Manufacturing

In this project, we demonstrate the implementation of three creational design patterns: **Singleton**, **Factory Method**, and **Builder** in the domain of **Vehicle Manufacturing**. We simulate the creation and management of vehicles like cars and bikes, using these design patterns to control object instantiation and ensure a flexible design.

## Used Design Patterns:
- **Singleton**: Ensures a single instance of the `ServiceCenter` class to manage vehicle registrations.
- **Factory Method**: Provides a method to create vehicle objects (`Car` and `Bike`) based on user input without specifying the exact class of the object.
- **Builder**: Constructs complex `Vehicle` objects in a step-by-step manner using a `Director` and `Builder`.

---

## Implementation

The **Vehicle Manufacturing** system involves three key classes: `VehicleFactory`, `VehicleBuilder`, and `SingletonServiceCenter`. These classes leverage **Factory Method**, **Builder**, and **Singleton** design patterns respectively to demonstrate different object creation approaches.

- **Factory Method** is used in the `VehicleFactory` class, allowing flexible creation of `Car` and `Bike` objects without modifying the client code.
- **Builder** is implemented in the `VehicleBuilder` class, which constructs vehicles part-by-part, enabling the creation of complex objects like a car or bike.
- **Singleton** is demonstrated through `SingletonServiceCenter`, which ensures that there is only one instance of a service center registering the created vehicles.

### Code Snippets

#### Singleton Pattern - `SingletonServiceCenter`
```python
class SingletonServiceCenter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonServiceCenter, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.vehicles = []

    def register_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle} registered.")
```

#### Factory Method Pattern - `VehicleFactory`
```python
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError("Unknown vehicle type")
```

#### Builder Pattern - `VehicleBuilder`
```python
class VehicleBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.vehicle = VehicleProduct()

    def set_wheels(self, wheels):
        self.vehicle.wheels = wheels

    def set_engine(self, engine):
        self.vehicle.engine = engine

    def get_product(self):
        return self.vehicle
```

## Conclusion/Screenshots/Results
Output: 
```commandline
Car created.
Bike created.
Vehicle with 4 wheels and V8 engine
Vehicle Car registered.
Vehicle Bike registered.
True
```

- The Singleton pattern ensures that the SingletonServiceCenter class only has one instance.
- The Factory Method allows creating instances of vehicles (Car and Bike) without changing the client code.
- The Builder pattern provides a flexible way to construct vehicles step by step.
