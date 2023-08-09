from project.booths.private_booth import PrivateBooth
from project.booths.open_booth import OpenBooth
from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread
from project.booths.booth import Booth


class ChristmasPastryShopApp:
    VALID_DELICACIES_OBJ_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTH_OBJ_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0
        self.existing_delicacies = set()
        self.existing_booth_numbers = set()

    # Helper methods
    @staticmethod
    def _find_obj_by_attr_value(collection, key, value):
        return next((obj for obj in collection if getattr(obj, key, None) == value), None)

    @staticmethod
    def _find_booth_with_sufficient_capacity(collection, key, value):
        return next((obj for obj in collection if getattr(obj, key, None) >= value and obj.is_reserved is False), None)

    def _validate_add_delicacy(self, name, type_delicacy):
        if name in self.existing_delicacies:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.VALID_DELICACIES_OBJ_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

    def _validate_order_delicacy(self, booth_number, delicacy_name):
        if booth_number not in self.existing_booth_numbers:
            raise Exception(f"Could not find booth {booth_number}!")
        if delicacy_name not in self.existing_delicacies:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

    def _validate_add_booth(self, booth_number, type_booth):
        if booth_number in self.existing_booth_numbers:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.VALID_BOOTH_OBJ_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        self._validate_add_delicacy(name, type_delicacy)

        fetched_delicacy_obj = self.VALID_DELICACIES_OBJ_TYPES[type_delicacy]
        created_new_delicacy = fetched_delicacy_obj(name, price)
        self.existing_delicacies.add(name)
        self.delicacies.append(created_new_delicacy)
        return f"Added delicacy {created_new_delicacy.name} - {created_new_delicacy.TYPE_DELICACY} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        self._validate_add_booth(booth_number, type_booth)

        fetched_booth_obj = self.VALID_BOOTH_OBJ_TYPES[type_booth]
        created_new_booth = fetched_booth_obj(booth_number, capacity)
        self.existing_booth_numbers.add(booth_number)
        self.booths.append(created_new_booth)
        return f"Added booth number {created_new_booth.booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth_sufficient_capacity = self._find_booth_with_sufficient_capacity(self.booths, 'capacity', number_of_people)
        if not booth_sufficient_capacity:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth_sufficient_capacity.reserve(number_of_people)
        return f"Booth {booth_sufficient_capacity.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        self._validate_order_delicacy(booth_number, delicacy_name)

        fetch_booth = self._find_obj_by_attr_value(self.booths, 'booth_number', booth_number)
        fetch_delicacy = self._find_obj_by_attr_value(self.delicacies, 'name', delicacy_name)
        fetch_booth.delicacy_orders.append(fetch_delicacy)
        return f"Booth {fetch_booth.booth_number} ordered {fetch_delicacy.name}."

    def leave_booth(self, booth_number: int):
        fetch_booth = self._find_obj_by_attr_value(self.booths, "booth_number", booth_number)
        bill = fetch_booth.calculate_bill()
        self.income += bill
        fetch_booth.free_booth()
        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."


if __name__ == "__main__":
    pass
