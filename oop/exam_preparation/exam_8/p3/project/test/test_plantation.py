from project.plantation import Plantation
import unittest


class PlantationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(25)

    def test_initialization_valid_params(self):
        self.assertEqual(25, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)
        plantation = Plantation(0)
        result = plantation.size
        self.assertEqual(0, result)

    def test_initialization_negative_size(self):
        with self.assertRaises(ValueError) as err:
            Plantation(-1)
        self.assertEqual("Size must be positive number!", str(err.exception))

    def test_change_plantation_size(self):
        with self.assertRaises(ValueError) as err:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(err.exception))
        self.plantation.size = 12
        result = self.plantation.size
        expected = 12
        self.assertEqual(expected, result)

    def test_hire_worker_new_worker(self):
        worker = "Pesho"
        result = self.plantation.hire_worker(worker)
        expected = "Pesho successfully hired."
        self.assertEqual(expected, result)
        self.assertEqual(["Pesho"], self.plantation.workers)

    def test_hire_worker_worker_already_hired(self):
        worker = "Pesho"
        self.plantation.hire_worker(worker)
        with self.assertRaises(ValueError) as err:
            self.plantation.hire_worker(worker)
        expected = "Worker already hired!"
        self.assertEqual(expected, str(err.exception))

    def test_len_plantation_default(self):
        result = self.plantation.__len__()
        expected = 0
        self.assertEqual(expected, result)

    def test_len_plantation_with_existing_plants(self):
        worker = "Pesho"
        plants = ["Banana", "Apple", "Orange"]
        self.plantation.plants[worker] = plants
        worker2 = "Ivaylo"
        plants2 = ["Banana", "Apple", "Orange"]
        self.plantation.plants[worker2] = plants2
        result = self.plantation.__len__()
        expected = 6
        self.assertEqual(expected, result)

    def test_planting_worker_not_existing(self):
        worker = "Pesho"
        plant = "Banana"
        with self.assertRaises(ValueError) as err:
            self.plantation.planting(worker, plant)
        expected = f"Worker with name {worker} is not hired!"
        self.assertEqual(expected, str(err.exception))

    def test_planting_valid_worker_insufficient_capacity(self):
        plantation = Plantation(3)
        worker = "Pesho"
        plants = ["Banana", "Apple", "Orange"]
        plantation.plants[worker] = plants
        plantation.hire_worker(worker)
        with self.assertRaises(ValueError) as err:
            plantation.planting(worker, "Kiwi")
        expected = "The plantation is full!"
        self.assertEqual(expected, str(err.exception))

    def test_planting_valid_worker_valid_capacity_first_plant(self):
        worker = "Pesho"
        plant = "Banana"
        self.plantation.hire_worker(worker)
        result = self.plantation.planting(worker, plant)
        expected = f"{worker} planted it's first {plant}."
        self.assertEqual(expected, result)
        self.assertEqual({"Pesho": ["Banana"]}, self.plantation.plants)

    def test_planting_worker_valid_worker_valid_capacity_worker_planted_before(self):
        worker = "Pesho"
        plant = "Banana"
        self.plantation.hire_worker(worker)
        self.plantation.planting(worker, plant)
        plant_next = "Apple"
        result = self.plantation.planting(worker, plant_next)
        expected = f"{worker} planted {plant_next}."
        self.assertEqual(expected, result)
        self.assertEqual({"Pesho": ["Banana", "Apple"]}, self.plantation.plants)

    def test_string_representation_empty_plant(self):
        result = str(self.plantation)
        expected = "Plantation size: 25\n"
        self.assertEqual(expected, result)

    def test_string_representation_with_plants(self):
        worker = "Pesho"
        plants = ["Banana", "Apple", "Orange"]
        self.plantation.hire_worker(worker)
        for plant in plants:
            self.plantation.planting(worker, plant)

        result = str(self.plantation)
        expected = "Plantation size: 25\nPesho\nPesho planted: Banana, Apple, Orange"
        self.assertEqual(expected, result)

    def test_repr_with_param(self):
        workers = ["Pesho", "Ivan", "Kiril", "Rosen"]
        for worker in workers:
            self.plantation.hire_worker(worker)
        result = self.plantation.__repr__()
        expected = "Size: 25\nWorkers: Pesho, Ivan, Kiril, Rosen"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
