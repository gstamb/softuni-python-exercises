from abc import ABC, abstractmethod


class BaseService(ABC):
    ERR_MSG_SERVICE_NAME = "Service name cannot be empty!"
    ERR_MSG_SERVICE_CAPACITY = "Service capacity cannot be less than or equal to 0!"
    min_robot_capacity = 0

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.__capacity = capacity
        self.robots = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip():
            self.__name = value
        else:
            raise ValueError(self.ERR_MSG_SERVICE_NAME)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value > self.min_robot_capacity:
            self.__capacity = value
        else:
            raise ValueError(self.ERR_MSG_SERVICE_CAPACITY)

    @abstractmethod
    def details(self):
        pass

    def get_total_robots_price(self):
        if self.robots:
            return f"The value of service {self.name} is {sum([x.price for x in self.robots]):.2f}."
        else:
            return f"The value of service {self.name} is 0.00."

    def feed_all_robots(self):
        count = 0
        if self.robots:
            for robot in self.robots:
                robot.eating()
                count += 1
        return count

    def get_capacity(self):
        return self.__capacity


if __name__ == "__main__":
    pass
