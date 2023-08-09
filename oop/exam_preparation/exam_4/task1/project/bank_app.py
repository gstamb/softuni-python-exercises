from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan


class BankApp:
    GET_VALID_LOANS_OBJ = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    GET_VALID_CLIENT_OBJ = {"Student": Student, "Adult": Adult}
    VALIDATE_LOAN_TO_PERSON = {"StudentLoan": "Student", "MortgageLoan": "Adult"}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    @staticmethod
    def _get_object_by_value(collection, key, value):
        return next((obj for obj in collection if getattr(obj, key, None) == value), None)

    def add_loan(self, loan_type: str):
        if loan_type not in self.GET_VALID_LOANS_OBJ:
            raise Exception("Invalid loan type!")

        fetch_loan_obj = self.GET_VALID_LOANS_OBJ[loan_type]
        new_loan_instance = fetch_loan_obj()
        self.loans.append(new_loan_instance)
        return f"{new_loan_instance.loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.GET_VALID_CLIENT_OBJ:
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."

        fetch_client_obj = self.GET_VALID_CLIENT_OBJ[client_type]
        create_new_customer = fetch_client_obj(client_name, client_id, income)
        self.clients.append(create_new_customer)
        return f"{create_new_customer.client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self._get_object_by_value(self.clients, "client_id", client_id)
        if not self.VALIDATE_LOAN_TO_PERSON[loan_type] == client.client_type:
            raise Exception("Inappropriate loan type!")

        get_loan = next((obj for obj in self.loans if getattr(obj, 'loan_type', None) == loan_type), None)
        self.loans.remove(get_loan)
        client.loans.append(get_loan)
        return f"Successfully granted {get_loan.loan_type} to {client.name} with ID {client.client_id}."

    def remove_client(self, client_id: str):
        client = self._get_object_by_value(self.clients, "client_id", client_id)
        if not client:
            raise Exception("No such client!")

        if len(client.loans):
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client.client_id}."

    def increase_loan_interest(self, loan_type: str):
        count = 0
        for loan in self.loans:
            if loan.loan_type == loan_type:
                loan.increase_interest_rate()
                count += 1
        return f"Successfully changed {count} loans."

    def increase_clients_interest(self, min_rate: float):
        count = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                count += 1
        return f"Number of clients affected: {count}."

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = sum([client.income for client in self.clients])
        loans_count_granted_to_clients = sum([len(client.loans) for client in self.clients])
        granted_sum = sum([client.total_loan_value() for client in self.clients])
        loans_count_not_granted = len(self.loans)
        loans_not_granted_sum = sum([loan.amount for loan in self.loans])
        sum_client_interest = sum([client.interest for client in self.clients])
        number_clients = sum([1 for _ in self.clients])

        try:
            avg_interest = sum_client_interest / number_clients
        except ZeroDivisionError:
            avg_interest = 0

        return f"Active Clients: {total_clients_count}\n" \
               f"Total Income: {total_clients_income:.2f}\n" \
               f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n" \
               f"Available Loans: {loans_count_not_granted}, Total Sum: {loans_not_granted_sum:.2f}\n" \
               f"Average Client Interest Rate: {avg_interest:.2f}"


if __name__ == "__main__":
    bank = BankApp(3)

    print(bank.add_loan('StudentLoan'))
    print(bank.add_loan('MortgageLoan'))
    print(bank.add_loan('StudentLoan'))
    print(bank.add_loan('MortgageLoan'))

    print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
    print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
    print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
    print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

    print(bank.grant_loan('StudentLoan', '1234567891'))
    print(bank.grant_loan('MortgageLoan', '1234567000'))
    print(bank.grant_loan('MortgageLoan', '1234567000'))

    print(bank.remove_client('1234567999'))

    print(bank.increase_loan_interest('StudentLoan'))
    print(bank.increase_loan_interest('MortgageLoan'))

    print(bank.increase_clients_interest(1.2))
    print(bank.increase_clients_interest(3.5))

    print(bank.get_statistics())
