from enum import IntEnum


class UserRole(IntEnum):
    MANAGER = 1
    BOSS = 2


class User:
    __role = 0

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    @property
    def role_name(self):
        return self.__get_role_name()

    @property
    def role(self):
        return self.__role

    def __init__(self, id, role, job, last_name, first_name, middle_name, birth_date, address, phone_number, email, salary, login, password):
        self.id = int(id)
        self.__role = int(role)
        self.job = str(job)
        self.last_name = str(last_name)
        self.first_name = str(first_name)
        self.middle_name = str(middle_name)
        self.birth_date = birth_date
        self.address = str(address)
        self.phone_number = str(phone_number)
        self.email = str(email)
        self.salary = int(salary)
        self.login = str(login)
        self.password = str(password)

    def __get_role_name(self):
        if self.role == UserRole.MANAGER:
            return "Менеджер"
        elif self.role == UserRole.BOSS:
            return "Босс"
        else:
            return "Неизвестно"
