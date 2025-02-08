from PyQt5 import QtCore, QtGui, QtWidgets


class UserInfoWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def setupUi(self):
        self.setWindowTitle("Информация о сотруднике")
        self.setFixedSize(801, 478)
        
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        
        # Основной вертикальный layout
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(90, 10, 90, 30)
        
        # Заголовок с именем пользователя
        self.name_label = QtWidgets.QLabel(self.user.full_name, self)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setFixedHeight(45)
        # Обрамляем заголовок рамкой (оставляем стиль без изменений, если нужно убрать рамку – измените стиль)
        self.name_label.setStyleSheet("border: 1px whight;")
        main_layout.addWidget(self.name_label)
        
        # Layout для отображения информации с разделителем между блоками
        details_layout = QtWidgets.QGridLayout()
        details_layout.setHorizontalSpacing(15)
        # Левый блок занимает колонки 0 и 1, затем spacer в колонке 2, правый блок занимает колонки 3 и 4
        details_layout.setColumnStretch(1, 1)
        details_layout.setColumnStretch(4, 2)
        
        # Задаем стиль для подписей и значений с рамками (если нужно изменить, измените стиль)
        label_style = "font-size: 14px; border: 1px whight; padding: 2px;"
        value_style = "font-size: 14px; color: rgb(30, 138, 86); font-weight: bold; border: 1px whight; padding: 2px;"
        
        # Строка: Дата рождения (левый блок)
        dob_label = QtWidgets.QLabel("Дата рождения:")
        dob_label.setStyleSheet(label_style)
        details_layout.addWidget(dob_label, 0, 0)
        
        self.dob_value = QtWidgets.QLabel(self.user.birth_date.strftime("%d.%m.%Y"))
        self.dob_value.setStyleSheet(value_style)
        details_layout.addWidget(self.dob_value, 0, 1)

        # Строка: Номер телефона (левый блок)
        phone_label = QtWidgets.QLabel("Номер телефона:")
        phone_label.setStyleSheet(label_style)
        details_layout.addWidget(phone_label, 1, 0)
        
        self.phone_value = QtWidgets.QLabel(self.user.phone_number)
        self.phone_value.setStyleSheet(value_style)
        details_layout.addWidget(self.phone_value, 1, 1)

        # Строка: E-mail (левый блок)
        email_label = QtWidgets.QLabel("E-mail:")
        email_label.setStyleSheet(label_style)
        details_layout.addWidget(email_label, 2, 0)

        self.email_value = QtWidgets.QLabel(self.user.email)
        self.email_value.setStyleSheet(value_style)
        self.email_value.setWordWrap(True)
        details_layout.addWidget(self.email_value, 2, 1)
        
        # Строка: Зарплата (левый блок)
        salary_label = QtWidgets.QLabel("Зарплата:")
        salary_label.setStyleSheet(label_style)
        details_layout.addWidget(salary_label, 3, 0)
        
        self.salary_value = QtWidgets.QLabel(str(self.user.salary))
        self.salary_value.setStyleSheet(value_style)
        details_layout.addWidget(self.salary_value, 3, 1)
        
        # Добавляем spacer между колонками 1 и 3 в виде пустого пространства (колонка 2)
        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        details_layout.addItem(spacer, 0, 2, 4, 4)
        
        # Правый блок
        
        # Строка: Логин (правый блок)
        login_label = QtWidgets.QLabel("Логин:")
        login_label.setStyleSheet(label_style)
        details_layout.addWidget(login_label, 0, 3)
        
        self.login_value = QtWidgets.QLabel(self.user.login)
        self.login_value.setStyleSheet(value_style)
        details_layout.addWidget(self.login_value, 0, 4)
        
        # Строка: Должность (правый блок)
        job_label = QtWidgets.QLabel("Должность:")
        job_label.setStyleSheet(label_style)
        details_layout.addWidget(job_label, 1, 3)
        
        self.job_value = QtWidgets.QLabel(self.user.job)
        self.job_value.setStyleSheet(value_style)
        details_layout.addWidget(self.job_value, 1, 4)

        # Строка: Адрес (правый блок)
        address_label = QtWidgets.QLabel("Адрес:")
        address_label.setStyleSheet(label_style)
        details_layout.addWidget(address_label, 2, 3)
        
        self.address_value = QtWidgets.QLabel(self.user.address)
        self.address_value.setStyleSheet(value_style)
        self.address_value.setWordWrap(True)
        details_layout.addWidget(self.address_value, 2, 4)
        
        main_layout.addLayout(details_layout)
        
        # Добавляем кнопку напрямую к центральному виджету:
        self.back_button = QtWidgets.QPushButton("Назад", self.centralwidget)
        self.back_button.setFixedSize(60, 25)
        self.back_button.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        # Позиционируем кнопку в правом нижнем углу (отступ 20 пикселей)
        self.back_button.move(720, 433)
        self.back_button.raise_()
        
        # Добавляем кнопку напрямую к центральному виджету:
        self.delete_button = QtWidgets.QPushButton("Скрыть сотрудника", self.centralwidget)
        self.delete_button.setFixedSize(150, 25)
        self.delete_button.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 14px; color: white; border: 0; border-radius: 4px;")
        # Позиционируем кнопку в правом нижнем углу (отступ 20 пикселей)
        self.delete_button.move(629, 20)
        self.delete_button.raise_()


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
            self.email = "nasushchnov487@gmail.com"

    dummy_user = DummyUser()

    window = UserInfoWindow()
    window.user = dummy_user
    window.setupUi()
    window.show()

    sys.exit(app.exec_())