from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    PORTION_SIZE = 200

    def __init__(self, name: str, price: float):
        super().__init__(name=name, price=price, portion=self.PORTION_SIZE)

    def __repr__(self):
        return BakedFood.__repr__(self)


if __name__ == "__main__":
    pass
