from service.user_manager import UserManager
from PyQt6.QtWidgets import QMessageBox

def open_emloyees_list_window(self):
    from view.employees_list_window import EmployeesListWindow
    self.employees_list_window = EmployeesListWindow()
    self.employees_list_window.show()
    self.close()

def delete_employee(self):
    msg = QMessageBox(self)
    msg.setWindowTitle("Подтверждение")
    msg.setText(f"Удалить сотрудника {self.employee.full_name}?")
    msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    yes_button = msg.button(QMessageBox.StandardButton.Yes)
    no_button = msg.button(QMessageBox.StandardButton.No)
    yes_button.setText("Да")
    no_button.setText("Нет")
    result = msg.exec()

    if result == QMessageBox.StandardButton.Yes:
        user_service = UserManager()
        result = user_service.update_deleted_status_employee(self.employee.id)
        if result == "":
            open_emloyees_list_window(self)
        else:
            QMessageBox.critical(self, "Ошибка", result)
    else:
        pass