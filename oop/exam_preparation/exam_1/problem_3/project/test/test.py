from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):

    def setUp(self) -> None:
        self.robot = Robot("Hash123", "Entertainment", 32, 2000.0)

    def test_valid_initialization(self):
        self.assertEqual("Hash123", self.robot.robot_id)
        self.assertEqual("Entertainment", self.robot.category)
        self.assertEqual(32, self.robot.available_capacity)
        self.assertEqual(2000.0, self.robot.price)

    def test_invalid_initialization_unavailable_category(self):
        with self.assertRaises(ValueError) as ex:
            Robot("Hash123", "Test", 32, 2000.0)
        self.assertEqual(f"Category should be one of '{Robot.ALLOWED_CATEGORIES}'", str(ex.exception))

    def test_invalid_initialization_negative_price(self):
        with self.assertRaises(ValueError) as ex:
            Robot("Hash123", "Entertainment", 32, -1)
        self.assertEqual("Price cannot be negative!", str(ex.exception))

    def test_attempting_to_upgrade_an_existing_upgrade(self):
        self.robot.upgrade("Party Hat", 5.0)
        result = self.robot.upgrade("Party Hat", 5.0)
        expected = f"Robot {self.robot.robot_id} was not upgraded."
        self.assertEqual(expected, result)

    def test_upgrade_robot_component(self):
        component = "Party Hat"
        result = self.robot.upgrade(component, 5.0)
        expected = f'Robot {self.robot.robot_id} was upgraded with {component}.'
        self.assertEqual(expected, result)
        self.assertEqual([component], self.robot.hardware_upgrades)
        self.assertEqual(2007.5, self.robot.price)

    def test_update_valid_parameters(self):
        result = self.robot.update(3, 25)
        expected = f'Robot {self.robot.robot_id} was updated to version {3}.'
        self.assertEqual(expected, result)

    def test_update_with_lower_level_system(self):
        self.robot.update(3, 31)
        result = self.robot.update(2, 31)
        expected = f"Robot {self.robot.robot_id} was not updated."
        self.assertEqual(expected, result)

    def test_update_with_an_existing_update(self):
        version_first = 2
        self.robot.update(version_first, 1)
        version_second = 3
        result = self.robot.update(version_second, 1)
        expected = f'Robot {self.robot.robot_id} was updated to version {version_second}.'
        self.assertEqual(expected, result)

    def test_compare_prices_robot_one_more_expensive(self):
        second_robot = Robot("Hash", "Entertainment", 32, 1900.0)
        result = self.robot > second_robot
        expected = f'Robot with ID {self.robot.robot_id} is more expensive than Robot with ID {second_robot.robot_id}.'
        self.assertEqual(expected, result)

    def test_compare_prices_robot_one_equals_price_robot_two(self):
        second_robot = Robot("Hash", "Entertainment", 32, 2000.0)
        result = self.robot > second_robot
        expected = f'Robot with ID {self.robot.robot_id} costs equal to Robot with ID {second_robot.robot_id}.'
        self.assertEqual(expected, result)

    def test_compare_prices_robot_two_more_expensive_robot_one(self):
        second_robot = Robot("Hash", "Entertainment", 32, 2200.0)
        result = self.robot > second_robot
        expected = f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {second_robot.robot_id}.'
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()

