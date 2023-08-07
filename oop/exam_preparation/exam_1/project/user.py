class User:
    rating_increase_scale = 0.5
    rating_decrease_scale = 2

    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating = 0
        self.is_blocked = False

    def __str__(self):
        return f"{self.first_name} {self.last_name} Driving license: {self.driving_license_number} Rating: {self.rating}"

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if value.strip():
            self.__first_name = value
        else:
            raise ValueError("First name cannot be empty!")

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if value.strip():
            self.__last_name = value
        else:
            raise ValueError("Last name cannot be empty!")

    @property
    def driving_license_number(self):
        return self.__driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        if value.strip():
            self.__driving_license_number = value
        else:
            raise ValueError("Driving license number is required!")

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value >= 0:
            self.__rating = value
        else:
            raise ValueError("Users rating cannot be negative!")

    def increase_rating(self):
        if self.rating + self.rating_increase_scale > 10:
            self.rating = 10
        else:
            self.rating += self.rating_increase_scale

    def decrease_rating(self):
        if self.rating - self.rating_decrease_scale < 0:
            self.rating = 0
            self.is_blocked = True
        else:
            self.rating -= self.rating_decrease_scale
