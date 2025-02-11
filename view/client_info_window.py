from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QDialog, QWidget, QScrollBar, QListWidget, QListWidgetItem, QTabWidget, QApplication
from service.client_manager import ClientManager
from service.user_manager import UserManager


class ClientInfoWindow(QDialog):
    def __init__(self, id_client):
        super().__init__()
        self.user = UserManager().authorised_user
        self.client = ClientManager().get_client_info(id_client)
        self.ui_client_info_window()

    def ui_client_info_window(self):
        self.setWindowTitle("Информация о клиенте")
        self.setFixedSize(568, 319)

        # Создаем пользовательский вертикальный скролл-бар
        self.custom_scroll = QScrollBar(self)
        self.custom_scroll.setOrientation(QtCore.Qt.Orientation.Vertical)
        # Располагаем скролл-бар слева – ширина 16 пикселей
        self.custom_scroll.setGeometry(0, 0, 16, 318)

        # Создаем list_widget рядом с пользовательским скролл-баром
        self.list_widget = QListWidget(self)
        # Сдвигаем list_widget вправо на ширину скролл-бара
        self.list_widget.setGeometry(QtCore.QRect(16, 0, 285, 318))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_widget.setFont(font)
        # Отключаем встроенный скролл-бар, чтобы не мешал
        self.list_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Связываем пользовательский скролл-бар и скрытый скролл-бар list_widget
        internal_scroll = self.list_widget.verticalScrollBar()
        internal_scroll.rangeChanged.connect(self.custom_scroll.setRange)
        self.custom_scroll.valueChanged.connect(internal_scroll.setValue)
        internal_scroll.valueChanged.connect(self.custom_scroll.setValue)

        # Добавляем 24 элемента в список (12 пар: ключ – значение)
        for _ in range(24):
            item = QListWidgetItem()
            item_font = QtGui.QFont()
            item_font.setPointSize(10)
            item_font.setWeight(50)
            item.setFont(item_font)
            # Выравниваем текст по левому краю внутри list_widget
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
            self.list_widget.addItem(item)

        # Применяем стиль к элементам значений (нечетные индексы)
        value_indices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
        for idx in value_indices:
            item = self.list_widget.item(idx)
            item.setForeground(QtGui.QBrush(QtGui.QColor(30, 138, 86)))
            font_item = item.font()
            font_item.setBold(True)
            item.setFont(font_item)

        self.tab_widget = QTabWidget(self)
        self.tab_widget.setGeometry(QtCore.QRect(306, -1, 261, 320))

        self.tab = QWidget()
        self.tab_widget.addTab(self.tab, "Счета")

        self.tab_2 = QWidget()
        self.tab_widget.addTab(self.tab_2, "Карты")

        self.tab_3 = QWidget()
        self.tab_widget.addTab(self.tab_3, "Вклады")

        self.tab_4 = QWidget()
        self.tab_widget.addTab(self.tab_4, "Кредиты")

        # Устанавливаем тексты ключей вручную (чётные индексы)
        self.list_widget.item(0).setText("ФИО:")
        self.list_widget.item(1).setText(self.client.full_name)
        self.list_widget.item(2).setText("Менеджер:")
        self.list_widget.item(3).setText(self.client.employee.full_name)
        self.list_widget.item(4).setText("Дата рождения:")
        self.list_widget.item(5).setText(self.client.birth_date.strftime("%d.%m.%Y"))
        self.list_widget.item(6).setText("Номер телефона:")
        self.list_widget.item(7).setText(self.client.phone_number)
        self.list_widget.item(8).setText("Адрес регистрации:")
        self.list_widget.item(9).setText(self.client.registration_address)
        self.list_widget.item(10).setText("Адрес проживания:")
        self.list_widget.item(11).setText(self.client.residential_address)
        self.list_widget.item(12).setText("E-mail:")
        self.list_widget.item(13).setText(self.client.email)
        self.list_widget.item(14).setText("Серия и номер паспорта:")
        self.list_widget.item(15).setText(str(self.client.passport_number))
        self.list_widget.item(16).setText("Дата выдачи паспорта:")
        self.list_widget.item(17).setText(self.client.passport_issue_date.strftime("%d.%m.%Y"))
        self.list_widget.item(18).setText("ИНН:")
        self.list_widget.item(19).setText(str(self.client.inn))
        self.list_widget.item(20).setText("Реестровый номер:")
        self.list_widget.item(22).setText("Дата регистрации в системе:")
        self.list_widget.item(23).setText(self.client.registration_date.strftime("%d.%m.%Y"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = ClientInfoWindow()
    form.show()
    sys.exit(app.exec())