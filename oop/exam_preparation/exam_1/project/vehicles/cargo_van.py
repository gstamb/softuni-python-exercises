from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    load_battery_penalty = 5

    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float = 180):
        super().__init__(brand, model, license_plate_number, max_mileage)
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage

    def drive(self, mileage: float):
        battery_discharge = round(mileage / self.max_mileage * 100)
        self.battery_level -= (battery_discharge + self.load_battery_penalty)


