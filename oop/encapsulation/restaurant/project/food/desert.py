from project import Food


class Desert(Food):
    def __init__(self, name: str, price: float, grams: float, calories: float):
        super().__init__(name, price, grams)
        self.calories = calories

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, calories):
        self.__calories = calories
