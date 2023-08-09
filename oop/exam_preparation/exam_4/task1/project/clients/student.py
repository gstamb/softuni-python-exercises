from project.clients.base_client import BaseClient


class Student(BaseClient):
    INITIAL_INTEREST = 2.0
    INCREASE_INTEREST_INCREMENT = 1.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INITIAL_INTEREST)
        self.client_type = "Student"

    def increase_clients_interest(self):
        self.interest += self.INCREASE_INTEREST_INCREMENT


if __name__ == "__main__":
    pass
