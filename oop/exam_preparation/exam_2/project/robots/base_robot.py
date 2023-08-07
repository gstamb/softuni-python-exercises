from abc import ABC, abstractmethod


class BaseRobot(ABC):

    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip():
            self.__name = value
        else:
            raise ValueError("Robot name cannot be empty!")

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        if value.strip():
            self.__kind = value
        else:
            raise ValueError("Robot kind cannot be empty!")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")

    @abstractmethod
    def eating(self):
        pass

