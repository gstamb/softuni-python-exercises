from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop("Good Boy")

    def test_initialization(self):
        self.assertEqual("Good Boy", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_valid_quantity(self):
        name = "Dog food"
        quantity = 25.2
        result = self.shop.add_food(name, quantity)
        expected = f"Successfully added {quantity:.2f} grams of {name}."
        self.assertEqual(expected, result)
        self.assertEqual({name: quantity}, self.shop.food)

    def test_add_food_invalid_quantity(self):
        name = "Dog food"
        quantity = 0
        with self.assertRaises(ValueError) as err:
            self.shop.add_food(name, quantity)
        expected = 'Quantity cannot be equal to or less than 0'
        self.assertEqual(expected, str(err.exception))
        self.assertEqual({}, self.shop.food)

    def test_add_food_adding_quantity_to_existing_product(self):
        name = "Dog food"
        quantity = 25.2
        self.shop.add_food(name, quantity)
        result = self.shop.add_food(name, quantity)
        expected = f"Successfully added {quantity:.2f} grams of {name}."
        self.assertEqual(expected, result)
        self.assertEqual({name: quantity * 2}, self.shop.food)

    def test_add_pet_valid_params(self):
        pet_name = "Pesho"
        result = self.shop.add_pet(pet_name)
        expected = f"Successfully added {pet_name}."
        self.assertEqual(expected, result)
        self.assertEqual([pet_name], self.shop.pets)

    def test_add_pet_existing_name(self):
        pet_name = "Pesho"
        self.shop.add_pet(pet_name)
        with self.assertRaises(Exception) as err:
            self.shop.add_pet(pet_name)
        expected = "Cannot add a pet with the same name"
        self.assertEqual(expected, str(err.exception))
        self.assertEqual([pet_name], self.shop.pets)

    def test_feed_pet_valid_params(self):
        food_name = "Dog food"
        quantity = 101
        self.shop.add_food(food_name, quantity)
        pet_name = "Pesho"
        self.shop.add_pet(pet_name)
        result = self.shop.feed_pet(food_name, pet_name)
        expected = f"{pet_name} was successfully fed"
        self.assertEqual(expected, result)
        self.assertEqual(quantity - 100, self.shop.food[food_name])

    def test_feed_pet_pet_name_not_existing(self):
        # food quantity going below zero was found during testing
        food_name = "Dog food"
        quantity = 25.2
        self.shop.add_food(food_name, quantity)
        pet_name = "Pesho"
        self.shop.add_pet(pet_name)
        with self.assertRaises(Exception) as err:
            self.shop.feed_pet(food_name, "Ivan")
        expected = f"Please insert a valid pet name"
        self.assertEqual(expected, str(err.exception))

    def test_feed_pet_food_name_not_existing(self):
        # food quantity going below zero was found during testing
        food_name = "Dog food"
        quantity = 25.2
        self.shop.add_food(food_name, quantity)
        pet_name = "Pesho"
        self.shop.add_pet(pet_name)
        non_existing_food_name = "Cat food"
        result = self.shop.feed_pet(non_existing_food_name, pet_name)
        expected = f'You do not have {non_existing_food_name}'
        self.assertEqual(expected, result)

    def test_feed_pet_food_name_not_sufficient(self):
        # food quantity going below zero was found during testing
        food_name = "Dog food"
        quantity = 25.2
        self.shop.add_food(food_name, quantity)
        pet_name = "Pesho"
        self.shop.add_pet(pet_name)
        result = self.shop.feed_pet(food_name, pet_name)
        expected = "Adding food..."
        self.assertEqual(expected, result)
        self.assertEqual(1025.2, self.shop.food[food_name])

    def test_string_representation(self):
        pet_names = ["Pesho", "Ivan", "Todor", "Misho"]
        for name in pet_names:
            self.shop.add_pet(name)
        result = str(self.shop)
        expected = f'Shop {self.shop.name}:\nPets: {", ".join(pet_names)}'
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
