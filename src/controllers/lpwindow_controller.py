from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
from src.ui.lpwindown import Ui_Dialog
from sqlalchemy.orm import Session
from services.db_connector import get_db
from models.employees import Employee
import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from PyQt5.QtGui import QFont, QFontDatabase
import os


class AuthController(QtWidgets.QDialog):
    successful_login = pyqtSignal(str)

    def __init__(self, parent=None):
        super(AuthController, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setFixedSize(self.size())  # фиксированный размер окна

        self.apply_custom_font()
        self.apply_dark_theme() 

        self.ui.ErrorLabel.hide()
        self.generate_captcha()

        self.ui.refreshCaptchaButton.clicked.connect(self.generate_captcha)
        self.ui.buttonBox.accepted.connect(self.validate_credentials)
        self.ui.buttonBox.rejected.connect(self.reject)

    def apply_custom_font(self):
        font_path = "src/assets/DMSans-Italic-VariableFont_opsz,wght.ttf"
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            app_font = QFont(font_family)
            app_font.setPointSize(9)
            QtWidgets.QApplication.setFont(app_font)
        else:
            print("Ошибка: Шрифт не найден или не загружен")

    def apply_dark_theme(self):
        dark_theme = """
        QDialog {
            background-color: #1c1c1c; 
            color: #ffffff;
        }
        QLabel {
            color: #ffffff;
        }
        QLineEdit {
            background-color: #2a2a2a;
            color: #ffffff;
            border: 1px solid #3d3d3d;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton {
            background-color: #3a3a3a;
            color: #ffffff;
            border: 1px solid #4a4a4a;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #4a4a4a;
        }
        QPushButton:pressed {
            background-color: #5a5a5a;
        }
        QDialogButtonBox QPushButton {
            background-color: #3a3a3a;
            color: #ffffff;
        }
        """
        self.setStyleSheet(dark_theme)

    def generate_captcha(self):
        width, height = 150, 50
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 36)

        self.current_captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        # текст с искажениями
        for i, char in enumerate(self.current_captcha_text):
            x = 10 + i * 20 + random.randint(-3, 3)
            y = random.randint(5, 15)
            draw.text((x, y), char, font=font, fill=self.random_color())

        # шум
        for _ in range(100):
            x, y = random.randint(0, width), random.randint(0, height)
            draw.point((x, y), fill=self.random_color())

        # фильтр размытия
        image = image.filter(ImageFilter.GaussianBlur(1))

        # капча во временном буфере сохраняеца
        from io import BytesIO
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)

        # загрузка изображения капчи в виджет
        q_image = QtGui.QImage()
        q_image.loadFromData(buffer.read(), "PNG")
        self.ui.captchaLabel.setPixmap(QtGui.QPixmap.fromImage(q_image))

    def random_color(self):
        # возвращает случайни цвет
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def validate_credentials(self):
        username = self.ui.usernameLineEdit.text().strip()
        password = self.ui.passwordLineEdit.text().strip()
        captcha_input = self.ui.captchaLineEdit.text().strip()

        if not username or not password or not captcha_input:
            self.show_error("Все поля обязательны для заполнения")
            return

        if captcha_input != self.current_captcha_text:
            self.show_error("Неверная капча")
            self.ui.captchaLineEdit.clear()
            self.generate_captcha()
            return

        db = next(get_db())
        employee = db.query(Employee).filter(Employee.username == username).first()

        if employee and password == employee.password_hash:  # пароль пока сравнивается в открытом виде
            self.ui.ErrorLabel.hide()
            QtWidgets.QMessageBox.information(self, "Успешно", f"Добро пожаловать, {employee.role_id}!")
            self.successful_login.emit(str(employee.role_id))
            self.accept()
        else:
            self.show_error("Неверный логин или пароль")

    def show_error(self, message):
        self.ui.ErrorLabel.setText(message)
        self.ui.ErrorLabel.show()
