from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QWidget, QScrollBar, QListWidget, QListWidgetItem, QTabWidget, QApplication


class ClientInfoWindow(QWidget):
    def __init__(self):
        super().__init__()
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

        # Добавляем 21 элемент в список
        for _ in range(22):
            item = QListWidgetItem()
            item_font = QtGui.QFont()
            item_font.setPointSize(10)
            item_font.setWeight(50)
            item.setFont(item_font)
            # Выравниваем текст по левому краю внутри list_widget
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
            self.list_widget.addItem(item)

        # Применяем стиль к данным клиента для индексов: 1,3,5,7,9,11,13,15,17,19
        indices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
        for idx in indices:
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

        # Устанавливаем тексты элементов вручную (выравнены по левому краю внутри list_widget)
        self.list_widget.item(0).setText("ФИО:")
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
    app = QApplication(sys.argv)
    form = ClientInfoWindow()
    form.show()
    sys.exit(app.exec())