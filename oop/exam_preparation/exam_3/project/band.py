class Band:
    ERR_MSG_BAND_NAME = "Band name should contain at least one character!"

    def __init__(self, name: str):
        self.name = name
        self.members = []

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(self.ERR_MSG_BAND_NAME)
        self.__name = value


if __name__ == "__main__":
    pass
