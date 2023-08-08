from project.band_members.drummer import Drummer
from project.band_members.singer import Singer
from project.band_members.guitarist import Guitarist
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
    ERR_MSG_INVALID_MUSICIAN_TYPE = "Invalid musician type!"
    ERR_MSG_MUSICIAN_EXISTS = "{0} is already a musician!"
    ERR_MSG_BAND_EXISTS = "{0} band is already created!"
    ERR_MSG_CONCERT_EXISTS = "{0} is already registered for {1} concert!"
    ERR_MSG_ADD_MUSICIAN_TO_BAND_NOT_MUSICIAN = "{0} isn't a musician!"
    ERR_MSG_REMOVE_MUSICIAN_FROM_BAND_NOT_MUSICIAN = "{0} isn't a member of {1}!"
    ERR_MSG_ADD_REMOVE_MUSICIAN_TO_BAND_NOT_BAND = "{0} isn't a band!"
    ERR_MSG_INSUFFICIENT_MEMBERS = "{0} can't start the concert because it doesn't have enough members!"
    ERR_MSG_BAND_NO_SKILLS_TO_PERFORM = "The {0} band is not ready to play at the concert!"

    SUCCESS_MSG_MUSICIAN_CREATED = "{0} is now a {1}."
    SUCCESS_MSG_BAND_CREATED = "{0} was created."
    SUCCESS_MSG_CONCERT_CREATED = "{0} concert in {1} was added."
    SUCCESS_MSG_ADD_MUSICIAN = "{0} was added to {1}."
    SUCCESS_MSG_REMOVE_MUSICIAN = "{0} was removed from {1}."
    SUCCESS_MSG_CONCERT_OUTCOME = "{0} gained {1:.2f}$ from the {2} concert in {3}."
    REQUIRED_SKILLS = {"Rock": {"play the drums with drumsticks", "sing high pitch notes", "play rock"},
                       "Metal": {"play the drums with drumsticks", "sing low pitch notes", "play metal"},
                       "Jazz": {"play the drums with drum brushes", "sing high pitch notes", "sing low pitch notes",
                                "play jazz"}
                       }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    @classmethod
    def _raise_error_upon_invalid_musician(cls, musician_type: str):
        if musician_type not in cls.VALID_MUSICIANS:
            raise ValueError(cls.ERR_MSG_INVALID_MUSICIAN_TYPE)

    @classmethod
    def _get_musician_object(cls, musician_type):
        return cls.VALID_MUSICIANS[musician_type]

    @staticmethod
    def _raise_error_if_obj_value_exists(collection, key, value, err_msg: str):
        if [obj for obj in collection if getattr(obj, key, None) == value]:
            raise Exception(err_msg)

    @staticmethod
    def _get_object_by_attribute(collection, key, value):
        return next((obj for obj in collection if getattr(obj, key, None) == value), None)

    @staticmethod
    def validate_musician_count(band: Band):
        members = set([member.__class__.__name__ for member in band.members])
        if len(members) == 3:
            return True
        return False

    def verify_musician_skills(self, band: Band, genre: str):
        skills = set()
        for musician in band.members:
            for skill in musician.skills:
                skills.add(skill)
        return self.REQUIRED_SKILLS[genre].issubset(skills)

    def create_musician(self, musician_type: str, name: str, age: int):
        self._raise_error_upon_invalid_musician(musician_type)
        self._raise_error_if_obj_value_exists(self.musicians, "name", name, self.ERR_MSG_MUSICIAN_EXISTS.format(name))

        musician_obj = self._get_musician_object(musician_type)
        new_musician = musician_obj(name, age)
        self.musicians.append(new_musician)
        return self.SUCCESS_MSG_MUSICIAN_CREATED.format(getattr(new_musician, "name"),
                                                        new_musician.__class__.__name__)

    def create_band(self, name: str):
        self._raise_error_if_obj_value_exists(self.bands, "name", name, self.ERR_MSG_BAND_EXISTS.format(name))

        new_band = Band(name)
        self.bands.append(new_band)
        return self.SUCCESS_MSG_BAND_CREATED.format(new_band.name)

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self._raise_error_if_obj_value_exists(self.concerts, "place", place,
                                              self.ERR_MSG_CONCERT_EXISTS.format(place, genre))

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return self.SUCCESS_MSG_CONCERT_CREATED.format(getattr(new_concert, "genre"), getattr(new_concert, "place"))

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._get_object_by_attribute(self.musicians, "name", musician_name)
        if not musician:
            raise Exception(self.ERR_MSG_ADD_MUSICIAN_TO_BAND_NOT_MUSICIAN.format(musician_name))
        band = self._get_object_by_attribute(self.bands, "name", band_name)
        if not band:
            raise Exception(self.ERR_MSG_ADD_REMOVE_MUSICIAN_TO_BAND_NOT_BAND.format(band_name))

        band.members.append(musician)
        return self.SUCCESS_MSG_ADD_MUSICIAN.format(musician.name, band.name)

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self._get_object_by_attribute(self.bands, "name", band_name)
        if not band:
            raise Exception(self.ERR_MSG_ADD_REMOVE_MUSICIAN_TO_BAND_NOT_BAND.format(band_name))
        member = self._get_object_by_attribute(band.members, "name", musician_name)
        if not member:
            raise Exception(self.ERR_MSG_REMOVE_MUSICIAN_FROM_BAND_NOT_MUSICIAN.format(musician_name, band_name))

        band.members.remove(member)
        return self.SUCCESS_MSG_REMOVE_MUSICIAN.format(musician_name, band_name)

    def start_concert(self, concert_place: str, band_name: str):
        band = self._get_object_by_attribute(self.bands, "name", band_name)
        concert = self._get_object_by_attribute(self.concerts, "place", concert_place)

        if not self.validate_musician_count(band):
            raise Exception(self.ERR_MSG_INSUFFICIENT_MEMBERS.format(band_name))

        if not self.verify_musician_skills(band, concert.genre):
            raise Exception(self.ERR_MSG_BAND_NO_SKILLS_TO_PERFORM.format(band_name))

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return self.SUCCESS_MSG_CONCERT_OUTCOME.format(band.name, profit, concert.genre, concert.place)


if __name__ == "__main__":

    musician_types = ["Singer", "Drummer", "Guitarist"]
    names = ["George", "Alex", "Lilly"]

    app = ConcertTrackerApp()

    for i in range(3):
        print(app.create_musician(musician_types[i], names[i], 20))

    print(app.musicians[0].learn_new_skill("sing high pitch notes"))
    print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
    print(app.musicians[2].learn_new_skill("play rock"))

    print(app.create_band("RockName"))
    for i in range(3):
        print(app.add_musician_to_band(names[i], "RockName"))
    print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))

    print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
    print(app.start_concert("Sofia", "RockName"))
