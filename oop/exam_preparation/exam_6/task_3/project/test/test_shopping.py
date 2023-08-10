from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class ShoppingCartTest(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Alpine", 50)

    def test_initialization_valid_params(self):
        self.assertEqual("Alpine", self.cart.shop_name)
        self.assertEqual(50, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_initialization_with_invalid_name(self):
        with self.assertRaises(ValueError) as err:
            ShoppingCart("Al23pine", 3000)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(err.exception))

    def test_add_to_cart_valid_product(self):
        result = self.cart.add_to_cart("Protector", 10)
        expected = "Protector product was successfully added to the cart!"
        self.assertEqual(expected, result)
        self.assertEqual(self.cart.products, {"Protector": 10})
        self.assertEqual("Fishing rod product was successfully added to the cart!",
                         self.cart.add_to_cart("Fishing rod", 10))
        self.assertEqual(self.cart.products, {"Protector": 10, "Fishing rod": 10})

    def test_add_to_cart_product_too_expensive_low_threshold(self):
        with self.assertRaises(ValueError) as err:
            self.cart.add_to_cart("Protector", 100)
        self.assertEqual("Product Protector cost too much!", str(err.exception))

    def test_add_to_cart_valid_product_float(self):
        result = self.cart.add_to_cart("Protector", 99.99)
        expected = "Protector product was successfully added to the cart!"
        self.assertEqual(expected, result)
        self.assertEqual(self.cart.products, {"Protector": 99.99})

    def test_remove_product_from_the_cart(self):
        self.cart.add_to_cart("Protector", 10)
        self.cart.add_to_cart("Fishing rod", 10)
        result = self.cart.remove_from_cart("Fishing rod")
        expected = "Product Fishing rod was successfully removed from the cart!"
        self.assertEqual(expected, result)
        self.assertEqual(self.cart.products, {"Protector": 10})

    def test_remove_product_from_the_cart_invalid_product(self):
        with self.assertRaises(ValueError) as err:
            self.cart.remove_from_cart("Protector")
        self.assertEqual("No product with name Protector in the cart!", str(err.exception))

    def test_adding_two_shop_instances(self):
        shop_instance_other = ShoppingCart("Seaside", 3000)
        self.cart.add_to_cart("Protector", 50)
        shop_instance_other.add_to_cart("Swimming Suit", 50)
        new_object = self.cart + shop_instance_other
        self.assertEqual("AlpineSeaside", new_object.shop_name)
        self.assertEqual({"Protector": 50, "Swimming Suit": 50}, new_object.products)
        self.assertEqual(3050, new_object.budget)
        self.assertIsInstance(new_object, ShoppingCart)

    def test_buying_products_exceeding_budget(self):
        self.cart.add_to_cart("Protector", 60)
        with self.assertRaises(ValueError) as err:
            self.cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 10.00lv!", str(err.exception))

    def test_buying_products_within_budget(self):
        self.cart.add_to_cart("Protector", 40)
        result = self.cart.buy_products()
        expected = 'Products were successfully bought! Total cost: 40.00lv.'
        self.assertEqual(expected, result)

    def test_buying_products_exceeding_budget_multiple_products(self):
        self.cart.add_to_cart("Protector", 5.0)
        self.cart.add_to_cart("Swimming Suit", 5)
        self.cart.add_to_cart("Swimming goggles", 90.99)
        with self.assertRaises(ValueError) as err:
            self.cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 50.99lv!", str(err.exception))


if __name__ == "__main__":
    pass
