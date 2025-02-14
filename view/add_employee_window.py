from PyQt6.QtWidgets import (
    QApplication, QPushButton, QVBoxLayout, QHBoxLayout,
    QWidget, QLabel, QLineEdit, QComboBox
)
from PyQt6.QtCore import QRect
from view.add_employee_w_controller import *
from data.user import UserRole


class AddEmployeeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_add_employee_window()

    def ui_add_employee_window(self):
        self.setWindowTitle("Добавление сотрудника")
        self.setFixedSize(801, 478)

        self.add_employee_button = QPushButton("Добавить сотрудника", self)
        self.add_employee_button.setFixedSize(160, 25)
        self.add_employee_button.setStyleSheet(
            "background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 5px;")
        self.add_employee_button.setGeometry(QRect(620, 10, 160, 25))
        self.add_employee_button.clicked.connect(lambda: add_staff(self))

        self.back_button = QPushButton("Назад", self)
        self.back_button.setFixedSize(60, 25)
        self.back_button.setStyleSheet(
            "background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 5px;")
        self.back_button.setGeometry(QRect(720, 433, 60, 25))
        self.back_button.clicked.connect(
            lambda: open_employees_list_window(self))

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 30, 20, 60)
        main_layout.setSpacing(5)

        self.error_label = QLabel("", self)
        self.error_label.setFixedHeight(22)
        self.error_label.setStyleSheet("color: red; font-size: 14px;")
        self.error_label.setGeometry(QRect(20, 10, 350, 25))

        form_layout_left = QVBoxLayout()
        self.login_label = QLabel("Логин")
        self.login_input = QLineEdit()
        self.login_input.setFixedHeight(25)

        self.password_label = QLabel("Пароль")
        self.password_input = QLineEdit()
        self.password_input.setFixedHeight(25)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.role_label = QLabel("Роль")
        self.role_input = QComboBox()
        self.role_input.setFixedHeight(25)
        translations = {
            'MANAGER': 'Менеджер',
            'BOSS': 'Начальник'
        }
        self.role_input.addItems(
            [translations.get(role.name, role.name) for role in UserRole])

        self.last_name_label = QLabel("Фамилия")
        self.last_name_input = QLineEdit()
        self.last_name_input.setFixedHeight(25)

        self.first_name_label = QLabel("Имя")
        self.first_name_input = QLineEdit()
        self.first_name_input.setFixedHeight(25)

        self.middle_name_label = QLabel("Отчество")
        self.middle_name_input = QLineEdit()
        self.middle_name_input.setFixedHeight(25)

        form_layout_left.addWidget(self.login_label)
        form_layout_left.addWidget(self.login_input)
        form_layout_left.addWidget(self.password_label)
        form_layout_left.addWidget(self.password_input)
        form_layout_left.addWidget(self.role_label)
        form_layout_left.addWidget(self.role_input)
        form_layout_left.addWidget(self.last_name_label)
        form_layout_left.addWidget(self.last_name_input)
        form_layout_left.addWidget(self.first_name_label)
        form_layout_left.addWidget(self.first_name_input)
        form_layout_left.addWidget(self.middle_name_label)
        form_layout_left.addWidget(self.middle_name_input)

        form_layout_right = QVBoxLayout()
        self.job_label = QLabel("Должность")
        self.job_input = QLineEdit()
        self.job_input.setFixedHeight(25)

        self.birth_date_label = QLabel("Дата рождения")
        self.birth_date_input = QLineEdit()
        self.birth_date_input.setFixedHeight(25)

        self.address_label = QLabel("Адрес")
        self.address_input = QLineEdit()
        self.address_input.setFixedHeight(25)

        self.phone_label = QLabel("Номер телефона")
        self.phone_input = QLineEdit()
        self.phone_input.setFixedHeight(25)

        self.salary_label = QLabel("Зарплата")
        self.salary_input = QLineEdit()
        self.salary_input.setFixedHeight(25)

        self.email_label = QLabel("E-mail")
        self.email_input = QLineEdit()
        self.email_input.setFixedHeight(25)

        form_layout_right.addWidget(self.job_label)
        form_layout_right.addWidget(self.job_input)
        form_layout_right.addWidget(self.birth_date_label)
        form_layout_right.addWidget(self.birth_date_input)
        form_layout_right.addWidget(self.address_label)
        form_layout_right.addWidget(self.address_input)
        form_layout_right.addWidget(self.phone_label)
        form_layout_right.addWidget(self.phone_input)
        form_layout_right.addWidget(self.salary_label)
        form_layout_right.addWidget(self.salary_input)
        form_layout_right.addWidget(self.email_label)
        form_layout_right.addWidget(self.email_input)

        forms_layout = QHBoxLayout()
        forms_layout.addLayout(form_layout_left)
        forms_layout.addSpacing(60)
        forms_layout.addLayout(form_layout_right)
        main_layout.addLayout(forms_layout)

        self.setLayout(main_layout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = AddEmployeeWindow()
    window.show()
    sys.exit(app.exec())
