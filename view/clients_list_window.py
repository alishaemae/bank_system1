from PyQt6.QtWidgets import QWidget, QPushButton, QTableWidget, QTableWidgetItem, QComboBox, QLineEdit, QStatusBar, QHBoxLayout
from PyQt6 import QtCore
from service.user_manager import UserManager, UserRole
from service.client_manager import ClientManager
from view.clients_list_w_controller import *

class ClientsListWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.user = UserManager().authorised_user
        self.clients = ClientManager().get_clients(self.user.id, self.user.role)
        if self.clients is None:
            self.clients = []
        else:
            self.clients = sorted(self.clients, key=lambda client: client.full_name)   
        self.ui_clients_list_window()

    def ui_clients_list_window(self):
        self.setWindowTitle("Главное окно")
        self.setFixedSize(801, 478)

        # Если пользователь - руководитель, то добавляем кнопку "Управление сотрудниками"
        if self.user.role == UserRole.BOSS:
            self.employees_button = QPushButton("Управление сотрудниками", self)
            self.employees_button.setFixedSize(190, 25)
            self.employees_button.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
            self.employees_button.setGeometry(QtCore.QRect(451, 10, 190, 25))
            self.employees_button.clicked.connect(lambda: open_employees_list_window(self))

        self.user_info_button = QPushButton("Личный кабинет", self)
        self.user_info_button.setFixedSize(130, 25)
        self.user_info_button.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        self.user_info_button.setGeometry(QtCore.QRect(651, 10, 130, 25))
        self.user_info_button.clicked.connect(lambda: open_user_info_window(self))
            
        # Кнопка "Создать отчет"
        self.report_button = QPushButton("Создать отчет", self)
        self.report_button.setFixedSize(110, 25)
        self.report_button.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        self.report_button.setGeometry(QtCore.QRect(20, 433, 60, 25))

        # Кнопка "Выйти"
        self.exit_button = QPushButton("Выйти", self)
        self.exit_button.setFixedSize(60, 25)
        self.exit_button.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        self.exit_button.move(720, 433)
        self.exit_button.clicked.connect(lambda: open_auth_window(self))

        # Таблица клиентов
        self.clients_table = QTableWidget(self)
        self.clients_table.setGeometry(QtCore.QRect(20, 70, 761, 343))
        self.clients_table.setColumnCount(4)
        self.clients_table.setHorizontalHeaderLabels(["ФИО", "Дата рождения", "Телефон", "Е-mail"])
        # self.clients_table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.clients_table.setColumnWidth(0, 225)
        self.clients_table.setColumnWidth(1, 150)
        self.clients_table.setColumnWidth(2, 170)
        self.clients_table.setColumnWidth(3, 199)
        self.clients_table.setStyleSheet("border: 1px solid rgb(30, 138, 86);")
        self.clients_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.clients_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.clients_table.cellDoubleClicked.connect(lambda: open_client_info_window(self, self.clients[self.clients_table.currentRow()].id))

        self.clients_table.setRowCount(len(self.clients))
        for i, client in enumerate(self.clients):
            item_full_name = QTableWidgetItem(client.full_name)
            item_full_name.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.clients_table.setItem(i, 0, item_full_name)

            item_birth_date = QTableWidgetItem(client.birth_date.strftime("%d.%m.%Y"))
            item_birth_date.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.clients_table.setItem(i, 1, item_birth_date)

            item_phone_number = QTableWidgetItem(client.phone_number)
            item_phone_number.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.clients_table.setItem(i, 2, item_phone_number)

            item_email = QTableWidgetItem(client.email)
            item_email.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.clients_table.setItem(i, 3, item_email)

        # Панель поиска
        self.horizontalLayoutWidget_2 = QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(16, 35, 320, 39))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setFixedSize(260, 20)
        self.lineEdit.setPlaceholderText("Введите фамилию/имя/отчество клиента")
        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.search_btn = QPushButton("Поиск", self.horizontalLayoutWidget_2)
        self.search_btn.setFixedSize(45, 20)
        self.search_btn.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 15x; color: white; border: 0; border-radius: 4px;")
        self.horizontalLayout_2.addWidget(self.search_btn)