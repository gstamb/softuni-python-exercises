from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str, capacity: int = 15):
        super().__init__(name, capacity)

    def details(self):
        if self.robots:
            return f"{self.name} Secondary Service:\nRobots: {' '.join([x.name for x in self.robots])}"
        else:
            return f"{self.name} Secondary Service:\nRobots: none"
