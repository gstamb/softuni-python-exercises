from project import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, price: float, milliliters: float, caffeine: float):
        super().__init__(name, price, milliliters)
        self.caffeine = caffeine

    @property
    def caffeine(self) -> float:
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, caffeine: float):
        self.__caffeine = caffeine
