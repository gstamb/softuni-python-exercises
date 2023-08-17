from project.drink.drink import Drink


class Water(Drink):
 
    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name=name, portion=portion, price=self.DRINK_COST, brand=brand)

    def __repr__(self):
        return Drink.__repr__(self)

    @property
    def DRINK_COST(self):
        return 1.5


if __name__ == "__main__":
    pass
