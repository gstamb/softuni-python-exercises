from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from collections import deque


class SpaceStation:
    ASTRONAUT_OBJECTS = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.missions = 0
        self.successful_missions = 0

    def __validate_mission(self, planet_name):
        """
        Validates that the target planet exists and assembles a team to carry out the mission.
        Team consist of up to five astronauts with the highest oxygen capacity.
        Return planet and team objects or raises an error if either does not exist.
         """
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        team = deque(self.astronaut_repository.assemble_a_team())
        if not team:
            raise Exception("You need at least one astronaut to explore the planet!")
        return planet, team

    def __process_mission(self, team, planet):
        """
        Mission consist of up to five astronauts going to the planet to collect items.
        Astronauts are dispatched sequentially according to their descending oxygen supply.
        An astronaut will collect items until it runs out of oxygen.
        Mission is successful if all items are found otherwise it is considered `not completed`.
        Returns the result of the mission.
        """
        initial_team_size = len(team)
        while team and planet.items:
            astronaut = team.popleft()
            while planet.items:
                if astronaut.oxygen - astronaut.UNITS_PER_BREATH < 0:
                    break
                find_item = planet.items.pop()
                astronaut.breathe()
                astronaut.backpack.append(find_item)

        if not planet.items:
            self.successful_missions += 1
            return f"Planet: {planet.name} was explored. {initial_team_size - len(team)} " \
                   f"astronauts participated in collecting items."
        else:
            return "Mission is not completed."

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.ASTRONAUT_OBJECTS.keys():
            raise Exception("Astronaut type is not valid!")
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        astronaut_object = self.ASTRONAUT_OBJECTS[astronaut_type]
        new_astronaut = astronaut_object(name)
        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        new_planet = Planet(name)
        new_planet.items = items.split(", ")
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        [astronaut.increase_oxygen(10) for astronaut in self.astronaut_repository.astronauts]

    def send_on_mission(self, planet_name: str):
        planet, team = self.__validate_mission(planet_name)
        self.missions += 1
        return self.__process_mission(team, planet)

    def report(self):
        report_string = f"{self.successful_missions} successful missions!\n"
        report_string += f"{self.missions - self.successful_missions} missions were not completed!\n"
        report_string += f"Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            report_string += str(astronaut)
        return report_string.strip()


if __name__ == "__main__":
    pass
