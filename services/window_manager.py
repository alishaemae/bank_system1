from PyQt5.QtWidgets import QDialog
from src.controllers.mainwindow_controller import MainWindowController
from src.controllers.lkemployees_controller import LKEmployeesController
from src.ui.lkemployees import Ui_Form 
from PyQt5.QtCore import Qt

main_window_instance = None  # глоб переменная для экземпляра главного окна
lk_window_instance = None  # глоб переменная для экземпляра личного кабинета

def show_main_window(role):
    global main_window_instance
    print(f"Открытие главного окна с ролью: {role}") 

    main_window_instance = MainWindowController(role)
    main_window_instance.show()
    main_window_instance.personal_cabinet_requested.connect(lambda: open_personal_cabinet(role))


def open_personal_cabinet(role):
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






