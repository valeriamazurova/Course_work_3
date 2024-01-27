from datetime import datetime


class Operation:
    def __init__(self, date, state, amount, currency, description, from_, to):
        self.date = date
        self.state = state
        self.amount = amount
        self.currency = currency
        self.description = description
        self.from_ = from_
        self.to = to

    def reformat_date(self):
        result = datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        self.date = result

    def __str__(self):
        result = f"{self.date} {self.description}\n{self.from_} -> {self.to}\n{self.amount} {self.to}\n"
        return result
