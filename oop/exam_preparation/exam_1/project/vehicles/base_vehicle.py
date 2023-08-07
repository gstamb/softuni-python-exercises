from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    ERR_MSG_EMPTY_BRAND = "Brand cannot be empty!"
    ERR_MSG_EMPTY_MODEL = "Model cannot be empty!"
    ERR_MSG_EMPTY_LPN = "License plate number is required!"
    max_battery = 100

    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level = self.max_battery
        self.is_damaged = False

    def __str__(self):
        return f"{self.brand} {self.model} License plate: {self.license_plate_number} Battery:" \
               f" {self.battery_level}% Status: {'Damaged' if self.is_damaged else 'OK'}"

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if value.strip():
            self.__brand = value
        else:
            raise ValueError(self.ERR_MSG_EMPTY_BRAND)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip():
            self.__model = value
        else:
            raise ValueError(self.ERR_MSG_EMPTY_MODEL)

    @property
    def license_plate_number(self):
        return self.__license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value):
        if value.strip():
            self.__license_plate_number = value
        else:
            raise ValueError(self.ERR_MSG_EMPTY_LPN)

    @abstractmethod
    def drive(self, mileage: float):
        pass

    def recharge(self):
        self.battery_level = self.max_battery

    def change_status(self):
        if self.is_damaged:
            self.is_damaged = False
        else:
            self.is_damaged = True


if __name__ == "__main__":
    pass
