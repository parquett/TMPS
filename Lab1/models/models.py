class VehicleProduct:
    def __init__(self):
        self.wheels = None
        self.engine = None

    def __str__(self):
        return f"Vehicle with {self.wheels} wheels and {self.engine} engine"

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

class VehicleDirector:
    def __init__(self, builder):
        self._builder = builder

    def build_sports_car(self):
        self._builder.set_wheels(4)
        self._builder.set_engine("V8")

    def build_bike(self):
        self._builder.set_wheels(2)
        self._builder.set_engine("Single-cylinder")
