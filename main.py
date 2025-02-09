import sys
import os
from PyQt5.QtWidgets import QApplication
from service.window_manager import show_main_window
from view.auth_w_controller import AuthController

def main(): 
    app = QApplication(sys.argv)
    auth_window = AuthController()  
    auth_window.show() 
    auth_window.successful_login.connect(show_main_window)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()