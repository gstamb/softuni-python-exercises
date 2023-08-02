from project import Food


class MainDish(Food):
    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price, grams)


