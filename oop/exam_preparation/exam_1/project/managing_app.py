from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.route import Route


def get_vehicle_obj(vehicle_type):
    if vehicle_type == "CargoVan":
        return CargoVan
    elif vehicle_type == "PassengerCar":
        return PassengerCar


class ManagingApp:
    def __init__(self):
        self.users = []
        self.users_lookup = {}
        self.vehicles = []
        self.vehicles_lookup = {}
        self.routes = []
        self.routes_lookup = {}

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if driving_license_number in self.users_lookup:
            return f"{driving_license_number} has already been registered to our platform."
        else:
            new_user = User(first_name, last_name, driving_license_number)
            self.users_lookup[driving_license_number] = len(self.users)
            self.users.append(new_user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ["PassengerCar", "CargoVan"]:
            return f"Vehicle type {vehicle_type} is inaccessible."
        if license_plate_number in self.vehicles_lookup:
            return f"{license_plate_number} belongs to another vehicle."

        get_vehicle = get_vehicle_obj(vehicle_type)
        register_vehicle = get_vehicle(brand, model, license_plate_number)
        self.vehicles_lookup[license_plate_number] = len(self.vehicles)
        self.vehicles.append(register_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        new_route = Route(start_point, end_point, length, len(self.routes) + 1)
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):

        user = self.users[self.users_lookup[driving_license_number]]
        vehicle = self.vehicles[self.vehicles_lookup[license_plate_number]]
        route_obj = self.routes[route_id - 1]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route_obj.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        vehicle.drive(route_obj.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):

        broken_vehicles = [x for x in self.vehicles if x.is_damaged][:count]

        repaired = 0
        for vehicle in sorted(broken_vehicles, key=lambda x: (x.brand, x.model)):
            if vehicle.is_damaged:
                vehicle.change_status()
                vehicle.recharge()
                repaired += 1

        return f"{len(broken_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        user_info = "*** E-Drive-Rent ***\n"
        for user in sorted(self.users, key=lambda x: -x.rating):
            user_info += f"{str(user)}\n"

        return user_info.strip()
