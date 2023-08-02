from project import Customer
from project import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []
        self.customers_lookup = {}
        self.dvd_lookup = {}

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def valid_customer_id(self, dvd_id):
        return dvd_id in self.customers_lookup

    def valid_dvd_id(self, dvd_id):
        return dvd_id in self.dvd_lookup

    def add_customer(self, customer: Customer):
        num_customers = len(self.customers)
        if num_customers < MovieWorld.customer_capacity():
            self.customers.append(customer)
            self.customers_lookup[customer.id] = len(self.customers) - 1

    def add_dvd(self, dvd: DVD):
        current_dvds = len(self.dvds)
        if current_dvds < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)
            self.dvd_lookup[dvd.id] = len(self.dvds) - 1

    def rent_dvd(self, customer_id: int, dvd_id: int):
        if self.valid_customer_id(customer_id) and self.valid_dvd_id(dvd_id):

            customer_object = self.customers[self.customers_lookup[customer_id]]
            dvd_object = self.dvds[self.dvd_lookup[dvd_id]]

            if dvd_id in [dvd.id for dvd in customer_object.rented_dvds]:
                return f"{customer_object.name} has already rented {dvd_object.name}"
            elif dvd_object.is_rented:
                return "DVD is already rented"
            elif customer_object.age < dvd_object.age_restriction:
                return f"{customer_object.name} should be at least {dvd_object.age_restriction} to rent this movie"
            else:
                customer_object.rented_dvds.append(dvd_object)
                dvd_object.is_rented = True
                return f"{customer_object.name} has successfully rented {dvd_object.name}"
        return "Invalid customer ID or DVD ID"

    def return_dvd(self, customer_id: int, dvd_id: int):
        if self.valid_customer_id(customer_id) and self.valid_dvd_id(dvd_id):

            customer_object = self.customers[self.customers_lookup[customer_id]]
            dvd_object = self.dvds[self.dvd_lookup[dvd_id]]

            if dvd_id in [dvd.id for dvd in customer_object.rented_dvds]:
                customer_object.rented_dvds.remove(dvd_object)
                dvd_object.is_rented = False
                return f"{customer_object.name} has successfully returned {dvd_object.name}"
            else:
                return f"{customer_object.name} does not have that DVD"

        return "Invalid customer ID or DVD ID"

    def __repr__(self):
        return_info = ""
        for index, customer in enumerate(self.customers):
            return_info += f"{customer}\n"

        for index, dvd in enumerate(self.dvds):
            return_info += f"{dvd}\n"
        return return_info


movie_world = MovieWorld("Test")
for _ in range(16):
    movie_world.add_dvd(DVD("A", 1, 1254, "February", 10))
