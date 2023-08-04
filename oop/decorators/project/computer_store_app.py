from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


def return_obj(computer_type):
    if computer_type == "Desktop Computer":
        return DesktopComputer
    elif computer_type == "Laptop":
        return Laptop
    else:
        return None


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        get_computer = return_obj(type_computer)
        if get_computer:
            computer = get_computer(manufacturer, model)
            self.warehouse.append(computer)
            return computer.configure_computer(processor, ram)
        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)
                return f"{computer} sold for {client_budget}$."
            else:
                raise Exception(f"Sorry, we don't have a computer for you.")
