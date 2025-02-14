def open_auth_window(self):
    from view.auth_window import AuthWindow
    self.auth_window = AuthWindow()
    self.auth_window.show()
    self.close()


def open_user_info_window(self):
    from view.user_info_window import UserInfoWindow
    self.user_info_window = UserInfoWindow()
    self.user_info_window.show()
    self.close()


def open_client_info_window(self, id_client):
    from view.client_info_window import ClientInfoWindow
    self.client_info_window = ClientInfoWindow(id_client)
    self.client_info_window.exec()


def open_employees_list_window(self):
    from view.employees_list_window import EmployeesListWindow
    self.employees_list_window = EmployeesListWindow()
    self.employees_list_window.show()
    self.close()

def open_create_report_window(self, clients):
    from view.create_report_window import CreateReportWindow
    self.create_report_window = CreateReportWindow(clients)
    self.create_report_window.exec()


def search_clients(self):
    search_text = self.lineEdit.text().strip().lower().replace("ё", "е")
    if search_text == "":
        filtered = self.all_clients
    else:
        filtered = [
            client for client in self.all_clients
            if search_text in client.full_name.lower().replace("ё", "е")
        ]
    self.clients = filtered
    self.populate_clients_table(filtered)
