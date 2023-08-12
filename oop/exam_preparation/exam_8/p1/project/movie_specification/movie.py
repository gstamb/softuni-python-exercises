from abc import ABC, abstractmethod

class Movie(ABC):
    FIRST_MOVIE_MADE_YEAR = 1888
    MINIMUM_VIEWER_AGE = None

    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes: int = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < self.FIRST_MOVIE_MADE_YEAR:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if value.__class__.__name__ != "User":
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.MINIMUM_VIEWER_AGE:
            raise ValueError(
                f"{self.__class__.__name__} movies must be restricted for audience under {self.MINIMUM_VIEWER_AGE} years!")
        self.__age_restriction = value

    @abstractmethod
    def details(self):
        pass


if __name__ == "__main__":
    pass
