from project.band_members.musician import Musician


class Singer(Musician):
    SINGER_AVAILABLE_SKILLS = {"sing high pitch notes", "sing low pitch notes"}

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.set_class_specific_skills()

    def set_class_specific_skills(self):
        self.class_specific_skills = self.SINGER_AVAILABLE_SKILLS


if __name__ == "__main__":
    pass
