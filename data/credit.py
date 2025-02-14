from enum import Enum


class CreditStatus(Enum):
    ACTIVE = 'active'
    CLOSED = 'closed'
    OVERDUE = 'overdue'


class Credit:
    @property
    def status(self):
        return self.__status

    @property
    def status_name(self):
        return self.__get_status_name()

    def __init__(self, id, client, type, amount, due_date, interest_rate, monthly_payment, penalty_rate, opened_at, closed_at, status):
        self.id = int(id)
        self.client = client
        self.type = type
        self.amount = float(amount)
        self.due_date = due_date
        self.interest_rate = float(interest_rate)
        self.monthly_payment = int(monthly_payment)
        self.penalty_rate = float(penalty_rate)
        self.opened_at = opened_at
        self.closed_at = closed_at
        self.__status = CreditStatus(status)

    def __get_status_name(self):
        if self.__status == CreditStatus.ACTIVE:
            return "Активен"
        elif self.__status == CreditStatus.CLOSED:
            return "Закрыт"
        elif self.__status == CreditStatus.OVERDUE:
            return "Просрочен"
        else:
            return "Неизвестный статус"
