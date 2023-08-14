class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        return next((astronaut for astronaut in self.astronauts if getattr(astronaut, 'name') == name), None)

    def assemble_a_team(self):
        return [astronaut for astronaut in
                sorted(self.astronauts, key=lambda x: -x.oxygen) if
                astronaut.oxygen > 30
                ][:5]


if __name__ == "__main__":
    pass
