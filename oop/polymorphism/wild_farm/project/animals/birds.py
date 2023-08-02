from project.animals.animal import Bird
from project.food import Meat, Fruit, Vegetable, Seed


class Owl(Bird):
    EXTRA_WEIGHT_PER_FEED = 0.25
    CAN_FEED_ON = (Meat,)

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    EXTRA_WEIGHT_PER_FEED = 0.35
    CAN_FEED_ON = (Meat, Vegetable, Fruit, Seed)

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Cluck"
