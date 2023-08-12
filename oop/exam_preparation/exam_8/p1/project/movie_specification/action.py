from project.movie_specification.movie import Movie


class Action(Movie):
    MINIMUM_VIEWER_AGE = 12

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 12):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f"{self.__class__.__name__} - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"


if __name__ == "__main__":
    pass
