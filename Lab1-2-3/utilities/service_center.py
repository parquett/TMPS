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
