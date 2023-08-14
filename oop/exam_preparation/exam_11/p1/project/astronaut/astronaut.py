from abc import ABC, abstractmethod


class Astronaut(ABC):
    UNITS_PER_BREATH = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @abstractmethod
    def breathe(self):
        pass

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __str__(self):
        return f"Name: {self.name}\nOxygen: {self.oxygen}\nBackpack items: {', '.join(self.backpack) if self.backpack else 'none'}\n"


if __name__ == "__main__":
    pass
