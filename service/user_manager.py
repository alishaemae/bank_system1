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
        # Инициализируем объект для работы с базой данных
        data_service = DatabaseManager()
        # Выполняем запрос к базе данных для получения данных пользователя по заданному логину
        query = data_service.get_user_db(login)

        # Если запрос выполнен без ошибок
        if query.error is None:
            # Извлекаем результат запроса (данные пользователя)
            result = query.result
            # Если результат не пустой (пользователь найден)
            if result:
                # Извлекаем хэшированный пароль из результата запроса (на позиции 12)
                hashed_password = result[12]
                # Сравниваем введённый пароль (закодированный в UTF-8) с хэшированным паролем с помощью bcrypt
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    # Если пароли совпадают, создаем экземпляр пользователя и сохраняем его в приватном поле __user
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
                    # Если пароль не совпадает, возвращаем сообщение об ошибке
                    return "Неверный пароль"
                # Проверяем, что роль пользователя входит в допустимый диапазон (от 1 до количества определенных ролей)
                if self.__user.role > len(UserRole) or self.__user.role < 1:
                    # Если роль некорректна, сбрасываем сохраненного пользователя и возвращаем сообщение об ошибке
                    self.__user = None
                    return "Неизвестная роль пользователя"
                # Если все проверки пройдены успешно, возвращаем пустую строку, что означает отсутствие ошибок
                return ""
            else:
                # Если пользователь по заданному логину не найден, возвращаем соответствующее сообщение
                return "Пользователь не найден"
        else:
            # Если при выполнении запроса произошла ошибка подключения к базе данных, возвращаем сообщение об ошибке
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

    def check_exist_login(self, login):
        data_service = DatabaseManager()
        query = data_service.check_exist_login_db(login)
        if query.error is None:
            result = query.result
            if result:
                user = User(
                    id=result[0],
                    role=result[1],
                    login=result[2],
                    job=None, last_name=None, first_name=None, middle_name=None, birth_date=None, address=None, phone_number=None, email=None, salary=0, password=None
                )
                return user
            else:
                return None
        else:
            return None

    def add_employee(self, login, password, role, last_name, first_name, middle_name, job, birth_date, address, phone_number, email, salary):
        data_service = DatabaseManager()
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())
        translations = {
            "Менеджер": "MANAGER",
            "Начальник": "BOSS"
        }
        role = UserRole[translations.get(role, role)].value
        query = data_service.add_employee_db(login, hashed_password, role, last_name,
                                             first_name, middle_name, job, birth_date, address, phone_number, email, salary)
        if query.error is None:
            return ""
        else:
            return f"Ошибка подключения к базе данных: {query.error}"
