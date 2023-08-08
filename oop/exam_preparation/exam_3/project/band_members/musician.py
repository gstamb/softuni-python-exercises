from abc import ABC, abstractmethod


class Musician(ABC):
    min_age = 16
    class_specific_skills = set()
    ERR_MSG_EMPTY_NAME = "Musician name cannot be empty!"
    ERR_MSG_UNDERAGE = "Musicians should be at least {0} years old!"
    ERR_MSG_UNAVAILABLE_CLASS_SKILL = "{0} is not a needed skill!"
    ERR_MSG_SKILL_ALREADY_LEARNED = "{0} is already learned!"
    CONFIRM_MSG_LEARNED_NEW_SKILL = "{0} learned to {1}."

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip():
            self.__name = value
        else:
            raise ValueError(self.ERR_MSG_EMPTY_NAME)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 16:
            self.__age = value
        else:
            raise ValueError(self.ERR_MSG_UNDERAGE.format(self.min_age))

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.class_specific_skills:
            raise ValueError(self.ERR_MSG_UNAVAILABLE_CLASS_SKILL.format(new_skill))
        if new_skill in self.skills:
            raise Exception(self.ERR_MSG_SKILL_ALREADY_LEARNED.format(new_skill))
        self.skills.append(new_skill)
        return self.CONFIRM_MSG_LEARNED_NEW_SKILL.format(self.name, new_skill)

    @abstractmethod
    def set_class_specific_skills(self):
        pass


if __name__ == "__main__":
    pass
