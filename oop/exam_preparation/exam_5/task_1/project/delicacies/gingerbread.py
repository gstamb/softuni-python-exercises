from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    GINGERBREAD_PORTION_SIZE = 200
    TYPE_DELICACY = "Gingerbread"
    def __init__(self, name: str, price: float):
        super().__init__(name=name, portion=self.GINGERBREAD_PORTION_SIZE, price=price)

    def details(self):
        return f"Gingerbread {self.name}: {self.GINGERBREAD_PORTION_SIZE}g - {self.price:.2f}lv."


if __name__ == "__main__":
    pass
