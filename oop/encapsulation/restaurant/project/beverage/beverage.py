from project.product import Product


class Beverage(Product):
    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price)
        self.milliliters = milliliters

    @property
    def milliliters(self) -> float:
        return self.__milliliters

    @milliliters.setter
    def milliliters(self, milliliters: float):
        self.__milliliters = milliliters
