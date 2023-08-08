class Concert:
    minimum_audience = 1
    minimum_ticket_price = 1.0
    minimum_expenses = 0.00
    VALID_GENRES = {"Metal", "Rock", "Jazz"}
    ERR_MSG_INVALID_GENRE = "Our group doesn't play {}!"
    ERR_MSG_NO_AUDIENCE = "At least one person should attend the concert!"
    ERR_MSG_TICKET_PRICE_TOO_LOW = "Ticket price must be at least 1.00$!"
    ERR_MSG_NEGATIVE_EXPENSES = "Expenses cannot be a negative number!"
    ERR_MSG_INVALID_PLACE = "Place must contain at least 2 chars. It cannot be empty!"

    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    def __str__(self):
        return f"{self.genre} concert at {self.place}."

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        if value not in self.VALID_GENRES:
            raise ValueError(self.ERR_MSG_INVALID_GENRE.format(value))
        else:
            self.__genre = value

    @property
    def audience(self):
        return self.__audience

    @audience.setter
    def audience(self, value):
        if value < self.minimum_audience:
            raise ValueError(self.ERR_MSG_NO_AUDIENCE)
        else:
            self.__audience = value

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        if value < self.minimum_ticket_price:
            raise ValueError(self.ERR_MSG_TICKET_PRICE_TOO_LOW)
        else:
            self.__ticket_price = value

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < self.minimum_expenses:
            raise ValueError(self.ERR_MSG_NEGATIVE_EXPENSES)
        else:
            self.__expenses = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        if len(value.strip()) < 2:
            raise ValueError(self.ERR_MSG_INVALID_PLACE)
        else:
            self.__place = value


if __name__ == "__main__":
    pass
