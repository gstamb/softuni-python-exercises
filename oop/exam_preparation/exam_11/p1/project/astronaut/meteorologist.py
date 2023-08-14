from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    UNITS_PER_BREATH = 15

    def __init__(self, name: str):
        super().__init__(name, oxygen=90)

    def breathe(self):
        self.oxygen -= self.UNITS_PER_BREATH


if __name__ == "__main__":
    pass
