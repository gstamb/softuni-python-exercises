from project.car.car import Car


class MuscleCar(Car):
    MIN_SPEED_LIMIT = 250
    MAX_SPEED_LIMIT = 450

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)
        self.speed_limit = speed_limit

    def __str__(self):
        return self.model


if __name__ == "__main__":
    pass
