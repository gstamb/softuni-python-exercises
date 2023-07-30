from project.food.desert import Desert


class Cake(Desert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name: str, price: float, grams: float, calories: float):
        super().__init__(name, price, grams, calories)
