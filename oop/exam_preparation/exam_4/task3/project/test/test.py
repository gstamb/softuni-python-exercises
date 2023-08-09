from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class SecondHandCarTest(TestCase):
    def setUp(self) -> None:
        self.shc = SecondHandCar("Trabant", "Cabriolet", 1000, 300)

    def test_initialization_valid_params(self):
        self.assertEqual("Trabant", self.shc.model)
        self.assertEqual("Cabriolet", self.shc.car_type)
        self.assertEqual(1000, self.shc.mileage)
        self.assertEqual(300, self.shc.price)

    def test_initializing_price_too_low(self):
        with self.assertRaises(ValueError) as err:
            SecondHandCar("Trabant", "Cabriolet", 1000, 0)
        self.assertEqual("Price should be greater than 1.0!", str(err.exception))

    def test_setting_price_too_low(self):
        with self.assertRaises(ValueError) as err:
            self.shc.price = 0
        self.assertEqual("Price should be greater than 1.0!", str(err.exception))

    def test_initializing_mileage_too_low(self):
        with self.assertRaises(ValueError) as err:
            SecondHandCar("Trabant", "Cabriolet", 50, 300)
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(err.exception))

    def test_changing_price_to_value_too_low(self):
        with self.assertRaises(ValueError) as err:
            self.shc.mileage = 50
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(err.exception))

    def test_increasing_price_on_promotion(self):
        with self.assertRaises(ValueError) as err:
            self.shc.set_promotional_price(400)
        self.assertEqual("You are supposed to decrease the price!", str(err.exception))

    def test_decreasing_price_on_promotion(self):
        result = self.shc.set_promotional_price(200)
        expected = "The promotional price has been successfully set."
        self.assertEqual(expected, result)
        self.assertEqual(self.shc.price, 200)

    def test_car_repair_cost_exceed_half_cars_value(self):
        result = self.shc.need_repair(600, "Change front window")
        expected = 'Repair is impossible!'
        self.assertEqual(expected, result)

    def test_car_repair_cost_not_exceed_half_cars_value(self):
        result = self.shc.need_repair(100, "Change front window")
        expected = "Price has been increased due to repair charges."
        self.assertEqual(expected, result)
        self.assertEqual(400, self.shc.price)
        self.assertEqual(["Change front window"], self.shc.repairs)

    def test_gt_comparison_between_car_objects_same_type(self):
        test_car2 = SecondHandCar("Zaporozhiec", "Cabriolet", 5000, 400)
        result = self.shc > test_car2
        expected = False
        self.assertEqual(expected, result)

    def test_gt_comparison_between_car_objects_different_type(self):
        test_car2 = SecondHandCar("Zaporozhiec", "Covertable", 5000, 400)
        result = self.shc > test_car2
        expected = 'Cars cannot be compared. Type mismatch!'
        self.assertEqual(expected, result)

    def test_car_string_representation(self):
        result = str(self.shc)
        model = "Trabant"
        car_type = "Cabriolet"
        mileage = 1000
        price = 300
        repairs = []
        expected = f"Model {model} | Type {car_type} | Milage {mileage}km\n" \
                   f"Current price: {price:.2f} | Number of Repairs: {len(repairs)}"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    pass
