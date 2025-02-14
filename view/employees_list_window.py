from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QPushButton, QWidget, QTableWidget, QTableWidgetItem
)
from view.employees_list_w_controller import *
from service.user_manager import UserManager


class EmployeesListWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.user = UserManager().authorised_user
        self.employees = UserManager().get_employees()
        if self.employees is None:
            self.employees = []
        else:
            self.employees = [
                employee for employee in self.employees if employee.id != self.user.id]
            self.employees = sorted(
                self.employees, key=lambda employee: employee.last_name)
        self.ui_employees_list_window()

    def ui_employees_list_window(self):
        self.setWindowTitle("Управление сотрудниками")
        self.setFixedSize(801, 478)

        # Таблица сотрудников
        self.employees_table = QTableWidget(self)
        self.employees_table.setGeometry(QtCore.QRect(20, 70, 761, 343))
        self.employees_table.setColumnCount(4)
        self.employees_table.setHorizontalHeaderLabels(
            ["ФИО", "Должность", "Роль", "Телефон"])
        self.employees_table.setColumnWidth(0, 230)
        self.employees_table.setColumnWidth(1, 150)
        self.employees_table.setColumnWidth(2, 165)
        self.employees_table.setColumnWidth(3, 199)

        self.employees_table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows)
        self.employees_table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers)
        self.employees_table.setRowCount(len(self.employees))

        for i, employee in enumerate(self.employees):
            item_full_name = QTableWidgetItem(
                f"{employee.last_name} {employee.first_name} {employee.middle_name}")
            item_full_name.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.employees_table.setItem(i, 0, item_full_name)

            item_job = QTableWidgetItem(f"{employee.job}")
            item_job.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.employees_table.setItem(i, 1, item_job)

            item_role = QTableWidgetItem(f"{employee.role_name}")
            item_role.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.employees_table.setItem(i, 2, item_role)

            item_phone = QTableWidgetItem(f"{employee.phone_number}")
            item_phone.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.employees_table.setItem(i, 3, item_phone)

        self.employees_table.cellDoubleClicked.connect(lambda: open_employee_info_window(
            self, self.employees[self.employees_table.currentRow()]))

        self.add_employee_button = QPushButton("Добавить сотрудника", self)
        self.add_employee_button.setFixedSize(160, 25)
        self.add_employee_button.setStyleSheet(
            "background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        self.add_employee_button.setGeometry(QtCore.QRect(620, 10, 160, 25))
        self.add_employee_button.clicked.connect(
            lambda: open_add_employee_window(self))

        self.back_button = QPushButton("Назад", self)
        self.back_button.setFixedSize(60, 25)
        self.back_button.setStyleSheet(
            "background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        self.back_button.setGeometry(QtCore.QRect(720, 433, 60, 25))
        self.back_button.clicked.connect(
            lambda: open_clients_list_window(self))

