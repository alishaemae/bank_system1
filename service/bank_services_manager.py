from PyQt6.QtWidgets import QMessageBox
from data.account import Account
from data.card import Card
from data.deposit import Deposit
from data.credit import Credit
from data.client import Client
from service.database_manager import DatabaseManager


class BankServicesManager:
    def get_accounts_for_client(self, id_client):
        database_manager = DatabaseManager()
        query = database_manager.get_accounts_for_client_db(id_client)
        if query.error is None:
            result = query.result
            if result:
                accounts = [Account(
                    id=row[0],
                    client=Client(
                        id=row[1],
                        employee=None, last_name=None, first_name=None, middle_name=None, birth_date=None, phone_number=None, registration_address=None, residential_address=None, email=None, passport_number=0, passport_issue_date=None, inn=0
                    ),
                    type=row[2],
                    number=row[3],
                    currency=row[4],
                    balance=row[5],
                    opened_date=row[6],
                    closed_date=row[7],
                    status=row[8]
                ) for row in result]
                return accounts
            else:
                return None
        else:
            QMessageBox.critical(
                None, "Ошибка", f"Ошибка подключения к базе данных: {query.error}")
            return None

    def get_cards_for_client(self, id_client):
        database_manager = DatabaseManager()
        query = database_manager.get_cards_for_client_db(id_client)
        if query.error is None:
            result = query.result
            if result:
                cards = [Card(
                    id=row[0],
                    client=Client(
                        id=row[1],
                        employee=None, last_name=None, first_name=None, middle_name=None, birth_date=None, phone_number=None, registration_address=None, residential_address=None, email=None, passport_number=0, passport_issue_date=None, inn=0
                    ),
                    account=Account(
                        number=row[2],
                        currency=row[3],
                        client=None, type=None, id=0, balance=None, opened_date=None, closed_date=None, status=None
                    ),
                    type=row[4],
                    number=row[5],
                    expiration_date=row[6],
                    credit_limit=row[7],
                    opened_date=row[8],
                    closed_date=row[9],
                    status=row[10]
                ) for row in result]
                return cards
            else:
                return None
        else:
            QMessageBox.critical(
                None, "Ошибка", f"Ошибка подключения к базе данных: {query.error}")
            return None

    def get_deposits_for_client(self, id_client):
        database_manager = DatabaseManager()
        query = database_manager.get_deposits_for_client_db(id_client)
        if query.error is None:
            result = query.result
            if result:
                deposits = [Deposit(
                    id=row[0],
                    client=Client(
                        id=row[1],
                        employee=None, last_name=None, first_name=None, middle_name=None, birth_date=None, phone_number=None, registration_address=None, residential_address=None, email=None, passport_number=0, passport_issue_date=None, inn=0
                    ),
                    type=row[2],
                    amount=row[3],
                    due_date=row[4],
                    interest_rate=row[5],
                    early_withdrawal_allowed=row[6],
                    opened_date=row[7],
                    closed_date=row[8],
                    status=row[9]
                ) for row in result]
                return deposits
            else:
                return None
        else:
            QMessageBox.critical(
                None, "Ошибка", f"Ошибка подключения к базе данных: {query.error}")
            return None

    def get_credits_for_client(self, id_client):
        database_manager = DatabaseManager()
        query = database_manager.get_credits_for_client_db(id_client)
        if query.error is None:
            result = query.result
            if result:
                credits = [Credit(
                    id=row[0],
                    client=Client(
                        id=row[1],
                        employee=None, last_name=None, first_name=None, middle_name=None, birth_date=None, phone_number=None, registration_address=None, residential_address=None, email=None, passport_number=0, passport_issue_date=None, inn=0
                    ),
                    type=row[2],
                    amount=row[3],
                    due_date=row[4],
                    interest_rate=row[5],
                    monthly_payment=row[6],
                    penalty_rate=row[7],
                    opened_date=row[8],
                    closed_date=row[9],
                    status=row[10]
                ) for row in result]
                return credits
            else:
                return None
        else:
            QMessageBox.critical(
                None, "Ошибка", f"Ошибка подключения к базе данных: {query.error}")
            return None
