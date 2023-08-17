from abc import ABC, abstractmethod


class BakedFood(ABC):
    MINIMUM_PRICE = 0

    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    @abstractmethod
    def PORTION_SIZE(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= self.MINIMUM_PRICE:
            raise ValueError("Price cannot be less than or equal to zero!")
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"


if __name__ == "__main__":
    pass