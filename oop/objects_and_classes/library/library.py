from user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # {"author" : []  }
        self.rented_books = {}  # { "username" : {"book_names" : "days till return"} }

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available and book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        else:
            for user, book in self.rented_books.items():
                if book_name in book:
                    return f'The book "{book_name}" is already rented and will be available in {book[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            del self.rented_books[user.username][book_name]
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"


if __name__ == "__main__":
    pass
