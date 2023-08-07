class User:
    ERR_MSG_EMPTY_FIRST_NAME = "First name cannot be empty!"
    ERR_MSG_EMPTY_LAST_NAME = "Last name cannot be empty!"
    ERR_MSG_EMPTY_DLN = "Driving license number is required!"
    ERR_MSG_NEGATIVE_RATING = "Users rating cannot be negative!"
    rating_increase_scale = 0.5
    rating_decrease_scale = 2
    min_rating = 0
    max_rating = 10

    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating = self.min_rating
        self.is_blocked = False

    def __str__(self):
        return f"{self.first_name} {self.last_name} " \
               f"Driving license: {self.driving_license_number} " \
               f"Rating: {self.rating}"

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if value.strip():
            self.__first_name = value
        else:
            raise ValueError(self.ERR_MSG_EMPTY_FIRST_NAME)

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if value.strip():
            self.__last_name = value
        else:
            raise ValueError(self.ERR_MSG_EMPTY_LAST_NAME)

    @property
    def driving_license_number(self):
        return self.__driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        if value.strip():
            self.__driving_license_number = value
        else:
            raise ValueError(self.ERR_MSG_EMPTY_DLN)

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value >= self.min_rating:
            self.__rating = value
        elif value > self.max_rating:
            self.__rating = self.max_rating
        else:
            raise ValueError(self.ERR_MSG_NEGATIVE_RATING)

    def increase_rating(self):
        if self.rating + self.rating_increase_scale > self.max_rating:
            self.rating = self.max_rating
        else:
            self.rating += self.rating_increase_scale

    def decrease_rating(self):
        if self.rating - self.rating_decrease_scale < self.min_rating:
            self.rating = self.min_rating
            self.is_blocked = True
        else:
            self.rating -= self.rating_decrease_scale


if __name__ == "__main__":
    pass
