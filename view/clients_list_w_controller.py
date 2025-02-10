def open_auth_window(self):
    from auth_window import AuthWindow
    self.auth_window = AuthWindow()
    self.auth_window.show()
    self.close()  

def open_user_info_window(self):
    from view.user_info_window import UserInfoWindow
    self.user_info_window = UserInfoWindow()
    self.user_info_window.show()
    self.close()

def open_client_info_window(self):
    from view.client_info_window import ClientInfoWindow
    self.client_info_window = ClientInfoWindow()
    self.client_info_window.show()

def open_employees_list_window(self):
    from view.employees_list_window import EmployeesListWindow
    self.employees_list_window = EmployeesListWindow()
    self.employees_list_window.show()
    self.close()