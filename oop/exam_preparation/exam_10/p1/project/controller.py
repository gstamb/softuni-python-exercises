from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __validate_object_exists(self, collection, key, value):
        """ Return an object by an attribute value. Raises an Exception if object does not exist """
        target_object = next((obj for obj in collection if getattr(obj, key) == value), None)
        if not target_object:
            object_type = "Driver" if collection is self.drivers else "Car" if collection is self.cars else "Race"
            raise Exception(f"{object_type} {value} could not be found!")
        return target_object

    def __validate_value_is_unique(self, collection, key, value):
        """ Raises an error if an object with a given attribute value already exists """
        if value in [getattr(obj, key) for obj in collection if getattr(obj, key) == value]:
            object_type = "Driver" if collection is self.drivers else "Car" if collection is self.cars else "Race"
            raise Exception(f"{object_type} {value} is already created!")

    def __find_vacant_cars_by_type(self, car_type):
        """ Returns a list of indexes for a desired type of car. Raises an Exception if no indexes are found. """
        car_index = [self.cars.index(car) for car in self.cars if
                     car.__class__.__name__ == car_type and car.is_taken is False]
        if not car_index or car_type not in self.VALID_CAR_TYPES:
            raise Exception(f"Car {car_type} could not be found!")
        return car_index

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.VALID_CAR_TYPES.keys():
            return
        self.__validate_value_is_unique(self.cars, "model", model)
        self.cars.append(self.VALID_CAR_TYPES[car_type](model, speed_limit))
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        self.__validate_value_is_unique(self.drivers, "name", driver_name)
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        self.__validate_value_is_unique(self.races, "name", race_name)
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        """
        Assigns the LIFO car to a driver.
        If the driver already has a car, that car is vacated and a new one is assigned.
        Else the target car is assigned to the driver.
        The car and the driver must exist else error is raised.
        """
        driver = self.__validate_object_exists(self.drivers, 'name', driver_name)
        car_index = self.__find_vacant_cars_by_type(car_type)

        available_car = self.cars[car_index[-1]]
        available_car.is_taken = True

        if driver.car:
            old_model = driver.car
            old_model.is_taken = False
            driver.car = available_car
            return f"Driver {driver_name} changed his car from {old_model.model} to {available_car.model}."
        else:
            driver.car = available_car
            return f"Driver {driver_name} chose the car {available_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        """
        Adds a driver to a race.
        Both driver and race must exist.
        Driver must have a car to participate and not to have entered the race already.
        """
        race = self.__validate_object_exists(self.races, 'name', race_name)
        driver = self.__validate_object_exists(self.drivers, 'name', driver_name)

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        """
        Starts a race. There must be a valid race with minimum 3 registered participants.
        Top 3 drivers with the highest vehicle speed limit are considered winners and are rewarded points.
         """
        race = self.__validate_object_exists(self.races, 'name', race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_drivers = [x for x in sorted(race.drivers, key=lambda x: -x.car.speed_limit)][:3]
        race_summary = ""
        for driver in fastest_drivers:
            race_summary += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"
            driver.record_winning_race()
        return race_summary.strip()


if __name__ == "__main__":
    pass
