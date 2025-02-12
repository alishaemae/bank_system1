from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QSpacerItem, QSizePolicy, QPushButton
from view.employee_info_w_controller import *
from data.user import UserRole


class EmployeeInfoWindow(QWidget):
    def __init__(self, employee):   
        super().__init__()
        self.employee = employee   
        self.ui_employee_info_window()

    def ui_employee_info_window(self):
        self.setWindowTitle("Информация о сотруднике")
        self.setFixedSize(801, 478)

        # Вместо создания центрального виджета устанавливаем layout на self
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(90, 10, 90, 30)

        # Заголовок с именем пользователя
        self.name_label = QLabel(self.employee.full_name, self)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_label.setFixedHeight(45)
        main_layout.addWidget(self.name_label)

        # Layout для отображения информации с разделителем между блоками
        details_layout = QGridLayout()
        details_layout.setHorizontalSpacing(15)
        details_layout.setColumnStretch(1, 1)
        details_layout.setColumnStretch(4, 2)
        # Увеличиваем минимальную ширину столбцов, чтобы правый столбец не сдвигался влево
        details_layout.setColumnMinimumWidth(1, 150)
        details_layout.setColumnMinimumWidth(4, 150)

        value_style = "font-size: 14px; color: rgb(30, 138, 86); font-weight: bold; border: 1px; padding: 2px;"
 
        font = QtGui.QFont()
        font.setPointSize(10)

        dob_label = QLabel("Дата рождения:")
        dob_label.setFont(font)
        details_layout.addWidget(dob_label, 0, 0)

        self.dob_value = QLabel(self.employee.birth_date.strftime("%d.%m.%Y"))
        self.dob_value.setStyleSheet(value_style)
        details_layout.addWidget(self.dob_value, 0, 1)

        phone_label = QLabel("Номер телефона:")
        phone_label.setFont(font)
        details_layout.addWidget(phone_label, 1, 0)

        self.phone_value = QLabel(self.employee.phone_number)
        self.phone_value.setStyleSheet(value_style)
        details_layout.addWidget(self.phone_value, 1, 1)

        email_label = QLabel("E-mail:")
        email_label.setFont(font)
        details_layout.addWidget(email_label, 2, 0)

        self.email_value = QLabel(self.employee.email)
        self.email_value.setStyleSheet(value_style)
        self.email_value.setWordWrap(True)
        details_layout.addWidget(self.email_value, 2, 1)

        salary_label = QLabel("Зарплата:")
        salary_label.setFont(font)
        details_layout.addWidget(salary_label, 3, 0)

        self.salary_value = QLabel(str(self.employee.salary))
        self.salary_value.setStyleSheet(value_style)
        details_layout.addWidget(self.salary_value, 3, 1)

        spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        details_layout.addItem(spacer, 0, 2, 4, 4)

        login_label = QLabel("Логин:")
        login_label.setFont(font)
        details_layout.addWidget(login_label, 0, 3)

        self.login_value = QLabel(self.employee.login)
        self.login_value.setStyleSheet(value_style)
        details_layout.addWidget(self.login_value, 0, 4)

        job_label = QLabel("Должность:")
        job_label.setFont(font)
        details_layout.addWidget(job_label, 1, 3)

        self.job_value = QLabel(self.employee.job)
        self.job_value.setStyleSheet(value_style)
        details_layout.addWidget(self.job_value, 1, 4)

        address_label = QLabel("Адрес:")
        address_label.setFont(font)
        details_layout.addWidget(address_label, 2, 3)

        self.address_value = QLabel(self.employee.address)
        self.address_value.setStyleSheet(value_style)
        self.address_value.setWordWrap(True)
        details_layout.addWidget(self.address_value, 2, 4)

        main_layout.addLayout(details_layout)

        self.back_button = QPushButton("Назад", self)
        self.back_button.setFixedSize(60, 25)
        self.back_button.setStyleSheet(
            "background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;"
        )
        self.back_button.move(720, 433)
        self.back_button.clicked.connect(lambda: open_emloyees_list_window(self))

        if self.employee.role == UserRole.MANAGER:
            self.delete_button = QPushButton("Удалить сотрудника", self)
            self.delete_button.setFixedSize(160, 25)
            self.delete_button.setStyleSheet(
                "background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;"
            )
            self.delete_button.setGeometry(QtCore.QRect(620, 10, 160, 25))
            self.delete_button.clicked.connect(lambda: delete_employee(self))


# if __name__ == "__main__":
#     import sys
#     import datetime
#     from PyQt6.QtWidgets import QApplication

#     app = QApplication(sys.argv)

#     class DummyUser:
#         def __init__(self):
#             self.full_name = "Иван Иванов Иванович"
#             self.birth_date = datetime.datetime(1990, 12, 31)
#             self.login = "ivanov"
#             self.phone_number = "+7 (111) 222-3333"
#             self.address = "г. Москва, ул. Ленина, д. 1"
#             self.job = "Бухгалтер"
#             self.salary = 50000
#             self.email = "nasushchnov487@gmail.com"

#     dummy_user = DummyUser()
#     window = EmployeeInfoWindow(dummy_user)
#     window.show()

#     sys.exit(app.exec())