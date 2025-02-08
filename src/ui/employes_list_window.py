from PyQt6.QtWidgets import (
    QApplication, QPushButton, QVBoxLayout, QHBoxLayout, 
    QWidget, QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import Qt


class DummyStaff:
    def __init__(self, last_name, first_name, middle_name, job, role_name, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.job = job
        self.role_name = role_name
        self.phone_number = phone_number


class StaffListWindow(QWidget):
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
        self.setWindowTitle("Управление персоналом")
        self.setGeometry(400, 230, 680, 450)
        self.setFixedSize(680, 450)

        main_layout = QVBoxLayout(self)

        top_layout = QHBoxLayout()

        self.add_staff_button = QPushButton("Добавить сотрудника")
        self.add_staff_button.setFixedSize(150, 25)
        self.add_staff_button.setStyleSheet("background-color: #7b99ca; font-size: 14px; color: white; border: 0; border-radius: 5px;")
        top_layout.addWidget(self.add_staff_button)
        top_layout.addStretch()

        self.back_button = QPushButton("Назад")
        self.back_button.setFixedSize(60, 25)
        self.back_button.setStyleSheet("background-color: #7b99ca; font-size: 14px; color: white; border: 0; border-radius: 5px;")

        self.staffs_table = QTableWidget()
        self.staffs_table.setColumnCount(4)
        self.staffs_table.setColumnWidth(0, 210)
        self.staffs_table.setColumnWidth(1, 130)
        self.staffs_table.setColumnWidth(2, 120)
        self.staffs_table.setColumnWidth(3, 150)
        self.staffs_table.setHorizontalHeaderLabels(["ФИО", "Должность", "Роль", "Телефон"])
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
            
        exit_layout = QHBoxLayout()
        exit_layout.addStretch()
        exit_layout.addWidget(self.back_button)

        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.staffs_table)
        main_layout.addLayout(exit_layout)

        self.setLayout(main_layout)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = StaffListWindow()
    window.show()
    sys.exit(app.exec())