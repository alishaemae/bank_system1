from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QSpacerItem, QSizePolicy, QPushButton
from service.user_manager import UserManager
from view.user_info_w_controller import *


class UserInfoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.user = UserManager().authorised_user
        self.ui_user_info_window()

    def ui_user_info_window(self):
        self.setWindowTitle("Личный кабинет")
        self.setFixedSize(801, 478)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(90, 10, 90, 30)

        self.name_label = QLabel(self.user.full_name, self)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_label.setFixedHeight(45)
        main_layout.addWidget(self.name_label)

        details_layout = QGridLayout()
        details_layout.setHorizontalSpacing(15)
        details_layout.setColumnStretch(1, 1)
        details_layout.setColumnStretch(4, 2)
        details_layout.setColumnMinimumWidth(1, 150)
        details_layout.setColumnMinimumWidth(4, 150)

        font = QtGui.QFont()
        font.setPointSize(10)
        value_style = "font-size: 14px; color: rgb(30, 138, 86); font-weight: bold; border: 1px; padding: 2px;"

        dob_label = QLabel("Дата рождения:")
        dob_label.setFont(font)
        details_layout.addWidget(dob_label, 0, 0)

        self.dob_value = QLabel(self.user.birth_date.strftime("%d.%m.%Y"))
        self.dob_value.setStyleSheet(value_style)
        details_layout.addWidget(self.dob_value, 0, 1)

        phone_label = QLabel("Номер телефона:")
        phone_label.setFont(font)
        details_layout.addWidget(phone_label, 1, 0)

        self.phone_value = QLabel(self.user.phone_number)
        self.phone_value.setStyleSheet(value_style)
        details_layout.addWidget(self.phone_value, 1, 1)

        email_label = QLabel("E-mail:")
        email_label.setFont(font)
        details_layout.addWidget(email_label, 2, 0)

        self.email_value = QLabel(self.user.email)
        self.email_value.setStyleSheet(value_style)
        self.email_value.setWordWrap(True)
        details_layout.addWidget(self.email_value, 2, 1)

        salary_label = QLabel("Зарплата:")
        salary_label.setFont(font)
        details_layout.addWidget(salary_label, 3, 0)

        self.salary_value = QLabel(str(self.user.salary))
        self.salary_value.setStyleSheet(value_style)
        details_layout.addWidget(self.salary_value, 3, 1)

        spacer = QSpacerItem(
            20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )
        details_layout.addItem(spacer, 0, 2, 4, 4)

        login_label = QLabel("Логин:")
        login_label.setFont(font)
        details_layout.addWidget(login_label, 0, 3)

        self.login_value = QLabel(self.user.login)
        self.login_value.setStyleSheet(value_style)
        details_layout.addWidget(self.login_value, 0, 4)

        job_label = QLabel("Должность:")
        job_label.setFont(font)
        details_layout.addWidget(job_label, 1, 3)

        self.job_value = QLabel(self.user.job)
        self.job_value.setStyleSheet(value_style)
        details_layout.addWidget(self.job_value, 1, 4)

        address_label = QLabel("Адрес:")
        address_label.setFont(font)
        details_layout.addWidget(address_label, 2, 3)

        self.address_value = QLabel(self.user.address)
        self.address_value.setStyleSheet(value_style)
        self.address_value.setWordWrap(True)
        details_layout.addWidget(self.address_value, 2, 4)

        main_layout.addLayout(details_layout)

        self.back_button = QPushButton("Назад", self)
        self.back_button.setFixedSize(60, 25)
        self.back_button.setStyleSheet(
            "background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        self.back_button.move(720, 433)
        self.back_button.clicked.connect(
            lambda: open_clients_list_window(self))
