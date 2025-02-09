from PyQt5 import QtCore, QtGui, QtWidgets
import os

class AuthWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # self.user = UserService().authorised_user
        self.ui_auth_window()

    def ui_auth_window(self):      
        self.setWindowTitle("Авторизация")
        self.setFixedSize(404, 300)

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 60, 281, 91)) 
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Поле для логина
        self.usernameLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.usernameLineEdit.setFixedHeight(28)
        self.usernameLineEdit.setPlaceholderText("Введите логин")
        self.verticalLayout.addWidget(self.usernameLineEdit)

        # Поле для пароля
        self.passwordLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setFixedHeight(28)
        self.passwordLineEdit.setPlaceholderText("Введите пароль")
        self.verticalLayout.addWidget(self.passwordLineEdit)

        # Метка капчи
        self.captchaLabel = QtWidgets.QLabel(self)
        self.captchaLabel.setGeometry(QtCore.QRect(60, 160, 180, 40))  
        font = QtGui.QFont()
        font.setPointSize(10)
        self.captchaLabel.setFont(font)
        self.captchaLabel.setObjectName("captchaLabel")
        
        # Кнопка обновления капчи
        self.refreshCaptchaButton = QtWidgets.QPushButton(self)
        self.refreshCaptchaButton.setGeometry(QtCore.QRect(250, 160, 40, 40))  
        self.refreshCaptchaButton.setStyleSheet("border: none;")
        refresh_icon = QtGui.QIcon(os.path.join(os.path.dirname(__file__), '..', 'assets', 'refresh.svg'))
        self.refreshCaptchaButton.setIcon(refresh_icon)
        self.refreshCaptchaButton.setIconSize(QtCore.QSize(32, 32))
        self.refreshCaptchaButton.setObjectName("refreshCaptchaButton")

        # Поле для капчи
        self.captchaLineEdit = QtWidgets.QLineEdit(self)
        self.captchaLineEdit.setGeometry(QtCore.QRect(60, 210, 281, 28))  
        font = QtGui.QFont()
        font.setPointSize(9)
        self.captchaLineEdit.setFont(font)
        self.captchaLineEdit.setObjectName("captchaLineEdit")
        self.captchaLineEdit.setPlaceholderText("Введите капчу")

        # Метка ошибки
        self.ErrorLabel = QtWidgets.QLabel(self)
        self.ErrorLabel.setGeometry(QtCore.QRect(30, 20, 351, 31)) 
        self.ErrorLabel.setAlignment(QtCore.Qt.AlignCenter) 
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setStyleSheet("color: red;")
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.ErrorLabel.setText("Ошибка!")

        self.enter_widget = QtWidgets.QWidget(self)
        self.enter_widget.setGeometry(QtCore.QRect(172, 255, 60, 25))
        self.enter_widget.setObjectName("enter_widget")
        self.enter_layout = QtWidgets.QVBoxLayout(self.enter_widget)
        self.enter_button = QtWidgets.QPushButton("Войти", self.enter_widget)
        self.enter_button.setFixedSize(60, 25)
        self.enter_button.setStyleSheet("background-color: rgb(30, 138, 86); font-size: 15px; color: white; border: 0; border-radius: 4px;")
        self.enter_button.raise_()