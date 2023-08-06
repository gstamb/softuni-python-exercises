class Route:
    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        self.start_point = start_point
        self.end_point = end_point
        self.length = length
        self.route_id = route_id
        self.is_locked = False

    @property
    def start_point(self):
        return self.__start_point

    @start_point.setter
    def start_point(self, value):
        if value.strip():
            self.__start_point = value
        else:
            raise ValueError("Start point cannot be empty!")

    @property
    def end_point(self):
        return self.__end_point

    @end_point.setter
    def end_point(self, value):
        if value.strip():
            self.__end_point = value
        else:
            raise ValueError("End point cannot be empty!")

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value >= 1.00:
            self.__length = value
        else:
            raise ValueError("Length cannot be less than 1.00 kilometer!")
