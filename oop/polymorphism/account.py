class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):
        return self._transactions[::-1]

    def __gt__(self, other):
        return self.amount > other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return self.amount != other.amount

    def __add__(self, other):
        return Account(f"{self.owner}&{other.owner}", self.amount + other.amount)

    @property
    def balance(self):
        return self.amount

    def handle_transaction(self, transaction_amount):
        if self.amount + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        else:
            self.amount += transaction_amount
            self._transactions.append(transaction_amount)
            return f"New balance: {self.amount}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        else:
            self.handle_transaction(amount)
