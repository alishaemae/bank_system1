from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(404, 300) 

        # Лейаут для логина и пароля
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 60, 281, 91)) 
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Поле для логина
        self.usernameLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(9)
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.verticalLayout.addWidget(self.usernameLineEdit)

        # Поле для пароля
        self.passwordLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(9)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.verticalLayout.addWidget(self.passwordLineEdit)

        # Метка капчи
        self.captchaLabel = QtWidgets.QLabel(Dialog)
        self.captchaLabel.setGeometry(QtCore.QRect(60, 160, 180, 40))  
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.captchaLabel.setFont(font)
        self.captchaLabel.setObjectName("captchaLabel")

        # Кнопка обновления капчи
        self.refreshCaptchaButton = QtWidgets.QPushButton(Dialog)
        self.refreshCaptchaButton.setGeometry(QtCore.QRect(250, 160, 40, 40))  
        self.refreshCaptchaButton.setStyleSheet("border: none;")
        refresh_icon = QtGui.QIcon("src/assets/refresh.svg")
        self.refreshCaptchaButton.setIcon(refresh_icon)
        self.refreshCaptchaButton.setIconSize(QtCore.QSize(32, 32))
        self.refreshCaptchaButton.setObjectName("refreshCaptchaButton")

        # Поле для капчи
        self.captchaLineEdit = QtWidgets.QLineEdit(Dialog)
        self.captchaLineEdit.setGeometry(QtCore.QRect(60, 210, 281, 28))  
        self.captchaLineEdit.setObjectName("captchaLineEdit")

        # Метка ошибки
        self.ErrorLabel = QtWidgets.QLabel(Dialog)
        self.ErrorLabel.setGeometry(QtCore.QRect(30, 20, 351, 31)) 
        self.ErrorLabel.setAlignment(QtCore.Qt.AlignCenter) 
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(9)
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setStyleSheet("color: red;")
        self.ErrorLabel.setObjectName("ErrorLabel")

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(190, 260, 191, 31))  
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText("ОК")  
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText("Отмена")  
        self.buttonBox.setObjectName("buttonBox")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Авторизация"))
        self.usernameLineEdit.setPlaceholderText(_translate("Dialog", "Введите логин"))
        self.passwordLineEdit.setPlaceholderText(_translate("Dialog", "Введите пароль"))
        self.captchaLineEdit.setPlaceholderText(_translate("Dialog", "Введите капчу"))
        self.refreshCaptchaButton.setText("")
        self.ErrorLabel.setText(_translate("Dialog", "Ошибка!"))
