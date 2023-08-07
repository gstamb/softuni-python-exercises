from abc import ABC, abstractmethod


class BaseVehicle(ABC):

    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level = 100
        self.is_damaged = False

    def __str__(self):
        return f"{self.brand} {self.model} License plate: {self.license_plate_number} Battery: {self.battery_level}% Status: {'Damaged' if self.is_damaged else 'OK'}"

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if value.strip():
            self.__brand = value
        else:
            raise ValueError("Brand cannot be empty!")

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip():
            self.__model = value
        else:
            raise ValueError("Model cannot be empty!")

    @property
    def license_plate_number(self):
        return self.__license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value):
        if value.strip():
            self.__license_plate_number = value
        else:
            raise ValueError("License plate number is required!")

    @abstractmethod
    def drive(self, mileage: float):
        pass

    def recharge(self):
        self.battery_level = 100

    def change_status(self):
        if self.is_damaged:
            self.is_damaged = False
        else:
            self.is_damaged = True
