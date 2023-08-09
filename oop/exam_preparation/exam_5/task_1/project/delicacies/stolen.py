from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    STOLEN_PORTION_SIZE = 250
    TYPE_DELICACY = "Stolen"


    def __init__(self, name: str, price: float):
        super().__init__(name=name, portion=self.STOLEN_PORTION_SIZE, price=price)

    def details(self):
        return f"Stolen {self.name}: {self.STOLEN_PORTION_SIZE}g - {self.price:.2f}lv."


if __name__ == "__main__":
    pass
