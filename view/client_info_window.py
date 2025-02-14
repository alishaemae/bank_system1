# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QDialog, QWidget, QScrollBar, QListWidget, QListWidgetItem, QTabWidget, QApplication, QVBoxLayout, QTableWidget, QTableWidgetItem
)
from service.client_manager import ClientManager
from service.user_manager import UserManager
from service.bank_services_manager import BankServicesManager
from view.client_info_w_controller import *


class ClientInfoWindow(QDialog):
    def __init__(self, id_client):
        super().__init__()
        self.user = UserManager().authorised_user
        self.client = ClientManager().get_client_info(id_client)
        self.ui_client_info_window()

    def ui_client_info_window(self):
        self.setWindowTitle("Информация о клиенте")
        self.setFixedSize(568, 319)

        self.custom_scroll = QScrollBar(self)
        self.custom_scroll.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.custom_scroll.setGeometry(0, 0, 16, 318)

        self.list_widget = QListWidget(self)
        self.list_widget.setGeometry(QtCore.QRect(16, 0, 285, 318))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_widget.setFont(font)
        self.list_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        internal_scroll = self.list_widget.verticalScrollBar()
        internal_scroll.rangeChanged.connect(self.custom_scroll.setRange)
        self.custom_scroll.valueChanged.connect(internal_scroll.setValue)
        internal_scroll.valueChanged.connect(self.custom_scroll.setValue)

        for _ in range(20):
            item = QListWidgetItem()
            item_font = QtGui.QFont()
            item_font.setPointSize(10)
            item_font.setWeight(50)
            item.setFont(item_font)
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
            self.list_widget.addItem(item)

        value_indices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        for idx in value_indices:
            item = self.list_widget.item(idx)
            item.setForeground(QtGui.QBrush(QtGui.QColor(30, 138, 86)))
            font_item = item.font()
            font_item.setBold(True)
            item.setFont(font_item)

        self.list_widget.item(0).setText("ФИО:")
        self.list_widget.item(1).setText(self.client.full_name)
        self.list_widget.item(2).setText("Менеджер:")
        self.list_widget.item(3).setText(self.client.employee.full_name)
        self.list_widget.item(4).setText("Дата рождения:")
        self.list_widget.item(5).setText(format_date(self.client.birth_date))
        self.list_widget.item(6).setText("Номер телефона:")
        self.list_widget.item(7).setText(self.client.phone_number)
        self.list_widget.item(8).setText("Адрес регистрации:")
        self.list_widget.item(9).setText(self.client.registration_address)
        self.list_widget.item(10).setText("Адрес проживания:")
        self.list_widget.item(11).setText(self.client.residential_address)
        self.list_widget.item(12).setText("E-mail:")
        self.list_widget.item(13).setText(self.client.email)
        self.list_widget.item(14).setText("Серия и номер паспорта:")
        self.list_widget.item(15).setText(str(self.client.passport_number))
        self.list_widget.item(16).setText("Дата выдачи паспорта:")
        self.list_widget.item(17).setText(format_date(self.client.passport_issue_date))
        self.list_widget.item(18).setText("ИНН:")
        self.list_widget.item(19).setText(str(self.client.inn))
        
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setGeometry(QtCore.QRect(301, 0, 268, 318))

        self.tab = QWidget()
        self.tab_widget.addTab(self.tab, "Счета")

        self.tab_2 = QWidget()
        self.tab_widget.addTab(self.tab_2, "Карты")

        self.tab_3 = QWidget()
        self.tab_widget.addTab(self.tab_3, "Депозиты")

        self.tab_4 = QWidget()
        self.tab_widget.addTab(self.tab_4, "Кредиты")

        services_manager = BankServicesManager()

        accounts = services_manager.get_accounts_for_client(self.client.id)
        cards = services_manager.get_cards_for_client(self.client.id)
        deposits = services_manager.get_deposits_for_client(self.client.id)
        credits = services_manager.get_credits_for_client(self.client.id)

        # --- Счета ---
        layout_accounts = QVBoxLayout(self.tab)
        layout_accounts.setContentsMargins(0, 0, 0, 0)
        accounts_list = QListWidget(self.tab)
        layout_accounts.addWidget(accounts_list)
        if accounts:
            for account in accounts:
                accounts_list.addItem(f"Тип: {account.type}")
                accounts_list.addItem(f"Номер: {account.number}")
                accounts_list.addItem(f"Валюта: {account.currency}")
                accounts_list.addItem(f"Баланс: {account.balance}")
                accounts_list.addItem(f"Дата открытия: {format_date(account.opened_date)}")
                if account.closed_date:
                    accounts_list.addItem(f"Дата закрытия: {format_date(account.closed_date)}")
                if account.status_name == "Активен":
                    status_item = QListWidgetItem(f"Статус: {account.status_name}")
                    status_item.setForeground(QtGui.QBrush(QtGui.QColor(30, 138, 86)))
                    accounts_list.addItem(status_item)
                else:
                    status_item = QListWidgetItem(f"Статус: {account.status_name}")
                    status_item.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
                    accounts_list.addItem(status_item)
                accounts_list.addItem("-" * 44)
        else:
            accounts_list.addItem("Нет данных по счетам")

        # --- Карты ---
        layout_cards = QVBoxLayout(self.tab_2)
        layout_cards.setContentsMargins(0, 0, 0, 0)
        cards_list = QListWidget(self.tab_2)
        layout_cards.addWidget(cards_list)
        if cards:
            for card in cards:
                cards_list.addItem(f"Тип: {card.type}")
                cards_list.addItem(f"Номер карты: {str(card.number)[:4]}{'*'*8}{str(card.number)[-4:]}")
                cards_list.addItem(f"Счет: {card.account.number}")
                cards_list.addItem(f"Срок действия: {format_date(card.expiration_date)}")
                if card.credit_limit != 0.00:
                    cards_list.addItem(f"Кредитный лимит: {card.credit_limit}")
                cards_list.addItem(f"Дата открытия: {format_date(card.opened_date)}")
                if card.closed_date:
                    cards_list.addItem(f"Дата закрытия: {format_date(card.closed_date)}")
                if card.status_name == "Активна":
                    status_item = QListWidgetItem(f"Статус: {card.status_name}")
                    status_item.setForeground(QtGui.QBrush(QtGui.QColor(30, 138, 86)))
                    cards_list.addItem(status_item)
                else:
                    status_item = QListWidgetItem(f"Статус: {card.status_name}")
                    status_item.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
                    cards_list.addItem(status_item)
                cards_list.addItem("-" * 44)
        else:
            cards_list.addItem("Нет данных по картам")

        # --- Депозиты ---
        layout_deposits = QVBoxLayout(self.tab_3)
        layout_deposits.setContentsMargins(0, 0, 0, 0)
        deposits_list = QListWidget(self.tab_3)
        layout_deposits.addWidget(deposits_list)
        if deposits:
            for deposit in deposits:
                deposits_list.addItem(f"Тип: {deposit.type}")
                deposits_list.addItem(f"Сумма: {deposit.amount}")
                deposits_list.addItem(f"Дата погашения: {format_date(deposit.due_date)}")
                deposits_list.addItem(f"Процентная ставка: {deposit.interest_rate}")
                deposits_list.addItem(f"Досрочное снятие: {deposit.early_withdrawal_allowed}")
                deposits_list.addItem(f"Дата открытия: {format_date(deposit.opened_at)}")
                if deposit.closed_at:
                    deposits_list.addItem(f"Дата закрытия: {format_date(deposit.closed_at)}")
                if deposit.status_name == "Активен":
                    status_item = QListWidgetItem(f"Статус: {deposit.status_name}")
                    status_item.setForeground(QtGui.QBrush(QtGui.QColor(30, 138, 86)))
                    deposits_list.addItem(status_item)
                else:
                    status_item = QListWidgetItem(f"Статус: {deposit.status_name}")
                    status_item.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
                    deposits_list.addItem(status_item)
                deposits_list.addItem("-" * 44)
        else:
            deposits_list.addItem("Нет данных по депозитам")

        # --- Кредиты ---
        layout_credits = QVBoxLayout(self.tab_4)
        layout_credits.setContentsMargins(0, 0, 0, 0)
        credits_list = QListWidget(self.tab_4)
        layout_credits.addWidget(credits_list)
        if credits:
            for credit in credits:
                credits_list.addItem(f"Тип: {credit.type}")
                credits_list.addItem(f"Сумма: {credit.amount}")
                credits_list.addItem(f"Дата погашения: {format_date(credit.due_date)}")
                credits_list.addItem(f"Процентная ставка: {credit.interest_rate}")
                credits_list.addItem(f"Месячный платеж: {credit.monthly_payment}")
                credits_list.addItem(f"Пеня: {credit.penalty_rate}")
                credits_list.addItem(f"Дата открытия: {format_date(credit.opened_at)}")
                if credit.closed_at:
                    credits_list.addItem(f"Дата закрытия: {format_date(credit.closed_at)}")
                if credit.status_name == "Активен":
                    status_item = QListWidgetItem(f"Статус: {credit.status_name}")
                    status_item.setForeground(QtGui.QBrush(QtGui.QColor(30, 138, 86)))
                    credits_list.addItem(status_item)
                else:
                    status_item = QListWidgetItem(f"Статус: {credit.status_name}")
                    status_item.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
                    credits_list.addItem(status_item)
                credits_list.addItem("-" * 44)
        else:
            credits_list.addItem("Нет данных по кредитам")


# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     # Не забудьте передать id клиента
#     form = ClientInfoWindow(id_client=1)
#     form.show()
#     sys.exit(app.exec())