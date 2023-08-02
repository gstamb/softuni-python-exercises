from project import Dough
from project import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        condition = True if name is None else bool(name.strip())
        if not condition:
            raise ValueError("The name cannot be an empty string")
        else:
            self.__name = name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, dough):
        if dough is None:
            raise ValueError("You should add dough to the pizza")
        else:
            self.__dough = dough

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, max_number_of_toppings):
        if max_number_of_toppings <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        else:
            self.__max_number_of_toppings = max_number_of_toppings

    def add_topping(self, topping: Topping):
        if self.max_number_of_toppings == len(self.toppings.keys()):
            raise ValueError("Not enough space for another topping")

        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        dough_weight = self.dough.weight
        topping_weight = sum(self.toppings.values())
        total_weight = dough_weight + topping_weight
        return total_weight
