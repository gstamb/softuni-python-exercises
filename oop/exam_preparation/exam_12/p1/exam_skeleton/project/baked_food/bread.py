from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):

    def __init__(self, name: str, price: float):
        super().__init__(name=name, price=price, portion=self.PORTION_SIZE)

    @property
    def PORTION_SIZE(self):
        return 200


if __name__ == "__main__":
    pass
