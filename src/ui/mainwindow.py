from PyQt5 import QtCore, QtWidgets

class UIMainWindow(QtWidgets.QMainWindow):
    # def init(self):
    #     super().init()
    #     self.setWindowTitle("Главное окно")
    #     self.setFixedSize(801, 478)
    #     self.setupUi()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # Верхняя область с кнопками
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 761, 39))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.add_client_btn = QtWidgets.QPushButton("Добавить клиента", self.horizontalLayoutWidget)
        self.add_client_btn.setFixedSize(130, 25)
        self.horizontalLayout.addWidget(self.add_client_btn)

        self.transactions_btn = QtWidgets.QPushButton("Управление транзакциями", self.horizontalLayoutWidget)
        self.transactions_btn.setFixedSize(170, 25)
        self.horizontalLayout.addWidget(self.transactions_btn)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.cabinet_btn = QtWidgets.QPushButton("Личный кабинет", self.horizontalLayoutWidget)
        self.cabinet_btn.setFixedSize(110, 25)
        self.horizontalLayout.addWidget(self.cabinet_btn)

        self.exit_btn = QtWidgets.QPushButton("Выйти", self.horizontalLayoutWidget)
        self.exit_btn.setFixedSize(60, 25)
        self.horizontalLayout.addWidget(self.exit_btn)

        # Таблица клиентов
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 130, 761, 310))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ФИО", "Дата рождения", "Телефон", "Е-mail"])
        self.tableWidget.setColumnWidth(0, 240)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 170)
        self.tableWidget.setColumnWidth(3, 199)

        # Панель поиска
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(425, 95, 357, 39))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox.addItem("Выберите")
        self.horizontalLayout_2.addWidget(self.comboBox)

        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setFixedSize(150, 20)
        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.search_btn = QtWidgets.QPushButton("Поиск", self.horizontalLayoutWidget_2)
        self.search_btn.setFixedSize(60, 25)
        self.horizontalLayout_2.addWidget(self.search_btn)

        # Статусная строка
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)


if __name__ == "main":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UIMainWindow()
    window.show()
    sys.exit(app.exec_())