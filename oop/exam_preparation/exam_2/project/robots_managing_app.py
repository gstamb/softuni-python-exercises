from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = ["MainService", "SecondaryService"]
    VALID_ROBOTS = ["MaleRobot", "FemaleRobot"]

    def __init__(self):
        self.robots = []
        self.services = []

    @classmethod
    def get_service_obj(cls, service_type):
        if service_type == "MainService":
            return MainService
        elif service_type == "SecondaryService":
            return SecondaryService

    @classmethod
    def return_robot_object(cls, robot_type):
        if robot_type == "MaleRobot":
            return MaleRobot
        elif robot_type == "FemaleRobot":
            return FemaleRobot

    @classmethod
    def allow_robots_in_service(cls, robot_type, service_type):
        if robot_type == "MaleRobot" and service_type == "MainService":
            return True
        if robot_type == "FemaleRobot" and service_type == "SecondaryService":
            return True
        return False

    def get_service_obj_from_str(self, service_name):
        # service existence is guaranteed by requirements
        return [x for x in self.services if x.name == service_name][0]

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")

        get_service = self.get_service_obj(service_type)
        new_service = get_service(name)
        self.services.append(new_service)
        return f"{new_service.__class__.__name__} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        get_robot = self.return_robot_object(robot_type)
        new_robot = get_robot(name, kind, price)
        self.robots.append(new_robot)
        return f"{new_robot.__class__.__name__} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        # robot and service existence guaranteed by requirement
        robot_index, robot_obj = [(index, x) for index, x in enumerate(self.robots) if x.name == robot_name][0]
        service_obj = self.get_service_obj_from_str(service_name)

        service_class_name = service_obj.__class__.__name__
        robot_class_name = robot_obj.__class__.__name__

        if not self.allow_robots_in_service(robot_class_name, service_class_name):
            return "Unsuitable service."
        if service_obj.capacity > len(service_obj.robots):
            service_obj.robots.append(self.robots.pop(robot_index))
            return f"Successfully added {robot_name} to {service_name}."
        else:
            raise Exception("Not enough capacity for this robot!")

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service_obj = self.get_service_obj_from_str(service_name)
        for robot in service_obj.robots:
            if robot.name == robot_name:
                self.robots.append(robot)
                service_obj.robots.remove(robot)
                return f"Successfully removed {robot_name} from {service_name}."
        else:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        robots_fed = self.get_service_obj_from_str(service_name).feed_all_robots()
        return f"Robots fed: {robots_fed}."

    def service_price(self, service_name: str):
        return self.get_service_obj_from_str(service_name).get_total_robots_price()

    def __str__(self):
        return_message = "".join([f"{service.details()}\n" for service in self.services]).strip()
        return return_message
