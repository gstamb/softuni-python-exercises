from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    """ Facade pattern for the Food, Drink and Table classes """
    VALID_FOOD = {"Cake": Cake, "Bread": Bread}
    VALID_DRINKS = {"Tea": Tea, "Water": Water}
    VALID_TABLE_TYPES = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = []
        self.running_total = 0
        self.available_tables = {}
        self.available_foods = {}
        self.available_drinks = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def __validate_unique_obj_attribute(self, object_type, identifier):
        if object_type in self.VALID_FOOD:
            if identifier in self.available_foods:
                raise Exception(f"{object_type} {identifier} is already in the menu!")
        elif object_type in self.VALID_DRINKS:
            if identifier in self.available_drinks:
                raise Exception(f"{object_type} {identifier} is already in the menu!")
        elif object_type in self.VALID_TABLE_TYPES:
            if identifier in self.available_tables:
                raise Exception(f"Table {identifier} is already in the bakery!")

    @staticmethod
    def __add_object_to_bakery(collection, validator, item_type, *args):
        """ Creates food , drink or table objects and append it to the corresponding attribute"""
        new_object = validator[item_type](*args)
        collection.append(new_object)
        return new_object

    def __fetch_table_by_key(self, key, value):
        return next(
            (table for table in self.tables_repository if getattr(table, key) >= value), None)

    def __process_order(self, food_or_drink, table_number, *args) -> str:
        """ Orders received as string are appended to the corresponding table.
            food_or_drink = collection either available_foods or available_drinks
            table_number = table identification where order is placed
            args = food or drink item names
            returns a string containing successfully ordered and unavailable items.
        """
        if table_number not in self.available_tables:
            return f"Could not find table {table_number}"
        ordered_items = list(args)
        order_info = f"Table {table_number} ordered:\n"
        for ordered_item in args:
            if ordered_item in food_or_drink:
                if food_or_drink is self.available_foods:
                    self.available_tables[table_number].order_food(food_or_drink[ordered_item])
                elif food_or_drink is self.available_drinks:
                    self.available_tables[table_number].order_drink(food_or_drink[ordered_item])
                ordered_items.remove(ordered_item)
                order_info += f"- {food_or_drink[ordered_item].name}: {food_or_drink[ordered_item].portion}g - " \
                              f"{food_or_drink[ordered_item].price}lv\n"

        if ordered_items:
            order_info += f"{self.name} does not have in the menu:\n"
            for unavailable in ordered_items:
                order_info += f"{unavailable}\n"

        return order_info.strip()

    def add_food(self, food_type: str, name: str, price: float):
        self.__validate_unique_obj_attribute(food_type, name)
        new_food_item = self.__add_object_to_bakery(self.food_menu, self.VALID_FOOD, food_type, name, price)
        self.available_foods[name] = new_food_item
        return f"Added {name} ({new_food_item.__class__.__name__}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        self.__validate_unique_obj_attribute(drink_type, name)
        new_drink_item = self.__add_object_to_bakery(self.drinks_menu, self.VALID_DRINKS, drink_type, name, portion,
                                                     brand)
        self.available_drinks[name] = new_drink_item
        return f"Added {name} ({new_drink_item.__class__.__name__}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        self.__validate_unique_obj_attribute(table_type, table_number)
        new_table = self.__add_object_to_bakery(self.tables_repository, self.VALID_TABLE_TYPES, table_type,
                                                table_number, capacity)

        self.available_tables[table_number] = new_table
        return f"Added table number {new_table.table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table_with_sufficient_capacity = self.__fetch_table_by_key("capacity", number_of_people)
        if not table_with_sufficient_capacity:
            return f"No available table for {number_of_people} people"
        table_with_sufficient_capacity.reserve(number_of_people)
        return f"Table {table_with_sufficient_capacity.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        return self.__process_order(self.available_foods, table_number, *args)

    def order_drink(self, table_number: int, *args):
        return self.__process_order(self.available_drinks, table_number, *args)

    def leave_table(self, table_number: int):
        target_table = self.available_tables[table_number]
        bill = target_table.get_bill()
        target_table.clear()
        self.total_income.append(bill)
        self.running_total += bill
        return f"Table: {target_table.table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        free_tables = ""
        for table in self.tables_repository:
            free_tables += f"{table.free_table_info()}\n"

        return free_tables.strip()

    def get_total_income(self):
        return f"Total income: {self.running_total:.2f}lv"


if __name__ == "__main__":
    pass
