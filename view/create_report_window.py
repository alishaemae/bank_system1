from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QDialog, QWidget, QScrollBar, QListWidget, QListWidgetItem, QTabWidget, QApplication
from service.client_manager import ClientManager
from service.user_manager import UserManager
from view.create_report_w_controller import *


class CreateReportWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_create_report_window()

    def ui_create_report_window(self):
        self.setWindowTitle("Создать отчет")
        self.setFixedSize(568, 319)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = CreateReportWindow()
    form.show()
    sys.exit(app.exec())
