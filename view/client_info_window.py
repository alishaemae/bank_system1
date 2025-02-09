from PyQt5 import QtCore, QtGui, QtWidgets


class ClientInfoWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui_client_info_window()

    def ui_client_info_window(self):
        self.setWindowTitle("Карточка клиента")
        self.setFixedSize(568, 319)

        self.list_widget = QtWidgets.QListWidget(self)
        self.list_widget.setGeometry(QtCore.QRect(0, 0, 301, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_widget.setFont(font)
        self.list_widget.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        # Добавляем 21 элемент в список
        for _ in range(21):
            item = QtWidgets.QListWidgetItem()
            item_font = QtGui.QFont()
            item_font.setPointSize(12)
            item_font.setBold(False)
            item_font.setWeight(50)
            item.setFont(item_font)
            self.list_widget.addItem(item)

        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setGeometry(QtCore.QRect(306, -1, 261, 321))

        self.tab = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab, "Счета")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab_2, "Карты")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab_3, "Вклады")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab_4, "Кредиты")

        # Устанавливаем тексты элементов вручную
        self.list_widget.item(0).setText("ФИО: ")
        self.list_widget.item(1).setText("Вася Пупкин Васильевич")
        self.list_widget.item(2).setText("Дата рождения:")
        self.list_widget.item(4).setText("Номер телефона:")
        self.list_widget.item(6).setText("Адрес регистрации:")
        self.list_widget.item(8).setText("Адрес проживания:")
        self.list_widget.item(10).setText("E-mail:")
        self.list_widget.item(12).setText("Серия и номер паспорта:")
        self.list_widget.item(14).setText("Дата выдачи паспорта:")
        self.list_widget.item(16).setText("ИНН:")
        self.list_widget.item(18).setText("Реестровый номер:")
        self.list_widget.item(20).setText("Дата регистрации в системе:")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form = ClientInfoWindow()
    form.show()
    sys.exit(app.exec_())
