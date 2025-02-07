from PyQt5.QtWidgets import QMainWindow
from src.ui.mainwindow import UIMainWindow

class MainWindowController(UIMainWindow):  # Наследуемся от UIMainWindow
    def __init__(self, parent=None):
        super().__init__(parent)
        # Вызов setupUi() создаёт интерфейс в self
        self.setupUi()
        self.setWindowTitle("Банковская Система")
        self.setFixedSize(801, 478)