import sys
import os
from PyQt5.QtWidgets import QApplication
from services.window_manager import show_main_window
from src.controllers.lpwindow_controller import AuthController

def main(): 
    app = QApplication(sys.argv)
    lp_window = AuthController()  
    lp_window.show() 
    lp_window.successful_login.connect(show_main_window)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()