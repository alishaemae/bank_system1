import sys
from PyQt6.QtWidgets import QApplication
from view.auth_window import AuthWindow


def main():
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
