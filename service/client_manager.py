from PyQt6.QtWidgets import QMessageBox
from service.database_manager import DatabaseManager
from data.client import Client
from data.user import User


class ClientManager:
    def get_clients(self, id_employee, role):
        database_manager = DatabaseManager()
        query = database_manager.get_clients_db(id_employee, role)
        if query.error is None:
            result = query.result
            if result:
                clients = [Client(
                    id=row[0],
                    employee=User(
                        id=row[1],
                        role=row[2],
                        job=row[3],
                        last_name=row[4],
                        first_name=row[5],
                        middle_name=row[6],
                        birth_date=None, address=None, phone_number=None, email=None, salary=0, login=None, password=None
                    ),
                    last_name=row[7],
                    first_name=row[8],
                    middle_name=row[9],
                    birth_date=row[10],
                    phone_number=row[11],
                    registration_address=row[12],
                    residential_address=row[13],
                    email=row[14],
                    passport_number=row[15],
                    passport_issue_date=row[16],
                    inn=row[17],
                ) for row in result]
                return clients
            else:
                return None
        else:
            QMessageBox.critical(
                None, "Ошибка", f"Ошибка подключения к базе данных: {query.error}")
            return None

    def get_client_info(self, id_client):
        database_manager = DatabaseManager()
        query = database_manager.get_client_info_db(id_client)
        if query.error is None:
            result = query.result
            if result:
                client = Client(
                    id=result[0],
                    employee=User(
                        id=result[1],
                        role=result[2],
                        job=result[3],
                        last_name=result[4],
                        first_name=result[5],
                        middle_name=result[6],
                        birth_date=None, address=None, phone_number=None, email=None, salary=0, login=None, password=None
                    ),
                    last_name=result[7],
                    first_name=result[8],
                    middle_name=result[9],
                    birth_date=result[10],
                    phone_number=result[11],
                    registration_address=result[12],
                    residential_address=result[13],
                    email=result[14],
                    passport_number=result[15],
                    passport_issue_date=result[16],
                    inn=result[17],
                )
                return client
            else:
                return None
        else:
            QMessageBox.critical(
                None, "Ошибка", f"Ошибка подключения к базе данных: {query.error}")
            return None
