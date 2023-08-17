from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    @property
    def PORTION_SIZE(self):
        return 245

    def __init__(self, name: str, price: float):
        super().__init__(name=name, price=price, portion=self.PORTION_SIZE)


if __name__ == "__main__":
    pass
