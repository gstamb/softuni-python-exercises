from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTest(TestCase):
    def test_initialization_params(self):
        vehicle = Vehicle(10.5, 10.5)
        self.assertEqual(vehicle.__class__.DEFAULT_FUEL_CONSUMPTION, 1.25)
        self.assertEqual(vehicle.fuel, 10.5)
        self.assertEqual(vehicle.horse_power, 10.5)
        self.assertEqual(vehicle.fuel_consumption, 1.25)

    def test_drive_with_less_fuel_than_needed(self):
        vehicle = Vehicle(10.5, 10.5)
        with self.assertRaises(Exception) as ex:
            vehicle.drive(8.5)
        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_with_enough_fuel(self):
        vehicle = Vehicle(10.5, 10.5)
        vehicle.drive(8.4)
        expected = 0
        result = vehicle.fuel
        self.assertEqual(expected, result)

    def test_refuel_exceeding_capacity(self):
        vehicle = Vehicle(10.5, 10.5)
        vehicle.drive(1)
        with self.assertRaises(Exception) as ex:
            vehicle.refuel(2)
        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel_within_capacity(self):
        vehicle = Vehicle(10.5, 10.5)
        vehicle.drive(8.4)
        vehicle.refuel(10)
        expected = 10
        result = vehicle.fuel
        self.assertEqual(expected, result)

    def test_string_representation(self):
        vehicle = Vehicle(10.5, 10.5)
        expected = f"The vehicle has 10.5 horse power with 10.5 fuel left and 1.25 fuel consumption"
        result = str(vehicle)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
