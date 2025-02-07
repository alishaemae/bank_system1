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
