from abc import ABC, abstractmethod


class Drink(ABC):
    DRINK_COST = 0

    def __init__(self, name: str, portion: float, price: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @abstractmethod
    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"


if __name__ == "__main__":
    pass
