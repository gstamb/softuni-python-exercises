from project.band_members.musician import Musician


class Guitarist(Musician):
    GUITARIST_AVAILABLE_SKILLS = {"play metal",
                                  "play rock",
                                  "play jazz"}

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.set_class_specific_skills()

    def set_class_specific_skills(self):
        self.class_specific_skills = self.GUITARIST_AVAILABLE_SKILLS


if __name__ == "__main__":
    pass
