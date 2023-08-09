from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INTEREST_RATE = 1.5
    LOAN_AMOUNT = 2000.0
    INCREASE_INTEREST_INCREMENT = 0.2

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST_RATE, amount=self.LOAN_AMOUNT)
        self.loan_type = "StudentLoan"

    def increase_interest_rate(self):
        self.interest_rate += self.INCREASE_INTEREST_INCREMENT


if __name__ == "__main__":
    pass
