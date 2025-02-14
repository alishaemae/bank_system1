from enum import Enum


class AccountStatus(Enum):
    ACTIVE = 'active'
    CLOSED = 'closed'
    FROZEN = 'frozen'


class Account:
    __status = None

    @property
    def status(self):
        return self.__status

    @property
    def status_name(self):
        return self.__get_status_name()

    def __init__(self, id, client, type, number, currency, balance, opened_date, closed_date, status):
        self.id = int(id)
        self.client = client
        self.type = type
        self.number = str(number)
        self.currency = str(currency)
        self.balance = str(balance)
        self.opened_date = opened_date
        self.closed_date = closed_date
        self.__status = AccountStatus(
            status) if status is not None else AccountStatus.ACTIVE

    def __get_status_name(self):
        if self.__status == AccountStatus.ACTIVE:
            return "Активен"
        elif self.__status == AccountStatus.CLOSED:
            return "Закрыт"
        elif self.__status == AccountStatus.FROZEN:
            return "Заморожен"
        else:
            return "Неизвестный статус"
