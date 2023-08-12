from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace


class HorseRaceApp:
    HORSE_NAME_OBJ = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    @staticmethod
    def find_object_by_key_value(collection, key, value):
        if next((obj for obj in collection if getattr(obj, key, None) == value), None):
            return True
        return False

    @staticmethod
    def __fetch_object_by_key_value(collection, key, value):
        obj = next((obj for obj in collection if getattr(obj, key, None) == value), None)
        if obj:
            return obj

    def __validate_horse(self, collection, key, value):
        if self.find_object_by_key_value(collection, key, value):
            raise Exception(f"Horse {value} has been already added!")

    def __validate_jockey(self, collection, key, value):
        if self.find_object_by_key_value(collection, key, value):
            raise Exception(f"Jockey {value} has been already added!")

    def __validate_horse_race(self, collection, key, value):
        if self.find_object_by_key_value(collection, key, value):
            raise Exception(f"Race {value} has been already created!")

    def __validate_add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__fetch_object_by_key_value(self.jockeys, 'name', jockey_name)
        horses = [horse for horse in self.horses if horse.__class__.__name__ == horse_type and not horse.is_taken]
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not horses:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        return jockey, horses

    def __validate_add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self.__fetch_object_by_key_value(self.horse_races, 'race_type', race_type)
        jockey = self.__fetch_object_by_key_value(self.jockeys, 'name', jockey_name)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        return horse_race, jockey

    def __validate_start_horse_race(self, race_type: str):
        horse_race = self.__fetch_object_by_key_value(self.horse_races, 'race_type', race_type)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")
        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        return horse_race

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.HORSE_NAME_OBJ:
            return
        self.__validate_horse(self.horses, 'name', horse_name)

        new_horse = self.HORSE_NAME_OBJ[horse_type](horse_name, horse_speed)
        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        self.__validate_jockey(self.jockeys, 'name', jockey_name)
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        self.__validate_horse_race(self.horse_races, 'race_type', race_type)
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey, horses = self.__validate_add_horse_to_jockey(jockey_name, horse_type)
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        horse = horses[-1]
        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race, jockey = self.__validate_add_jockey_to_horse_race(race_type, jockey_name)
        if jockey in horse_race.jockeys:
            return f"{jockey_name} has been already added to the {race_type} race."
        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self.__validate_start_horse_race(race_type)
        winner = next((jockey for jockey in sorted(horse_race.jockeys, key=lambda x: -x.horse.speed)), None)
        return f"The winner of the {race_type} race, with a speed of " \
               f"{winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."


if __name__ == "__main__":
    pass