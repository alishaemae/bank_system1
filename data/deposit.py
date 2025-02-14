from enum import Enum


class DepositStatus(Enum):
    ACTIVE = 'active'
    CLOSED = 'closed'
    FROZEN = 'frozen'


class Deposit:
    @property
    def status(self):
        return self.__status

    @property
    def status_name(self):
        return self.__get_status_name()

    def __init__(self, id, client, type, amount, due_date, interest_rate, early_withdrawal_allowed, opened_at, closed_at, status):
        self.id = int(id)
        self.client = client
        self.type = type
        self.amount = float(amount)
        self.due_date = due_date
        self.interest_rate = float(interest_rate)
        self.early_withdrawal_allowed = early_withdrawal_allowed
        self.opened_at = opened_at
        self.closed_at = closed_at
        self.__status = DepositStatus(status)

    def __get_status_name(self):
        if self.__status == DepositStatus.ACTIVE:
            return "Активен"
        elif self.__status == DepositStatus.CLOSED:
            return "Закрыт"
        elif self.__status == DepositStatus.FROZEN:
            return "Заморожен"
        else:
            return "Неизвестный статус"
