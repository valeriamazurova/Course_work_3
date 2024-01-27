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

    def reformat_date(self) -> None:
        """Преобразовывает дату в необходимый формат"""
        result = datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        self.date = result

    def __str__(self) -> str:
        result = f"{self.date} {self.description}\n{self.from_} -> {self.to}\n{self.amount} {self.currency}\n"
        return result

    @staticmethod
    def __mask_number(value: str) -> str:
        """Маскирует номер карты или счета"""
        if value.startswith("Счет"):
            return f"Счет **{value[-4:]}"
        return f"{value[:-12]} {value[-12:-10]}** **** {value[-4:]}"

    def prepare_mask_number(self) -> None:
        """Выбор атрибута для маскировки"""
        self.from_ = self.__mask_number(self.from_) if self.from_ else ""
        self.to = self.__mask_number(self.to) if self.to else ""


