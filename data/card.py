from enum import Enum

class CardStatus(Enum):
    ACTIVE = 'active'
    BLOCKED = 'blocked'
    EXPIRED = 'expired'
    CLOSED = 'closed'

class Card:
    @property
    def status(self):
        return self.__status
    
    @property
    def status_name(self):
        return self.__get_status_name()
    
    def __init__(self, client, account, type, number, expiration_date, credit_limit, opened_date, closed_date, status):
        self.client = client
        self.account = account
        self.type = type
        self.number = int(number)
        self.expiration_date = expiration_date
        self.credit_limit = float(credit_limit)
        self.opened_date = opened_date
        self.closed_date = closed_date
        self.__status = CardStatus(status)
        

    def __get_status_name(self):
        if self.__status == CardStatus.ACTIVE:
            return "Активна"
        elif self.__status == CardStatus.BLOCKED:
            return "Заблокирована"
        elif self.__status == CardStatus.EXPIRED:
            return "Просрочена"
        elif self.__status == CardStatus.CLOSED:
            return "Закрыта"
        else:
            return "Неизвестный статус"