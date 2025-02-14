def open_clients_list_window(self):
    from view.clients_list_window import ClientsListWindow
    self.clients_info_window = ClientsListWindow()
    self.clients_info_window.show()
    self.close()
