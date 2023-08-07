from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    WEIGHT_INCREMENT_MALE = 3
    STARTING_WEIGHT_MALE_ROBOT = 9

    def __init__(self, name: str, kind: str, price: float, weight: int = None):
        super().__init__(name, kind, price, weight)
        self.weight = weight if weight is not None else self.STARTING_WEIGHT_MALE_ROBOT

    def eating(self):
        self.weight += self.WEIGHT_INCREMENT_MALE


if __name__ == "__main__":
    pass
