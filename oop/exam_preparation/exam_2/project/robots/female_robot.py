from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    WEIGHT_INCREMENT_FEMALE = 1
    STARTING_WEIGHT_FEMALE_ROBOT = 7

    def __init__(self, name: str, kind: str, price: float, weight: int = None):
        super().__init__(name, kind, price, weight)
        self.weight = weight if weight is not None else self.STARTING_WEIGHT_FEMALE_ROBOT

    def eating(self):
        self.weight += self.WEIGHT_INCREMENT_FEMALE


if __name__ == "__main__":
    pass
