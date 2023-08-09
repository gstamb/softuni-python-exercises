from abc import ABC, abstractmethod


class BaseLoan(ABC):
    INTEREST_RATE = 0
    LOAN_AMOUNT = 0
    INCREASE_INTEREST_INCREMENT = 0

    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate
        self.amount = amount
        self.loan_type = "BaseLoan"

    @abstractmethod
    def increase_interest_rate(self):
        pass


if __name__ == "__main__":
    pass
