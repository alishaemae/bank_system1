from PyQt5.QtWidgets import QDialog
from view.mainwindow_controller import MainWindowController
from view.lkemployees_controller import LKEmployeesController
from view.user_info_window import Ui_Form 
from PyQt5.QtCore import Qt

main_window_instance = None  # глоб переменная для экземпляра главного окна
lk_window_instance = None  # глоб переменная для экземпляра личного кабинета

def show_main_window():
    global main_window_instance
    if main_window_instance is not None:
        main_window_instance.close()
    main_window_instance = MainWindowController()
    main_window_instance.show()


def open_personal_cabinet():
    global lk_window_instance
    print(f"Открытие личного кабинета с ролью: {role}")

    if role == "Администратор":
        role = "admin"
    elif role == "Кассир":
        role = "cashier"
    elif role == "Менеджер":
        role = "manager"
    else:
        raise ValueError(f"Неизвестная роль: {role}")

    if lk_window_instance is not None:
        lk_window_instance.close() 

    lk_window_instance = QDialog()
    ui = Ui_Form()
    ui.setupUi(lk_window_instance)

    # передаем реальный объект окна в контроллер и роль
    lk_controller = LKEmployeesController(ui, role)

    # устанавливаем связь между окном и контроллером
    lk_window_instance.setAttribute(Qt.WA_DeleteOnClose, False)

    # показываем окно
    lk_window_instance.show()






