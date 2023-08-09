from abc import ABC, abstractmethod


class Booth(ABC):
    INVALID_CAPACITY = 0  # or less
    BOOTH_TYPE = "Booth"

    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= self.INVALID_CAPACITY:
            raise ValueError("Capacity cannot be a negative number!")
        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people: int):
        pass

    def calculate_bill(self):
        if self.delicacy_orders:
            orders_value = sum([order.price for order in self.delicacy_orders])
            reservation_value = self.price_for_reservation
            bill = orders_value + reservation_value
            return bill
        return 0

    def free_booth(self):
        self.delicacy_orders.clear()
        self.price_for_reservation = 0
        self.is_reserved = False


if __name__ == "__main__":
    pass
