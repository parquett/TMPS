# Behavioral Design Patterns  
**Author**: Martiniuc Artiom

## Objectives:
1. Study and understand Behavioral Design Patterns.
2. Choose a domain, define its main classes/models/entities and identify appropriate behavioral patterns.
3. Use behavioral design patterns to organize and extend functionality in a project.

## Domain: Vehicle Manufacturing

In this project, we demonstrate the implementation of two behavioral design patterns: **Observer** and **Command** in the domain of **Vehicle Manufacturing**. These patterns are used to handle notifications of vehicle registrations and to encapsulate actions as commands for more flexible and extensible system operations.

---

## Used Design Patterns:

- **Observer**: This pattern enables the `VehicleRegistrationSystem` (the subject) to notify multiple observers when a vehicle is registered. Observers such as `ExternalServiceObserver` and `ManagerObserver` can react independently to these notifications.

- **Command**: This pattern encapsulates actions like creating, registering, and building vehicles as objects, enabling features like centralized execution, queuing, and extensibility via a `CommandInvoker`.

---

## Implementation

### **Observer Pattern**

#### Components:
- **Subject**: `VehicleRegistrationSystem` maintains a list of observers and notifies them when a vehicle is registered.
- **Observers**: 
  - `ExternalServiceObserver`: Represents an external service that gets notified about vehicle registrations.
  - `ManagerObserver`: Represents a manager who is notified when a new vehicle is registered.

##### Subject: `VehicleRegistrationSystem`
```python
from .observer_pattern import Subject

class VehicleRegistrationSystem(Subject):
    def __init__(self):
        self._observers = []
        self._latest_vehicle = None

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
        self.notify()
```
#### Observers: `ExternalServiceObserver` and `ManagerObserver`
```python
class ExternalServiceObserver(Observer):
    def update(self, vehicle):
        print(f"External Service notified: Vehicle {vehicle} has been registered.")

class ManagerObserver(Observer):
    def update(self, vehicle):
        print(f"Manager notified: Vehicle {vehicle} has been added to the system.")
```
#### Integration:
In the `VehicleManagementFacade`, the `VehicleRegistrationSystem` is used to register vehicles and notify the observers.

### Command Pattern
#### Components:
- **Command Interface**: Command defines the interface for all commands.
- **Concrete Commands**: Specific commands like `CreateVehicleCommand`, `BuildSportsCarCommand`, and `BuildBikeCommand` encapsulate actions.
- **Invoker**: `CommandInvoker` executes the commands in a centralized manner.

#### Command Interface
```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
```
#### Concrete Commands
```python
class CreateVehicleCommand(Command):
    def __init__(self, facade, vehicle_type):
        self.facade = facade
        self.vehicle_type = vehicle_type

    def execute(self):
        self.facade.create_and_register_vehicle(self.vehicle_type)

class BuildSportsCarCommand(Command):
    def __init__(self, facade):
        self.facade = facade

    def execute(self):
        self.facade.build_and_register_sports_car()

class BuildBikeCommand(Command):
    def __init__(self, facade):
        self.facade = facade

    def execute(self):
        self.facade.build_and_register_bike()
```

#### Command Invoker
```python
class CommandInvoker:
    def __init__(self):
        self.command_queue = []

    def add_command(self, command):
        self.command_queue.append(command)

    def execute_commands(self):
        for command in self.command_queue:
            command.execute()
        self.command_queue.clear()
```
#### Integration:
The `CommandInvoker` executes commands that encapsulate actions like creating, registering, and building vehicles, using the `VehicleManagementFacade`.

### Conclusion/Screenshots/Results

Output:
```commandline
Car created.
Vehicle car registered.
Vehicle car registered in the system.
External Service notified: Vehicle car has been registered.
Manager notified: Vehicle car has been added to the system.
Vehicle with 4 wheels and V8 engine
Vehicle Sports Car registered.
Vehicle Sports Car registered in the system.
External Service notified: Vehicle Sports Car has been registered.
Manager notified: Vehicle Sports Car has been added to the system.
Vehicle with 2 wheels and Single-cylinder engine
Vehicle Bike registered.
Vehicle Bike registered in the system.
External Service notified: Vehicle Bike has been registered.
Manager notified: Vehicle Bike has been added to the system.

```
**Benefits of Observer Pattern**:
- Decoupling: Observers are decoupled from the subject, allowing independent reactions to changes.
- Scalability: New observers can be added without modifying the subject.
- Real-time Updates: Notifications ensure all observers are immediately aware of changes.

**Benefits of Command Pattern**:
- Encapsulation: Commands encapsulate specific operations, improving code organization.
- Centralized Execution: The CommandInvoker enables centralized execution and queuing of commands.
- Extensibility: Adding new commands is straightforward.

