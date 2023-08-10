from abc import ABC, abstractmethod


class Meal(ABC):
    CONDITION_MIN_PRICE_SETTER = 0
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Name cannot be an empty string!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= self.CONDITION_MIN_PRICE_SETTER:
            raise ValueError("Invalid price!")
        self.__price = value

    @abstractmethod
    def details(self):
        pass


if __name__ == "__main__":
    pass
