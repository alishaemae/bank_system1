from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QHBoxLayout, QPushButton
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class StaffListWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление персоналом")
        self.setFixedSize(801, 478)
        self.setupUi()

    def setupUi(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(90, 10, 90, 30)
        main_layout.setSpacing(10)

        # Заголовок
        self.title_label = QLabel("Список сотрудников", self)
        title_font = QFont()
        title_font.setPointSize(15)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setFixedHeight(45)
        # По примеру info окна, без границ
        self.title_label.setStyleSheet("border: none;")
        main_layout.addWidget(self.title_label)

        # Таблица сотрудников
        self.staffs_table = QTableWidget(self)
        self.staffs_table.setColumnCount(4)
        self.staffs_table.setHorizontalHeaderLabels(["ФИО", "Должность", "Роль", "Телефон"])
        # Настройки ширины колонок
        self.staffs_table.setColumnWidth(0, 210)
        self.staffs_table.setColumnWidth(1, 130)
        self.staffs_table.setColumnWidth(2, 120)
        self.staffs_table.setColumnWidth(3, 150)
        # Выравнивание содержимого и запрет редактирования
        self.staffs_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.staffs_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        main_layout.addWidget(self.staffs_table)

        # Нижний горизонтальный layout для кнопок
        bottom_layout = QHBoxLayout()
        # Кнопка "Добавить сотрудника" слева
        self.add_staff_button = QPushButton("Добавить сотрудника", self)
        self.add_staff_button.setFixedSize(150, 25)
        self.add_staff_button.setStyleSheet(
            "background-color: #7b99ca; font-size: 14px; color: white; border: none; border-radius: 5px;"
        )
        bottom_layout.addWidget(self.add_staff_button)

        bottom_layout.addStretch()

        # Кнопка "Назад" справа
        self.back_button = QPushButton("Назад", self)
        self.back_button.setFixedSize(60, 25)
        self.back_button.setStyleSheet(
            "background-color: #7b99ca; font-size: 14px; color: white; border: none; border-radius: 5px;"
        )
        bottom_layout.addWidget(self.back_button)

        main_layout.addLayout(bottom_layout)


# Test data and standalone launch
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

    # Создаем тестовых сотрудников
    staffs = [
        DummyStaff("Иванов", "Иван", "Иванович", "Бухгалтер", "Сотрудник", "+7 (111) 222-3333"),
        DummyStaff("Петров", "Петр", "Петрович", "Менеджер", "Руководитель", "+7 (222) 333-4444"),
        DummyStaff("Сидоров", "Сидор", "Сидорович", "Аналитик", "Специалист", "+7 (333) 444-5555"),
    ]

    app = QApplication(sys.argv)
    window = StaffListWindow()
    
    # Заполняем таблицу тестовыми данными
    window.staffs_table.setRowCount(len(staffs))
    for i, staff in enumerate(staffs):
        full_name = f"{staff.last_name} {staff.first_name} {staff.middle_name}"
        item_full_name = QTableWidgetItem(full_name)
        item_full_name.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        window.staffs_table.setItem(i, 0, item_full_name)

        item_job = QTableWidgetItem(staff.job)
        item_job.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        window.staffs_table.setItem(i, 1, item_job)

        item_role = QTableWidgetItem(staff.role_name)
        item_role.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        window.staffs_table.setItem(i, 2, item_role)

        item_phone = QTableWidgetItem(staff.phone_number)
        item_phone.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        window.staffs_table.setItem(i, 3, item_phone)

    window.show()
    sys.exit(app.exec())