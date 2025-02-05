from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

class LKEmployeesController(QDialog):
    def __init__(self, ui, role):
        super().__init__()
        self.ui = ui
        self.role = role
        self.ui.setupUi(self)
        self.configure_page_by_role()
        self.connect_signals()

    def configure_page_by_role(self):
        print(f"Получена роль: {self.role}")  

        if self.role == "admin":
            self.ui.stackedWidget.setCurrentIndex(2)  # страница администратора
            print("Открыта страница администратора")
        elif self.role == "cashier":
            self.ui.stackedWidget.setCurrentIndex(0)  # страница кассира
            print("Открыта страница кассира")
        elif self.role == "manager":
            self.ui.stackedWidget.setCurrentIndex(1)  # страница менеджера
            print("Открыта страница менеджера")
        else:
            raise ValueError(f"Неизвестная роль: {self.role}")

    def connect_signals(self):
        self.ui.pushButton.clicked.connect(self.logout)
        self.ui.pushButton_2.clicked.connect(self.logout)
        self.ui.pushButton_3.clicked.connect(self.logout)

    def logout(self):
        print("Выход из личного кабинета")
        self.close()

