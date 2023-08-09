from unittest import TestCase, main
from project.toy_store import ToyStore


class ToyStoreTest(TestCase):
    def setUp(self) -> None:
        self.toy = ToyStore()

    def test_initialization(self):
        self.assertEqual(self.toy.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_not_in_shelf_keys(self):
        with self.assertRaises(Exception) as err:
            self.toy.add_toy("R", "Roro")
        expected = "Shelf doesn't exist!"
        self.assertEqual(expected, str(err.exception))

    def test_add_toy_same_toy_already_in_shelf(self):
        self.toy.add_toy("A", "Robocop")
        with self.assertRaises(Exception) as err:
            self.toy.add_toy("A", "Robocop")
        expected = "Toy is already in shelf!"
        self.assertEqual(expected, str(err.exception))

    def test_add_toy_different_toy_already_in_shelf(self):
        self.toy.add_toy("A", "Robocop")
        with self.assertRaises(Exception) as err:
            self.toy.add_toy("A", "Terminator")
        expected = "Shelf is already taken!"
        self.assertEqual(expected, str(err.exception))

    def test_add_toy_valid_key_unoccupied_space(self):
        result = self.toy.add_toy("A", "Robocop")
        expected = "Toy:Robocop placed successfully!"
        self.assertEqual(expected, result)
        self.assertEqual(self.toy.toy_shelf["A"], "Robocop")

    def remove_toy_not_existing_shelf(self):
        with self.assertRaises(Exception) as err:
            self.toy.remove_toy("R", "Robocop")
        expected = "Shelf doesn't exist!"
        self.assertEqual(expected, str(err.exception))

    def test_remove_toy_toy_not_in_shelf(self):
        self.toy.add_toy("A", "Robocop")
        with self.assertRaises(Exception) as err:
            self.toy.remove_toy("A", "Terminator")
        expected = "Toy in that shelf doesn't exists!"
        self.assertEqual(expected, str(err.exception))

    def test_remove_toy_valid_toy_and_shelf(self):
        self.toy.add_toy("A", "Robocop")
        result = self.toy.remove_toy("A", "Robocop")
        expected = "Remove toy:Robocop successfully!"
        self.assertEqual(expected, result)
        self.assertEqual(self.toy.toy_shelf["A"], None)


if __name__ == "__main__":
    pass
