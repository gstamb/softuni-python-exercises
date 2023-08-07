from project.services.base_service import BaseService


class SecondaryService(BaseService):
    ROBOTS_CAPACITY = 15

    def __init__(self, name: str, capacity: int = None):
        super().__init__(name, capacity)
        self.capacity = capacity if capacity is not None else self.ROBOTS_CAPACITY

    def details(self):
        if self.robots:
            return f"{self.name} Secondary Service:\nRobots: {' '.join([x.name for x in self.robots])}"
        else:
            return f"{self.name} Secondary Service:\nRobots: none"


if __name__ == "__main__":
    pass
