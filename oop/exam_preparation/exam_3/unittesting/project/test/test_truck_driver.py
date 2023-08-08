from unittest import TestCase
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self):
        self.driver = TruckDriver("Pesho", 1.40)

    def test_init_obj_valid_params(self):
        self.assertEqual(self.driver.name, "Pesho")
        self.assertEqual(self.driver.money_per_mile, 1.4)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0.0)
        self.assertEqual(self.driver.miles, 0)

    def test_init_invalid_money_go_negative(self):
        with self.assertRaises(ValueError) as ex:
            driver = TruckDriver("Pesho", 0)
            town = "Sofia"
            miles = 1500
            driver.add_cargo_offer(town, miles)
            driver.drive_best_cargo_offer()
        self.assertEqual("Pesho went bankrupt.", str(ex.exception))

    def test_money_earned_turning_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.earned_money -= 1
        self.assertEqual("Pesho went bankrupt.", str(ex.exception))

    def test_cargo_offer_invalid_params(self):
        self.driver.add_cargo_offer("Sofia", 12)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 12)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_valid_cargo_offer(self):
        result = self.driver.add_cargo_offer("Sofia", 12)
        expected = "Cargo for 12 to Sofia was added as an offer."
        self.assertEqual(result, expected)

    def test_valid_cargo_offer_dict_data(self):
        self.driver.add_cargo_offer("Sofia", 12)
        result = self.driver.available_cargos
        expected = {"Sofia": 12}
        self.assertEqual(result, expected)

    def test_picking_offer_with_greatest_distance(self):
        self.driver.add_cargo_offer("Sofia", 12)
        self.driver.add_cargo_offer("Bourgas", 15)
        self.driver.add_cargo_offer("Varna", 13)
        result = self.driver.drive_best_cargo_offer()
        expected = "Pesho is driving 15 to Bourgas."
        self.assertEqual(result, expected)

    def test_drive_best_cargo_offer_with_no_offers(self):
        result = self.driver.drive_best_cargo_offer()
        expected = "There are no offers available."
        self.assertEqual(expected, result)

    def test_drive_best_cargo_offer_valid_offers(self):
        self.driver.add_cargo_offer("Sofia", 12)
        result = self.driver.drive_best_cargo_offer()
        expected = "Pesho is driving 12 to Sofia."
        self.assertEqual(expected, result)
        self.assertEqual(self.driver.miles, 12)
        self.assertEqual(self.driver.earned_money, 12 * self.driver.money_per_mile)

    def test_drive_cargo_and_incur_expenses(self):
        town = "Sofia"
        miles = 1500
        self.driver.add_cargo_offer(town, miles)
        money_earned = 1500 * self.driver.money_per_mile
        expenses_eat = 1500 // 250 * -20
        expenses_sleep = -45
        expenses_pump_gas = -500
        self.driver.drive_best_cargo_offer()
        expected = money_earned + expenses_eat + expenses_sleep + expenses_pump_gas
        result = self.driver.earned_money
        self.assertEqual(expected, result)

    def test_drive_cargo_and_incur_expenses_max_distance(self):
        town = "Sofia"
        miles = 10000
        self.driver.add_cargo_offer(town, miles)
        money_earned = miles * self.driver.money_per_mile
        expenses_eat = miles // 250 * -20
        expenses_sleep = miles // 1000 * -45
        expenses_pump_gas = miles // 1500 * -500
        expenses_repair_truck = miles // 10000 * -7500
        self.driver.drive_best_cargo_offer()
        expected = money_earned + expenses_eat + expenses_sleep + expenses_pump_gas + expenses_repair_truck
        result = self.driver.earned_money
        self.assertEqual(expected, result)

    def test_string_rep(self):
        town = "Sofia"
        miles = 1500
        self.driver.add_cargo_offer(town, miles)
        self.driver.drive_best_cargo_offer()
        result = str(self.driver)
        expect = "Pesho has 1500 miles behind his back."
        self.assertEqual(result, expect)

    def test_expense_functions_eat(self):
        self.driver.earned_money = 1000
        self.driver.eat(250)
        expect = 980
        result = self.driver.earned_money
        self.assertEqual(expect, result)

    def test_expense_functions_sleep(self):
        self.driver.earned_money = 1000
        self.driver.sleep(1000)
        expect = 955
        result = self.driver.earned_money
        self.assertEqual(expect, result)

    def test_expense_functions_pump_gas(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(1500)
        expect = 500
        result = self.driver.earned_money
        self.assertEqual(expect, result)

    def test_expense_functions_repair_truck(self):
        self.driver.earned_money = 10000
        self.driver.repair_truck(10000)
        expect = 2500
        result = self.driver.earned_money
        self.assertEqual(expect, result)


if __name__ == "__main__":
    pass
