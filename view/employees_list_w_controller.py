def open_clients_list_window(self):
    from view.clients_list_window import ClientsListWindow 
    self.clients_list_window = ClientsListWindow()
    self.clients_list_window.show()
    self.close()

def open_employee_info_window(self, employee):
    from view.employee_info_window import EmployeeInfoWindow
    self.employee_info_window = EmployeeInfoWindow(employee)
    self.employee_info_window.show()
    self.close()

def open_add_employee_window(self):
    from view.add_employee_window import AddEmployeeWindow
    self.add_employee_window = AddEmployeeWindow()
    self.add_employee_window.show()
    self.close()