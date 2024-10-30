class ExternalVehicleService:
    def external_register(self, vehicle_type, details):
        print(f"External Service: Registering {vehicle_type} with details: {details}")


class VehicleServiceAdapter:
    def __init__(self, external_service):
        self.external_service = external_service

    def register_vehicle(self, vehicle_type, details):
        # Adapting the external service to match our system's interface
        self.external_service.external_register(vehicle_type, details)
