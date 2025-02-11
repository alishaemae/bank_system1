import bcrypt
import sys
import os
from data.user import *
from service.database_manager import DatabaseManager
from service.singleton import SingletonMeta

class UserManager(metaclass=SingletonMeta):
    __user: User = None

    @property
    def authorised_user(self):
        return self.__user
    
    def get_user(self, login, password):
        data_service = DatabaseManager()
        query = data_service.get_user_db(login)
        if query.error is None:
            result = query.result   
            if result:
                hashed_password = result[12]
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    self.__user = User(
                        id=result[0],
                        role=result[1],
                        job=result[2],
                        last_name=result[3],
                        first_name=result[4],
                        middle_name=result[5],
                        birth_date=result[6],
                        address=result[7],
                        phone_number=result[8],
                        email=result[9],
                        salary=result[10],
                        login=result[11],
                        password=result[12]
                        )
                else:
                    return "Неверный пароль"
                if self.__user.role > len(UserRole) or self.__user.role < 1:
                    self.__user = None
                    return "Неизвестная роль пользователя"
                return ""
            else:
                return "Пользователь не найден"
        else:
            return "Ошибка подключения к базе данных"
    
    def get_employees(self):
        data_service = DatabaseManager()
        query = data_service.get_employees_db()
        if query.error is None:
            result = query.result
            if result:
                employees = [User(
                    id=row[0],
                    role=row[1],
                    job=row[2],
                    last_name=row[3],
                    first_name=row[4],
                    middle_name=row[5],
                    birth_date=row[6],
                    address=row[7],
                    phone_number=row[8],
                    email=row[9],
                    salary=row[10],
                    login=row[11],
                    password=None
                ) for row in result]
                return employees
            else:
                return "Сотрудники не найдены"
        else:
            return f"Ошибка подключения к базе данных: {query.error}"
    
    def update_deleted_status_employee(self, id_employee):
        data_service = DatabaseManager()
        query = data_service.update_deleted_status_employee_db(id_employee)
        if query.error is None:
            return ""
        else:
            return f"Ошибка подключения к базе данных: {query.error}"

    # def check_exist_login(self, login):
    #     data_service = DatabaseService()
    #     query = data_service.check_exist_login_db(login)
    #     if query.error is None:
    #         result = query.result
    #         if result:
    #             user = User(
    #                 id_staff=result[0],
    #                 last_name=result[1],
    #                 first_name=result[2],
    #                 middle_name=result[3],
    #                 login=result[4],
    #                 password=result[5],
    #                 role=result[6], job=None, birth_date=None, address=None, phone_number=None, salary=0
    #             )
    #             return user
    #         else:
    #             return None
    #     else:
    #         return None


    
    # def add_staff(self, login, password, role, last_name, first_name, middle_name, job, birth_date, address, phone_number, salary):
    #     data_service = DatabaseService()
    #     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    #     role = UserRole[role].value
    #     query = data_service.add_staff_db(login, hashed_password, role, last_name, first_name, middle_name, job, birth_date, address, phone_number, salary)
    #     if query.error is None:
    #         return ""
    #     else:
    #         return f"Ошибка подключения к базе данных: {query.error}"
    
    # def get_staff_info_by_login(self, login):
    #     data_service = DatabaseService()
    #     query = data_service.get_user_db(login)
    #     if query.error is None:
    #         result = query.result
    #         if result:
    #             staff = User(
    #                 id_staff=result[0],
    #                 role=result[1],
    #                 job=result[2],
    #                 last_name=result[3],
    #                 first_name=result[4],
    #                 middle_name=result[5],
    #                 birth_date=result[6],
    #                 address=result[7],
    #                 phone_number=result[8],
    #                 salary=result[9],
    #                 login=result[10],
    #                 password=result[11])
    #             return staff
    #         else:
    #             return None
    #     else:
    #         return None
        
    # def update_staff(self, login, password, role, last_name, first_name, middle_name, job, birth_date, address, phone_number, salary):
    #     data_service = DatabaseService()
    #     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    #     role = UserRole[role].value
    #     query = data_service.update_staff_db(login, hashed_password, role, last_name, first_name, middle_name, job, birth_date, address, phone_number, salary)
    #     if query.error is None:
    #         return ""
    #     else:
    #         return f"Ошибка подключения к базе данных: {query.error}"