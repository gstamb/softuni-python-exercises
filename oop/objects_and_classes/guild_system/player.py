class Player:
    def __init__(self, name: int, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills:
            return "Skill already added"
        else:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        info_builder = ""
        info_builder += f"Name: {self.name}\n"
        info_builder += f"Guild: {self.guild}\n"
        info_builder += f"HP: {self.hp}\n"
        info_builder += f"MP: {self.mp}\n"
        for skill, mana_cost in self.skills.items():
            info_builder += f"==={skill} - {mana_cost}\n"

        return info_builder

if __name__ == "__main__":
    pass