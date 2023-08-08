from project.band_members.musician import Musician


class Drummer(Musician):
    DRUMMER_AVAILABLE_SKILLS = {"play the drums with drumsticks",
                                "play the drums with drum brushes",
                                "read sheet music"}

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.set_class_specific_skills()

    def set_class_specific_skills(self):
        self.class_specific_skills = self.DRUMMER_AVAILABLE_SKILLS


if __name__ == "__main__":
    pass
