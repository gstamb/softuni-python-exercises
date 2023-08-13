class Player:
    name_list = set()
    MIN_STAMINA = 0
    MAX_STAMINA = 100
    MIN_AGE = 12

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name not valid!")
        if value in Player.name_list:
            raise Exception(f"Name {value} is already used!")
        Player.name_list.add(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MIN_AGE:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < self.MIN_STAMINA or value > self.MAX_STAMINA:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < self.MAX_STAMINA

    def valid_subtraction(self, value):
        if self.stamina - value <= self.MIN_STAMINA:
            return self.MIN_STAMINA
        else:
            return self.stamina - value


if __name__ == "__main__":
    pass
