from PyQt6.QtWidgets import (
    QApplication, QPushButton, QVBoxLayout, QHBoxLayout,
    QWidget, QLabel, QLineEdit, QComboBox, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt


class AddEmployeeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_add_employee_window()

    def ui_add_employee_window(self):
        self.setWindowTitle("Добавление сотрудника")
        self.setFixedSize(701, 378)

        # Основной layout с отступами по краям
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(5)

        # Верхняя панель с кнопкой "Добавить сотрудника"
        top_layout = QHBoxLayout()
        self.add_employee_button = QPushButton("Добавить сотрудника")
        self.add_employee_button.setFixedSize(180, 25)
        self.add_employee_button.setStyleSheet(
            "background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 5px;"
        )
        # Здесь оставляем только кнопку добавления, кнопку "Назад" убираем из верхней панели
        top_layout.addWidget(self.add_employee_button)
        top_layout.addStretch()

        self.error_label = QLabel("")
        self.error_label.setFixedHeight(22)
        self.error_label.setStyleSheet("color: red; font-size: 14px;")
        top_layout.addWidget(self.error_label)
        self.error_label.setText("Заполните все поля")

        # Инициализируем кнопку "Назад" (не трогаем расположение кнопок)
        self.back_button = QPushButton("Назад")
        self.back_button.setFixedSize(60, 25)
        self.back_button.setStyleSheet(
            "background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 5px;"
        )

        # Левый столбец (форма 1)
        form_layout = QVBoxLayout()
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
        self.role_input.addItems(["Администратор", "Сотрудник"])

        self.last_name_label = QLabel("Фамилия")
        self.last_name_input = QLineEdit()
        self.last_name_input.setFixedHeight(25)

        self.first_name_label = QLabel("Имя")
        self.first_name_input = QLineEdit()
        self.first_name_input.setFixedHeight(25)

        self.middle_name_label = QLabel("Отчество")
        self.middle_name_input = QLineEdit()
        self.middle_name_input.setFixedHeight(25)

        form_layout.addWidget(self.login_label)
        form_layout.addWidget(self.login_input)
        form_layout.addWidget(self.password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.role_label)
        form_layout.addWidget(self.role_input)
        form_layout.addWidget(self.last_name_label)
        form_layout.addWidget(self.last_name_input)
        form_layout.addWidget(self.first_name_label)
        form_layout.addWidget(self.first_name_input)
        form_layout.addWidget(self.middle_name_label)
        form_layout.addWidget(self.middle_name_input)

        # Правый столбец (форма 2)
        form_1_layout = QVBoxLayout()
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

        form_1_layout.addWidget(self.job_label)
        form_1_layout.addWidget(self.job_input)
        form_1_layout.addWidget(self.birth_date_label)
        form_1_layout.addWidget(self.birth_date_input)
        form_1_layout.addWidget(self.address_label)
        form_1_layout.addWidget(self.address_input)
        form_1_layout.addWidget(self.phone_label)
        form_1_layout.addWidget(self.phone_input)
        form_1_layout.addWidget(self.salary_label)
        form_1_layout.addWidget(self.salary_input)
        form_1_layout.addWidget(self.email_label)
        form_1_layout.addWidget(self.email_input)

        # Расположение форм в два столбца
        parallel_layout = QHBoxLayout()
        parallel_layout.addLayout(form_layout, 1)
        parallel_layout.addLayout(form_1_layout, 1)

        # Добавляем верхнюю панель и формы
        main_layout.addLayout(top_layout)
        # Отступ между кнопками и формами – так, чтобы названия полей ушли ниже
        main_layout.addSpacing(10)
        main_layout.addLayout(parallel_layout)

        # Вместо растяжителя добавляем фиксированный отступ, чтобы кнопку "Назад" разместить ниже
        main_layout.addSpacing(9)

        # Нижняя панель с кнопкой "Назад" в правом нижнем углу
        exit_layout = QHBoxLayout()
        exit_layout.addWidget(self.back_button)
        exit_layout.setAlignment(self.back_button, Qt.AlignmentFlag.AlignRight)
        main_layout.addLayout(exit_layout)

        self.setLayout(main_layout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = AddEmployeeWindow()
    window.show()
    sys.exit(app.exec())