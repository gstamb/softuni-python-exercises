from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.route import Route


class ManagingApp:
    AVAILABLE_SERVICES = {"CargoVan": CargoVan, "PassengerCar": PassengerCar}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if self._check_existing_registration(driving_license_number, self.users, "driving_license_number"):
            return f"{driving_license_number} has already been registered to our platform."
        else:
            new_user = User(first_name, last_name, driving_license_number)
            self.users.append(new_user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if not self.AVAILABLE_SERVICES.get(vehicle_type, None):
            return f"Vehicle type {vehicle_type} is inaccessible."
        if self._check_existing_registration(license_plate_number, self.vehicles, "license_plate_number"):
            return f"{license_plate_number} belongs to another vehicle."

        get_vehicle = self.AVAILABLE_SERVICES[vehicle_type]
        register_vehicle = get_vehicle(brand, model, license_plate_number)
        self.vehicles.append(register_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            elif route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

        new_route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = self._get_object_by_attribute(self.users, "driving_license_number", driving_license_number)
        vehicle = self._get_object_by_attribute(self.vehicles, "license_plate_number", license_plate_number)
        route_obj = self._get_object_by_attribute(self.routes, "route_id", route_id)

        trip_not_possible = self._should_cancel_trip(user, vehicle, route_obj, driving_license_number,
                                                     license_plate_number, route_id)
        if trip_not_possible:
            return trip_not_possible
        else:
            vehicle.drive(route_obj.length)
            self._process_trip_outcome(user, vehicle, is_accident_happened)
            return str(vehicle)

    def repair_vehicles(self, count: int):
        broken_vehicles = sorted([x for x in self.vehicles if x.is_damaged], key=lambda x: (x.brand, x.model))

        for vehicle in broken_vehicles[:count]:
            vehicle.change_status()
            vehicle.recharge()

        return f"{min(count, len(broken_vehicles))} vehicles were successfully repaired!"

    def users_report(self):
        user_info = "*** E-Drive-Rent ***\n"
        for user in sorted(self.users, key=lambda x: -x.rating):
            user_info += f"{str(user)}\n"

        return user_info.strip()

    @staticmethod
    def _get_object_by_attribute(collection, key, value):
        return next((obj for obj in collection if getattr(obj, key) == value), None)

    @staticmethod
    def _check_existing_registration(value, collection, attribute_name):
        return any(getattr(x, attribute_name, None) == value for x in collection)

    @staticmethod
    def _process_trip_outcome(user, vehicle, is_accident_happened):
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

    @staticmethod
    def _should_cancel_trip(user, vehicle, route_obj, driving_license_number, license_plate_number, route_id):
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route_obj.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        return False


if __name__ == "__main__":
    pass
