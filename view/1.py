from PyQt5 import QtCore, QtWidgets

class UIemployes_info(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Управление сотрудниками")
        self.setFixedSize(801, 478)
        self.setupUi()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.add_client_btn = QtWidgets.QPushButton("Добавить сотрудника")
        self.add_client_btn.setFixedSize(150, 25)
        self.add_client_btn.move(20, 20)
        self.add_client_btn.raise_()

        self.exit_btn = QtWidgets.QPushButton("Назад")
        self.exit_btn.setFixedSize(60, 25)


        # Таблица клиентов
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 130, 761, 310))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ФИО", "Должность", "Роль", "Телефон"])
        self.tableWidget.setColumnWidth(0, 240)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 170)
        self.tableWidget.setColumnWidth(3, 199)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UIemployes_info()
    window.show()
    sys.exit(app.exec_())