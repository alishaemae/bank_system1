from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QDialog, QPushButton, QComboBox,
    QLineEdit, QDateEdit, QLabel
)
from view.create_report_w_controller import *
from PyQt6.QtCore import QDate


class CreateReportWindow(QDialog):
    def __init__(self, clients):
        super().__init__()
        self.clients = clients
        self.ui_create_report_window()

    def ui_create_report_window(self):
        self.resize(400, 250)
        self.setWindowTitle("Создание отчёта")

        self.create_report_button = QPushButton(self)
        self.create_report_button.setGeometry(QtCore.QRect(120, 200, 160, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.create_report_button.setFont(font)
        self.create_report_button.setStyleSheet(
            "background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;"
        )
        self.create_report_button.setText("Создать отчет")
        self.create_report_button.clicked.connect(lambda: create_report(self))

        self.client_line_edit = QLineEdit(self)
        self.client_line_edit.setGeometry(QtCore.QRect(20, 40, 201, 20))
        self.client_line_edit.setPlaceholderText("Введите ФИО клиента")

        self.filter_combo_box = QComboBox(self)
        self.filter_combo_box.setGeometry(QtCore.QRect(240, 40, 130, 22))
        self.filter_combo_box.addItems(
            ["Выбрать все", "Счета", "Карты", "Депозиты", "Кредиты"])

        self.start_date_edit = QDateEdit(self)
        self.start_date_edit.setGeometry(QtCore.QRect(40, 110, 110, 22))
        self.start_date_edit.setCalendarPopup(True)

        self.end_date_edit = QDateEdit(self)
        self.end_date_edit.setGeometry(QtCore.QRect(240, 110, 110, 22))
        self.end_date_edit.setCalendarPopup(True)
        self.end_date_edit.setDate(QDate.currentDate())

        self.date_label = QLabel(self)
        self.date_label.setGeometry(QtCore.QRect(130, 80, 260, 16))
        self.date_label.setText("Выберите период")
