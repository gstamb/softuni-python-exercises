class Vehicle:
    def __init__(self, variety: str, model: str, price: int):
        self.type = variety
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if self.owner is None:
            if money >= self.price:
                change = money - self.price
                self.owner = owner
                return f"Successfully bought a {self.type}. Change: {change:.2f}"
            else:
                return "Sorry, not enough money"
        else:
            return "Car already sold"

    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"
        else:
            self.owner = None

    def __repr__(self):
        if self.owner is None:
            return f"{self.model} {self.type} is on sale: {self.price}"
        else:
            return f"{self.model} {self.type} is owned by: {self.owner}"

vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type,
model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)

