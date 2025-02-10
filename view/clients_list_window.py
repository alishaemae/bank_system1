from PyQt6.QtWidgets import QWidget, QPushButton, QTableWidget, QComboBox, QLineEdit, QStatusBar, QHBoxLayout
from PyQt6 import QtCore
from service.user_manager import UserManager
from view.clients_list_w_controller import *

class ClientsListWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.user = UserManager().authorised_user
        self.ui_clients_list_window()

    def ui_clients_list_window(self):
        self.setWindowTitle("Главное окно")
        self.setFixedSize(801, 478)

        # Верхняя область с кнопками
        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 761, 25))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.back_button = QPushButton("Личный кабинет", self)
        self.back_button.setFixedSize(130, 25)
        self.back_button.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        # Позиционируем кнопку в правом нижнем углу (отступ 20 пикселей)
        self.back_button.move(650, 20)
        self.back_button.clicked.connect(lambda: open_user_info_window(self))

        # Кнопка "Создать отчет"
        self.back_button = QPushButton("Создать отчет", self)
        self.back_button.setFixedSize(110, 25)
        self.back_button.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        self.back_button.setGeometry(QtCore.QRect(20, 433, 60, 25))

        self.back_button = QPushButton("Выйти", self)
        self.back_button.setFixedSize(60, 25)
        self.back_button.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        # Позиционируем кнопку в правом нижнем углу (отступ 20 пикселей)
        self.back_button.move(720, 433)
        self.back_button.clicked.connect(lambda: open_auth_window(self))

        # Таблица клиентов
        self.clients_table = QTableWidget(self)
        self.clients_table.setGeometry(QtCore.QRect(20, 70, 761, 343))
        self.clients_table.setColumnCount(4)
        self.clients_table.setHorizontalHeaderLabels(["ФИО", "Дата рождения", "Телефон", "Е-mail"])
        self.clients_table.setColumnWidth(0, 240)
        self.clients_table.setColumnWidth(1, 150)
        self.clients_table.setColumnWidth(2, 170)
        self.clients_table.setColumnWidth(3, 199)
        self.clients_table.setStyleSheet("border: 1px solid rgb(30, 138, 86);")
        self.clients_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.clients_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.clients_table.cellDoubleClicked.connect(lambda: open_client_info_window(self))

        # Панель поиска
        self.horizontalLayoutWidget_2 = QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 35, 357, 39))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.comboBox = QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox.addItem("Выберите")
        self.horizontalLayout_2.addWidget(self.comboBox)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setFixedSize(150, 20)
        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.search_btn = QPushButton("Поиск", self.horizontalLayoutWidget_2)
        self.search_btn.setFixedSize(45, 20)
        self.search_btn.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 15x; color: white; border: 0; border-radius: 4px;")
        self.horizontalLayout_2.addWidget(self.search_btn)
