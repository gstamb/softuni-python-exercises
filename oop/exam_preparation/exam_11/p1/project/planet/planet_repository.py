class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet):
        self.planets.append(planet)

    def remove(self, planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        return next((planet for planet in self.planets if getattr(planet, 'name') == name), None)


if __name__ == "__main__":
    pass
