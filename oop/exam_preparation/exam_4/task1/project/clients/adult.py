from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INITIAL_INTEREST = 4.0
    INCREASE_INTEREST_INCREMENT = 2.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INITIAL_INTEREST)
        self.client_type = "Adult"

    def increase_clients_interest(self):
        self.interest += self.INCREASE_INTEREST_INCREMENT


if __name__ == "__main__":
    pass
