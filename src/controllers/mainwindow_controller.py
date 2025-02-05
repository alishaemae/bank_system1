from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import uic
from src.controllers.lkemployees_controller import LKEmployeesController 
from src.controllers.lpwindow_controller import AuthController
from src.ui.mainwindow import Ui_MainWindow  

class MainWindowController(QMainWindow):
    personal_cabinet_requested = pyqtSignal(str)

    def __init__(self, role, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)  

        self.setWindowTitle("Банковская Система")

        self.apply_dark_theme()

        self.role = role
        print(f"Главное окно открыто с ролью: {self.role}")  


        self.ui.pushButton.setText("Клиенты")  
        self.ui.pushButton.clicked.connect(self.show_clients_page)  # клиенты
        self.ui.pushButton_2.clicked.connect(self.show_accounts_page)  # счет
        self.ui.pushButton_6.clicked.connect(self.show_transactions_page)  # транзакции
        self.ui.pushButton_4.clicked.connect(self.show_loans_page)  # кредиты
        self.ui.pushButton_5.clicked.connect(self.show_cards_page)  # карты
        self.ui.pushButton_3.clicked.connect(self.show_employees_page)  # сотрудники
        self.ui.pushButton_7.clicked.connect(self.show_activity_log_page)  # журнал активности

        # лк
        self.ui.pushButton_26.clicked.connect(self.request_personal_cabinet)

        self.ui.stackedwitged.setCurrentIndex(0)

    def apply_dark_theme(self):
        dark_theme = """
        QMainWindow {
            background-color: #1c1c1c; /* Темный фон для основного окна */
        }
        QDialog {
            background-color: #1c1c1c; /* Темный фон для диалогов */
            color: #ffffff;
        }
        QLabel {
            color: #ffffff;
        }
        QLineEdit {
            background-color: #2a2a2a;
            color: #ffffff;
            border: 1px solid #3d3d3d;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton {
            background-color: #3a3a3a;
            color: #ffffff;
            border: 1px solid #4a4a4a;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #4a4a4a;
        }
        QPushButton:pressed {
            background-color: #5a5a5a;
        }
        QDialogButtonBox QPushButton {
            background-color: #3a3a3a;
            color: #ffffff;
        }
        QTabWidget {
            background-color: #2a2a2a; /* Темный фон для QTabWidget */
            color: #ffffff; /* Белый цвет текста */
        }
        QTabWidget::pane {
            border: none; /* Убираем границу у панели */
        }
        QTabBar {
            background-color: #3a3a3a; /* Темный фон для вкладок */
            color: #ffffff; /* Белый текст на вкладках */
        }
        QTabBar::tab {
            background-color: #3a3a3a; /* Фон вкладок */
            color: #ffffff; /* Текст на вкладке */
            padding: 10px;
        }
        QTabBar::tab:selected {
            background-color: #4a4a4a; /* Выделенная вкладка */
        }
        QTabBar::tab:hover {
            background-color: #4a4a4a; /* Вкладка при наведении */
        }
        """
        self.setStyleSheet(dark_theme)

    def show_clients_page(self):
        self.ui.stackedwitged.setCurrentIndex(1)  

    def show_accounts_page(self):
        self.ui.stackedwitged.setCurrentIndex(2)  # страница для счетов

    def show_transactions_page(self):
        self.ui.stackedwitged.setCurrentIndex(3)  # страница для транзакций

    def show_loans_page(self):
        self.ui.stackedwitged.setCurrentIndex(4)  # страница для кредитов

    def show_cards_page(self):
        self.ui.stackedwitged.setCurrentIndex(5)  # страница для карт

    def show_employees_page(self):
        self.ui.stackedwitged.setCurrentIndex(6)  # страница для сотрудников

    def show_activity_log_page(self):
        self.ui.stackedwitged.setCurrentIndex(7)  # страница для журнала активности

    def request_personal_cabinet(self):
        if not self.role:
            QMessageBox.warning(self, "Ошибка", "Роль пользователя не установлена")
            return
        print(f"Запрос на открытие личного кабинета с ролью: {self.role}")
        self.personal_cabinet_requested.emit(self.role)