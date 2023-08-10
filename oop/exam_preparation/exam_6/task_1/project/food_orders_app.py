from project.meals.starter import Starter
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.client import Client
import itertools


class FoodOrdersApp:
    ORDER_ID_GENERATOR = itertools.count(1).__next__

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.meal_lookup = {}

    def _validate_menu_is_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def _validate_client_exists(self, client_phone_number):
        if client_phone_number in [getattr(client, "phone_number") for client in self.clients_list]:
            return True
        return False

    def _get_client_obj(self, client_phone_number):
        return next(
            (client for client in self.clients_list if getattr(client, 'phone_number', None) == client_phone_number),
            None)

    def register_client(self, client_phone_number: str):
        if self._validate_client_exists(client_phone_number):
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client.phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in {"Starter", "MainDish", "Dessert"}:
                self.meal_lookup[meal.name] = len(self.menu)
                self.menu.append(meal)

    def show_menu(self):
        self._validate_menu_is_ready()
        return "\n".join([meal.details() for meal in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self._validate_menu_is_ready()

        if not self._validate_client_exists(client_phone_number):
            self.register_client(client_phone_number)

        for meal, quantity in meal_names_and_quantities.items():
            if meal not in self.meal_lookup:
                raise Exception(f"{meal} is not on the menu!")
            else:
                menu_obj = self.menu[self.meal_lookup[meal]]
                if quantity > menu_obj.quantity:
                    raise Exception(f"Not enough quantity of {menu_obj.__class__.__name__}: {meal}!")

        client = self._get_client_obj(client_phone_number)

        for meal, quantity in meal_names_and_quantities.items():
            menu_obj = self.menu[self.meal_lookup[meal]]
            menu_obj.quantity -= quantity
            client.shopping_cart.append(menu_obj)
            if meal not in client.meal_quantity:
                client.meal_quantity[meal] = 0
            client.meal_quantity[meal] += quantity
            client.bill += menu_obj.price * quantity

        return f"Client {client.phone_number} successfully " \
               f"ordered {', '.join([meal.name for meal in client.shopping_cart])} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self._get_client_obj(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal, quantity in client.meal_quantity.items():
            self.menu[self.meal_lookup[meal]].quantity += quantity

        client.meal_quantity = dict()
        client.shopping_cart.clear()
        client.bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self._get_client_obj(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        order_total = client.bill
        client.meal_quantity = dict()
        client.shopping_cart.clear()
        client.bill = 0
        return f"Receipt #{self.ORDER_ID_GENERATOR()} with total amount of {order_total:.2f} " \
               f"was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


if __name__ == "__main__":
    pass
