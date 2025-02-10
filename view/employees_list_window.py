from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QPushButton, QWidget, QTableWidget, QTableWidgetItem
)
from view.employees_list_w_controller import *

class EmployeesListWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Тестовые данные
        self.employees = [
            DummyStaff("Иванов", "Иван", "Иванович", "Бухгалтер", "Сотрудник", "+7 (111) 222-3333"),
            DummyStaff("Петров", "Петр", "Петрович", "Менеджер", "Руководитель", "+7 (222) 333-4444"),
            DummyStaff("Сидоров", "Сидор", "Сидорович", "Аналитик", "Специалист", "+7 (333) 444-5555"),
        ]
        self.ui_employees_list_window()
    
    def ui_employees_list_window(self):
        self.setWindowTitle("Управление сотрудниками")
        self.setFixedSize(801, 478)

        # Таблица сотрудников
        self.employees_table = QTableWidget(self)
        self.employees_table.setGeometry(QtCore.QRect(20, 70, 761, 343))
        self.employees_table.setColumnCount(4)
        self.employees_table.setHorizontalHeaderLabels(["ФИО", "Должность", "Роль", "Телефон"])
        self.employees_table.setColumnWidth(0, 230)
        self.employees_table.setColumnWidth(1, 150)
        self.employees_table.setColumnWidth(2, 165)
        self.employees_table.setColumnWidth(3, 199)
        self.employees_table.setStyleSheet("border: 1px solid rgb(30, 138, 86);")

 
        self.employees_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.employees_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.employees_table.setRowCount(len(self.employees))

        for i, staff in enumerate(self.employees):
            item_full_name = QTableWidgetItem(f"{staff.last_name} {staff.first_name} {staff.middle_name}")
            item_full_name.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.employees_table.setItem(i, 0, item_full_name)

            item_job = QTableWidgetItem(f"{staff.job}")
            item_job.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.employees_table.setItem(i, 1, item_job)

            item_role = QTableWidgetItem(f"{staff.role_name}")
            item_role.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.employees_table.setItem(i, 2, item_role)

            item_phone = QTableWidgetItem(f"{staff.phone_number}")
            item_phone.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.employees_table.setItem(i, 3, item_phone)

        # Кнопка "Добавить сотрудника"
        self.add_employee_button = QPushButton("Добавить сотрудника", self)
        self.add_employee_button.setFixedSize(160, 25)
        self.add_employee_button.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        self.add_employee_button.setGeometry(QtCore.QRect(620, 20, 160, 25))
        self.add_employee_button.clicked.connect(lambda: open_add_employee_window(self))
            
        # Кнопка "Назад"
        self.back_button = QPushButton("Назад", self)
        self.back_button.setFixedSize(60, 25)
        self.back_button.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        self.back_button.setGeometry(QtCore.QRect(720, 433, 60, 25))
        self.back_button.clicked.connect(lambda: open_clients_list_window(self))


class DummyStaff:
    def __init__(self, last_name, first_name, middle_name, job, role_name, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.job = job
        self.role_name = role_name
        self.phone_number = phone_number

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = EmployeesListWindow()
    window.show()
    sys.exit(app.exec())