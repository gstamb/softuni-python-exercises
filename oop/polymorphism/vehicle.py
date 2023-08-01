from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption  # litres per km
        self.summer_extra_fuel_consumption = 0.9

    def drive(self, distance: int):
        distance_total_fuel_consumption = distance * (self.fuel_consumption + self.summer_extra_fuel_consumption)
        if distance_total_fuel_consumption > self.fuel_quantity:
            pass
        else:
            self.fuel_quantity -= distance_total_fuel_consumption

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption  # litres per km
        self.summer_extra_fuel_consumption = 1.6
        self.fuel_capacity_penalty = 0.95  # of total fuel when refueled

    def drive(self, distance: int):
        distance_total_fuel_consumption = distance * (self.fuel_consumption + self.summer_extra_fuel_consumption)
        if distance_total_fuel_consumption > self.fuel_quantity:
            pass
        else:
            self.fuel_quantity -= distance_total_fuel_consumption

    def refuel(self, fuel: int):
        fuel_without_penalty = fuel * self.fuel_capacity_penalty
        self.fuel_quantity += fuel_without_penalty
