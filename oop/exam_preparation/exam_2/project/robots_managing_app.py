from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_SERVICE_ROBOTS_COMBO = {"MainService": "MaleRobot", "SecondaryService": "FemaleRobot"}
    VALID_ROBOTS = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def __str__(self):
        return_message = "".join([f"{service.details()}\n" for service in self.services]).strip()
        return return_message

    @staticmethod
    def get_obj_from_str(collection, key, value):
        return next((obj for obj in collection if getattr(obj, key) == value), None)

    @staticmethod
    def _is_enough_capacity_for_robot(service_obj):
        return service_obj.get_capacity() > len(service_obj.robots)

    def _is_valid_service_for_robot(self, service_obj, robot_obj):
        return self.VALID_SERVICE_ROBOTS_COMBO.get(service_obj.__class__.__name__) == robot_obj.__class__.__name__

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES.keys():
            raise Exception("Invalid service type!")

        create_service = self.VALID_SERVICES[service_type]
        new_service = create_service(name)
        self.services.append(new_service)
        return f"{new_service.__class__.__name__} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS.keys():
            raise Exception("Invalid robot type!")

        create_robot = self.VALID_ROBOTS[robot_type]
        new_robot = create_robot(name, kind, price)
        self.robots.append(new_robot)
        return f"{new_robot.__class__.__name__} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot_index, robot_obj = [(index, x) for index, x in enumerate(self.robots) if x.name == robot_name][0]
        service_obj = self.get_obj_from_str(self.services, "name", service_name)

        if not self._is_valid_service_for_robot(service_obj, robot_obj):
            return "Unsuitable service."
        if self._is_enough_capacity_for_robot(service_obj):
            service_obj.robots.append(self.robots.pop(robot_index))
            return f"Successfully added {robot_name} to {service_name}."
        else:
            raise Exception("Not enough capacity for this robot!")

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service_obj = self.get_obj_from_str(self.services, "name", service_name)
        for robot in service_obj.robots:
            if robot.name == robot_name:
                self.robots.append(robot)
                service_obj.robots.remove(robot)
                return f"Successfully removed {robot_name} from {service_name}."
        else:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        robots_fed = self.get_obj_from_str(self.services, "name", service_name).feed_all_robots()
        return f"Robots fed: {robots_fed}."

    def service_price(self, service_name: str):
        return self.get_obj_from_str(self.services, "name", service_name).get_total_robots_price()


if __name__ == "__main__":
    pass
