from project.library import Library
from unittest import TestCase, main


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.library = Library("Sofia")

    def test_valid_init(self):
        self.assertEqual("Sofia", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_init_invalid_name(self):
        with self.assertRaises(ValueError) as err:
            Library("")
        self.assertEqual("Name cannot be empty string!", str(err.exception))

    def test_add_book_to_library(self):
        author = "Malcolm Gladwell"
        book = "Talking to strangers"
        self.library.add_book(author, book)
        result = self.library.books_by_authors
        expected = {author: [book]}
        self.assertEqual(expected, result)

    def test_add_book_to_library_author_already_registered(self):
        author = "Malcolm Gladwell"
        book = "Talking to strangers"
        self.library.add_book(author, book)
        book2 = "Outliers"
        self.library.add_book(author, book2)
        result = self.library.books_by_authors
        expected = {author: [book, book2]}
        self.assertEqual(expected, result)

    def test_add_reader(self):
        reader = "Peter"
        self.library.add_reader(reader)
        result = self.library.readers
        expected = {reader: []}
        self.assertEqual(expected, result)

    def test_add_already_existing_reader(self):
        reader = "Peter"
        self.library.add_reader(reader)
        result = self.library.add_reader(reader)
        expected = f"{reader} is already registered in the {self.library.name} library."
        self.assertEqual(expected, result)

    def test_rent_book_valid_params(self):
        reader1 = "Peter"
        self.library.add_reader(reader1)
        reader2 = "Josine"
        self.library.add_reader(reader2)
        author = "Malcolm Gladwell"
        book1 = "Talking to strangers"
        book2 = "Outliers"
        self.library.add_book(author, book1)
        self.library.add_book(author, book2)
        book2 = "Outliers"
        self.library.add_book(author, book2)
        self.library.rent_book(reader1, author, book1)
        result = self.library.readers
        expected = {reader2: [], reader1: [{author: book1}]}
        self.assertEqual(expected, result)
        self.assertEqual({author: [book2]}, self.library.books_by_authors)

    def test_rent_book_invalid_reader_name(self):
        author = "Malcolm Gladwell"
        book1 = "Talking to strangers"
        self.library.add_book(author, book1)
        book2 = "Outliers"
        self.library.add_book(author, book2)
        result = self.library.rent_book("Pesho", author, book1)
        expected = f"Pesho is not registered in the {self.library.name} Library."
        self.assertEqual(expected, result)

    def test_rent_book_invalid_author(self):
        reader1 = "Peter"
        self.library.add_reader(reader1)
        author = "Malcolm Gladwell"
        book1 = "Talking to strangers"
        self.library.add_book(author, book1)
        book2 = "Outliers"
        self.library.add_book(author, book2)
        self.library.rent_book(reader1, author, book1)
        result = self.library.rent_book(reader1, "Kafka", book1)
        expected = f"{self.library.name} Library does not have any Kafka's books."
        self.assertEqual(expected, result)

    def test_rent_book_invalid_title(self):
        reader1 = "Peter"
        self.library.add_reader(reader1)
        author = "Malcolm Gladwell"
        book1 = "Talking to strangers"
        self.library.add_book(author, book1)
        book2 = "Outliers"
        self.library.add_book(author, book2)
        self.library.rent_book(reader1, author, book1)
        result = self.library.rent_book(reader1, author, "Blink")
        expected = f"""{self.library.name} Library does not have {author}'s "Blink"."""
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
