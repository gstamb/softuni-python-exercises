from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @staticmethod
    def make_sound():
        pass

    def feed(self, food):
        if isinstance(food, getattr(self.__class__, "CAN_FEED_ON")):
            self.food_eaten += food.quantity
            self.weight += getattr(self.__class__, "EXTRA_WEIGHT_PER_FEED") * food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Bird(Animal):
    @abstractmethod
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    @staticmethod
    def make_sound():
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, " \
               f"{self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    @abstractmethod
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    @staticmethod
    def make_sound():
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, " \
               f"{self.weight}, {self.living_region}, {self.food_eaten}]"
