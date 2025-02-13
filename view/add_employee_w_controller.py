from service.user_manager import UserManager
import re
from PyQt6.QtWidgets import QMessageBox

def open_employees_list_window(self):
    from view.employees_list_window import EmployeesListWindow
    self.employees_list_window = EmployeesListWindow()
    self.employees_list_window.show()
    self.close()

def check_fields(self):
    if (self.login_input.text() and self.password_input.text() and self.role_input.currentText() and
    self.last_name_input.text() and self.first_name_input.text() and self.middle_name_input.text() and
    self.job_input.text() and self.birth_date_input.text() and self.address_input.text() and
    self.phone_input.text() and self.salary_input.text()) and self.email_input.text():
        return True
    else:
        return False


def add_staff(self):
    login = self.login_input.text()
    password = self.password_input.text()
    role = self.role_input.currentText()
    last_name = self.last_name_input.text()
    first_name = self.first_name_input.text()
    middle_name = self.middle_name_input.text()
    job = self.job_input.text()
    birth_date = self.birth_date_input.text()
    address = self.address_input.text()
    phone_number = self.phone_input.text()
    salary = self.salary_input.text()
    email = self.email_input.text()
    
    if check_fields(self):
        if phone_number.replace("+","").replace("-", "").replace(" ", "").isdigit():
            if re.fullmatch(r"^\+7 \d{3} \d{3}-\d{2}-\d{2}$", phone_number):
                if re.fullmatch(r"^\d{4}-\d{2}-\d{2}$", birth_date):
                    if salary.isdigit():
                        if check_login(self):
                            if UserManager().add_employee(login, password, role, last_name, first_name, middle_name, job, birth_date, address, phone_number, email, salary) == "":
                                open_employees_list_window(self)
                            else:
                                self.error_label.setText("Что-то пошло не так!")
                        else:
                            self.error_label.setText("Логин занят!")
                    else:
                        self.error_label.setText("Зарплата должна содержать только цифры!")
                        self.salary_input.clear()
                else:
                    self.error_label.setText("Формат даты рождения: YYYY-MM-DD")
            else:
                self.error_label.setText("Формат номера телефона: +7 XXX XXX-XX-XX")
        else:
            self.error_label.setText("Номер телефона должен содержать только цифры!")
    else:
        self.error_label.setText("Заполните все поля!")

def check_login(self):
    login = self.login_input.text()
    employee = UserManager().check_exist_login(login)
    if employee is None:
        return True
    else:
        return False

