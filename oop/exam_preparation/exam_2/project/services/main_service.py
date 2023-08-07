from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str, capacity: int = 30):
        super().__init__(name, capacity)

    def details(self):
        if self.robots:
            return f"{self.name} Main Service:\nRobots: {' '.join([x.name for x in self.robots])}"
        else:
            return f"{self.name} Main Service:\nRobots: none"
