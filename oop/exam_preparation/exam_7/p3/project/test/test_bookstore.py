from project.bookstore import Bookstore
from unittest import TestCase, main


class BookstoreTest(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(30)

    def test_init_valid_params(self):
        self.assertEqual(30, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_init_with_zero_books_error(self):
        with self.assertRaises(ValueError) as err:
            self.bookstore.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(err.exception))
        with self.assertRaises(ValueError) as err2:
            self.bookstore.books_limit = -1
        self.assertEqual("Books limit of -1 is not valid", str(err2.exception))
        with self.assertRaises(ValueError) as err3:
            Bookstore(0)
        self.assertEqual("Books limit of 0 is not valid", str(err3.exception))
        with self.assertRaises(ValueError) as err4:
            Bookstore(-1)
        self.assertEqual("Books limit of -1 is not valid", str(err4.exception))

    def test_len_method_returns_correct_number_of_books(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book 1": 12, "Book 2": 13}
        result = len(self.bookstore)
        expected = 25
        self.assertEqual(expected, result)

    def test_receive_book_func_book_limit_reached(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book 1": 12, "Book 2": 13}
        with self.assertRaises(Exception) as err:
            self.bookstore.receive_book("Book 3", 6)
        expected = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(expected, str(err.exception))

    def test_receive_book_func_book_limit_not_reached(self):
        self.bookstore.receive_book("Book 1", 6)
        self.bookstore.receive_book("Book 2", 6)
        self.bookstore.receive_book("Book 3", 6)
        result = self.bookstore.receive_book("Book 3", 6)
        expected = f"12 copies of Book 3 are available in the bookstore."
        self.assertEqual(expected, result)
        result = self.bookstore.receive_book("Book 2", 6)
        expected = f"12 copies of Book 2 are available in the bookstore."
        self.assertEqual(expected, result)

    def test_sell_books_book_does_not_exist(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book 1": 12, "Book 2": 13}
        with self.assertRaises(Exception) as err:
            self.bookstore.sell_book("Book 4", 3)
        self.assertEqual("Book Book 4 doesn't exist!", str(err.exception))

    def test_sell_books_insufficient_quantity(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book 1": 12, "Book 2": 13}
        with self.assertRaises(Exception) as err:
            self.bookstore.sell_book("Book 1", 13)
        self.assertEqual("Book 1 has not enough copies to sell. Left: 12", str(err.exception))

    def test_sell_books_sufficient_quantity_to_sell(self):
        book = "Book 1"
        quantity = 12
        self.bookstore.receive_book(book, quantity)
        result = self.bookstore.sell_book("Book 1", 12)
        expected = f"Sold {quantity} copies of {book}"
        self.assertEqual(expected, result)
        self.assertEqual(12, self.bookstore._Bookstore__total_sold_books)
        self.assertEqual({f"{book}": 0}, self.bookstore.availability_in_store_by_book_titles)

    def test_string_repr_method(self):
        book = "Book 1"
        quantity = 12
        self.bookstore.receive_book(book, quantity)
        self.bookstore.sell_book("Book 1", 12)
        result = str(self.bookstore)
        expected = 'Total sold books: 12\nCurrent availability: 0\n - Book 1: 0 copies'
        self.assertEqual(expected, result)


if __name__ == "__main__":
    pass
