from project.drink.drink import Drink


class Tea(Drink):
    DRINK_COST = 2.5

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name=name, portion=portion, price=self.DRINK_COST, brand=brand)

    def __repr__(self):
        return Drink.__repr__(self)


if __name__ == "__main__":
    pass
