from PyQt5 import QtCore, QtGui, QtWidgets


class UserInfoWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def setupUi(self):
        self.setWindowTitle("Личный кабинет")
        self.setFixedSize(801, 478)
        
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        
        # Основной вертикальный layout
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(100, 20, 100, 20)
        
        # Заголовок с именем пользователя
        self.name_label = QtWidgets.QLabel(self.user.full_name, self)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setFixedHeight(45)
        main_layout.addWidget(self.name_label)
        
        # Layout для отображения информации
        details_layout = QtWidgets.QGridLayout()
        details_layout.setHorizontalSpacing(15)
        details_layout.setColumnStretch(1, 1)
        
        # Задаем стиль для подписей и значений
        label_style = "font-size: 14px; color: #000000"
        value_style = "font-size: 14px; color: #558dbb; font-weight: bold;"
        
        # Строка 0: Дата рождения и Логин
        dob_label = QtWidgets.QLabel("Дата рождения:")
        dob_label.setStyleSheet(label_style)
        details_layout.addWidget(dob_label, 0, 0)
        
        self.dob_value = QtWidgets.QLabel(self.user.birth_date.strftime("%d.%m.%Y"))
        self.dob_value.setStyleSheet(value_style)
        details_layout.addWidget(self.dob_value, 0, 1)
        
        login_label = QtWidgets.QLabel("Логин:")
        login_label.setStyleSheet(label_style)
        details_layout.addWidget(login_label, 0, 2)
        
        self.login_value = QtWidgets.QLabel(self.user.login)
        self.login_value.setStyleSheet(value_style)
        details_layout.addWidget(self.login_value, 0, 3)
        
        # Строка 1: Номер телефона и Адрес
        phone_label = QtWidgets.QLabel("Номер телефона:")
        phone_label.setStyleSheet(label_style)
        details_layout.addWidget(phone_label, 1, 0)
        
        self.phone_value = QtWidgets.QLabel(self.user.phone_number)
        self.phone_value.setStyleSheet(value_style)
        details_layout.addWidget(self.phone_value, 1, 1)
        
        address_label = QtWidgets.QLabel("Адрес:")
        address_label.setStyleSheet(label_style)
        details_layout.addWidget(address_label, 1, 2)
        
        self.address_value = QtWidgets.QLabel(self.user.address)
        self.address_value.setStyleSheet(value_style)
        self.address_value.setWordWrap(True)
        details_layout.addWidget(self.address_value, 1, 3)
        
        # Строка 2: Должность и Зарплата
        job_label = QtWidgets.QLabel("Должность:")
        job_label.setStyleSheet(label_style)
        details_layout.addWidget(job_label, 2, 0)
        
        self.job_value = QtWidgets.QLabel(self.user.job)
        self.job_value.setStyleSheet(value_style)
        details_layout.addWidget(self.job_value, 2, 1)
        
        salary_label = QtWidgets.QLabel("Зарплата:")
        salary_label.setStyleSheet(label_style)
        details_layout.addWidget(salary_label, 2, 2)
        
        self.salary_value = QtWidgets.QLabel(str(self.user.salary))
        self.salary_value.setStyleSheet(value_style)
        details_layout.addWidget(self.salary_value, 2, 3)
        
        main_layout.addLayout(details_layout)
        
        # # Кнопка "Назад" в нижней части окна
        # button_layout = QtWidgets.QHBoxLayout()
        # self.back_button = QtWidgets.QPushButton("Назад", self)
        # self.back_button.setFixedSize(50, 25)
        # self.back_button.setStyleSheet("background-color: #7b99ca; font-size: 14px; color: white; border: 0; border-radius: 5px;")
        # button_layout.addWidget(self.back_button)
        # main_layout.addLayout(button_layout)

        
        # Вместо этого добавляем кнопку напрямую к центральному виджету:
        self.back_button = QtWidgets.QPushButton("Назад", self.centralwidget)
        self.back_button.setFixedSize(50, 25)
        self.back_button.setStyleSheet("background-color: #7b99ca; font-size: 14px; color: white; border: 0; border-radius: 5px;")
        # Позиционируем кнопку в правом нижнем углу (отступ 20 пикселей от края)
        self.back_button.move(720, 430)
        self.back_button.raise_()  # убедимся, что кнопка отображается поверх основного layout


if __name__ == "__main__":
    import sys
    import datetime
    from PyQt5 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)

    class DummyUser:
        def __init__(self):
            self.full_name = "Иван Иванов Иванович"
            self.birth_date = datetime.datetime(1990, 12, 31)
            self.login = "ivanov"
            self.phone_number = "+7 (111) 222-3333"
            self.address = "г. Москва, ул. Ленина, д. 1"
            self.job = "Бухгалтер"
            self.salary = 50000

dummy_user = DummyUser()

window = UserInfoWindow()
window.user = dummy_user
window.setupUi()
window.show()

sys.exit(app.exec_())