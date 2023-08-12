from project.movie_specification.movie import Movie
from typing import List


class User:
    MINIMUM_USER_AGE = 6

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: List[Movie] = []
        self.movies_owned: List[Movie] = []

    def __str__(self):
        str_rep = f"Username: {self.username}, Age: {self.age}\n"
        str_rep += "Liked movies:\n"
        if self.movies_liked:
            str_rep += "\n".join([picture.details() for picture in self.movies_liked])
            str_rep += "\n"
        else:
            str_rep += "No movies liked.\n"
        str_rep += "Owned movies:\n"
        if self.movies_owned:
            str_rep += "\n".join([picture.details() for picture in self.movies_owned])
        else:
            str_rep += "No movies owned.\n"
        return str_rep.strip()

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MINIMUM_USER_AGE:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value


if __name__ == "__main__":
    pass
