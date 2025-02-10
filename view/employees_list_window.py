from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QPushButton, QWidget, QTableWidget, QTableWidgetItem
)

class EmployeesListWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Тестовые данные
        self.staffs = [
            DummyStaff("Иванов", "Иван", "Иванович", "Бухгалтер", "Сотрудник", "+7 (111) 222-3333"),
            DummyStaff("Петров", "Петр", "Петрович", "Менеджер", "Руководитель", "+7 (222) 333-4444"),
            DummyStaff("Сидоров", "Сидор", "Сидорович", "Аналитик", "Специалист", "+7 (333) 444-5555"),
        ]
        self.ui_staffs_info_window()
    
    def ui_staffs_info_window(self):
        self.setWindowTitle("Управление сотрудниками")
        self.setFixedSize(801, 478)

        # Таблица сотрудников
        self.staffs_table = QtWidgets.QTableWidget(self)
        self.staffs_table.setGeometry(QtCore.QRect(20, 70, 761, 343))
        self.staffs_table.setColumnCount(4)
        self.staffs_table.setHorizontalHeaderLabels(["ФИО", "Должность", "Роль", "Телефон"])
        self.staffs_table.setColumnWidth(0, 230)
        self.staffs_table.setColumnWidth(1, 150)
        self.staffs_table.setColumnWidth(2, 165)
        self.staffs_table.setColumnWidth(3, 199)
        self.staffs_table.setStyleSheet("border: 1px solid rgb(30, 138, 86);")

 
        self.staffs_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.staffs_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.staffs_table.setRowCount(len(self.staffs))

        for i, staff in enumerate(self.staffs):
            item_full_name = QTableWidgetItem(f"{staff.last_name} {staff.first_name} {staff.middle_name}")
            item_full_name.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.staffs_table.setItem(i, 0, item_full_name)

            item_job = QTableWidgetItem(f"{staff.job}")
            item_job.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.staffs_table.setItem(i, 1, item_job)

            item_role = QTableWidgetItem(f"{staff.role_name}")
            item_role.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.staffs_table.setItem(i, 2, item_role)

            item_phone = QTableWidgetItem(f"{staff.phone_number}")
            item_phone.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.staffs_table.setItem(i, 3, item_phone)

        # Кнопка "Добавить сотрудника"
        self.add_staff_button = QPushButton("Добавить сотрудника", self)
        self.add_staff_button.setFixedSize(160, 25)
        self.add_staff_button.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        self.add_staff_button.setGeometry(QtCore.QRect(620, 20, 160, 25))
            
        # Кнопка "Назад"
        self.back_button = QPushButton("Назад", self)
        self.back_button.setFixedSize(60, 25)
        self.back_button.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        self.back_button.setGeometry(QtCore.QRect(720, 433, 60, 25))


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
    sys.exit(app.exec_())