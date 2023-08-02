from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):
    EXTRA_WEIGHT_PER_FEED = 0.10
    CAN_FEED_ON = (Vegetable, Fruit)

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    EXTRA_WEIGHT_PER_FEED = 0.40
    CAN_FEED_ON = (Meat,)

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    EXTRA_WEIGHT_PER_FEED = 0.30
    CAN_FEED_ON = (Meat, Vegetable)

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    EXTRA_WEIGHT_PER_FEED = 1.00
    CAN_FEED_ON = (Meat,)

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "ROAR!!!"
