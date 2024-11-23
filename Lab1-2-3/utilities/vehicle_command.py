from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


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


class CommandInvoker:
    def __init__(self):
        self.command_queue = []

    def add_command(self, command):
        self.command_queue.append(command)

    def execute_commands(self):
        for command in self.command_queue:
            command.execute()
        self.command_queue.clear()
