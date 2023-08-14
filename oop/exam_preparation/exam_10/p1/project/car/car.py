from abc import ABC, abstractmethod


class Car(ABC):
    MODEL_MINIMUM_LENGTH = 4
    MIN_SPEED_LIMIT = 0
    MAX_SPEED_LIMIT = 0

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < self.MODEL_MINIMUM_LENGTH:
            raise ValueError(f"Model {value} is less than {self.MODEL_MINIMUM_LENGTH} symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not self.MIN_SPEED_LIMIT <= value <= self.MAX_SPEED_LIMIT:
            raise ValueError(f"Invalid speed limit! Must be between {self.MIN_SPEED_LIMIT} and {self.MAX_SPEED_LIMIT}!")
        self.__speed_limit = value

    @abstractmethod
    def __str__(self):
        pass

if __name__ == "__main__":
    pass
