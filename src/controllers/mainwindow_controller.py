from PyQt5.QtWidgets import QMainWindow
from src.ui.mainwindow import UIMainWindow

class MainWindowController(UIMainWindow):  # Наследуемся от UIMainWindow
    def __init__(self, parent=None):
        super().__init__(parent)
        # Вызов setupUi() создаёт интерфейс в self
        self.setupUi()
        self.setWindowTitle("Банковская Система")
        self.setFixedSize(801, 478)
        self.apply_dark_theme()

    def apply_dark_theme(self):
        dark_theme = """
        QMainWindow {
            background-color: #1c1c1c;
        }
        QDialog {
            background-color: #1c1c1c;
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
            background-color: #2a2a2a;
            color: #ffffff;
        }
        QTabWidget::pane {
            border: none;
        }
        QTabBar {
            background-color: #3a3a3a;
            color: #ffffff;
        }
        QTabBar::tab {
            background-color: #3a3a3a;
            color: #ffffff;
            padding: 10px;
        }
        QTabBar::tab:selected {
            background-color: #4a4a4a;
        }
        QTabBar::tab:hover {
            background-color: #4a4a4a;
        }
        """
        self.setStyleSheet(dark_theme)
