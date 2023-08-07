from abc import ABC, abstractmethod


class BaseRobot(ABC):
    ERR_MSG_ROBOT_NAME = "Robot name cannot be empty!"
    ERR_MSG_ROBOT_KIND = "Robot kind cannot be empty!"
    ERR_MSG_ROBOT_PRICE = "Robot price cannot be less than or equal to 0.0!"
    min_value_price = 0

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
            raise ValueError(self.ERR_MSG_ROBOT_NAME)

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        if value.strip():
            self.__kind = value
        else:
            raise ValueError(self.ERR_MSG_ROBOT_KIND)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > self.min_value_price:
            self.__price = value
        else:
            raise ValueError(self.ERR_MSG_ROBOT_PRICE)

    @abstractmethod
    def eating(self):
        pass


if __name__ == "__main__":
    pass
