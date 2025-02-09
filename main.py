import sys
from PyQt5.QtWidgets import QApplication
from view.auth_windown import AuthWindow

def main(): 
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()