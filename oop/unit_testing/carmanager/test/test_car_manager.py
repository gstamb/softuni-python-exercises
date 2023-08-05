from unittest import TestCase, main
from carmanager.car_manager import Car


class CarTest(TestCase):
    def test_initialization_valid_params(self):
        test_car = Car("a", "b", 1, 4)
        self.assertEqual(test_car.make, "a")
        self.assertEqual(test_car.model, "b")
        self.assertEqual(test_car.fuel_consumption, 1)
        self.assertEqual(test_car.fuel_capacity, 4)
        self.assertEqual(test_car.fuel_amount, 0)

    def test_initialization_wrong_make_param(self):
        with self.assertRaises(Exception) as ex:
            Car(None, "b", 1, 4)
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_initialization_empty_make_param(self):
        with self.assertRaises(Exception) as ex:
            Car("", "b", 1, 4)
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_initialization_wrong_model_param(self):
        with self.assertRaises(Exception) as ex:
            Car("a", None, 1, 4)
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_initialization_empty_model_param(self):
        with self.assertRaises(Exception) as ex:
            Car("a", "", 1, 4)
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_initialization_negative_fuel_consumption_param(self):
        with self.assertRaises(Exception) as ex:
            Car("a", "b", -11, 4)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_initialization_zero_fuel_consumption_param(self):
        with self.assertRaises(Exception) as ex:
            Car("a", "b", 0, 4)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_initialization_negative_fuel_capacity_param(self):
        with self.assertRaises(Exception) as ex:
            Car("a", "b", 1, -11)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_initialization_zero_fuel_capacity_param(self):
        with self.assertRaises(Exception) as ex:
            Car("a", "b", 1, 0)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_setting_negative_fuel_amount_param(self):
        test_car = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            test_car.fuel_amount = -1
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_setting_zero_fuel_amount_param(self):
        test_car = Car("a", "b", 1, 4)
        test_car.fuel_amount = 0
        result = test_car.fuel_amount
        expected = 0
        self.assertEqual(result, expected)

    def test_refuel_function_with_valid_fuel_above_capacity(self):
        test_car = Car("a", "b", 1, 4)
        test_car.refuel(5)
        result = test_car.fuel_amount
        expected = 4
        self.assertEqual(result, expected)

    def test_refuel_function_with_valid_fuel_below_capacity(self):
        test_car = Car("a", "b", 1, 4)
        test_car.refuel(2)
        result = test_car.fuel_amount
        expected = 2
        self.assertEqual(result, expected)

    def test_refuel_function_with_zerofuel(self):
        test_car = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            test_car.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_drive_distance_larger_than_fuel(self):
        test_car = Car("a", "b", 1, 4)
        test_car.fuel_amount = 1
        with self.assertRaises(Exception) as ex:
            test_car.drive(1000)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive_distance_sufficient_fuel(self):
        test_car = Car("a", "b", 1, 4)
        test_car.fuel_amount = 1000
        test_car.drive(100)
        result = test_car.fuel_amount
        expected = 999
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()
