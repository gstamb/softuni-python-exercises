from abc import ABC, abstractmethod
from project.baked_food.cake import Cake
from project.drink.tea import Tea


class Table(ABC):
    MIN_CAPACITY = 0

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    @abstractmethod
    def TABLE_TYPE_RANGE(self):
        pass

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= self.MIN_CAPACITY:
            raise ValueError(f"Capacity has to be greater than {self.MIN_CAPACITY}!")
        self.__capacity = value

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not min(self.TABLE_TYPE_RANGE) <= value < max(self.TABLE_TYPE_RANGE):
            raise ValueError(
                f"{self.__class__.__name__} table's number must be between {min(self.TABLE_TYPE_RANGE)} and {max(self.TABLE_TYPE_RANGE) - 1} inclusive!")
        self.__table_number = value

    def reserve(self, number_of_people: int):
        if self.capacity >= number_of_people:
            self.is_reserved = True
            self.number_of_people = number_of_people

    def order_food(self, baked_food):
        self.food_orders.append(baked_food)

    def order_drink(self, drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        total_food_price = sum([food.price for food in self.food_orders])
        total_drink_price = sum([drink.price for drink in self.drink_orders])
        bill = total_drink_price + total_food_price
        return bill

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.is_reserved = False
        self.number_of_people = 0

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"


if __name__ == "__main__":
    pass
