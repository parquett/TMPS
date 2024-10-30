from domain import Vehicle

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
