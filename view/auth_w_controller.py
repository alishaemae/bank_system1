from PyQt6 import QtWidgets, QtGui
from service.db_connector import get_db
from data.employees import Employee
import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os


def generate_captcha(self):
    # Коэффициент масштабирования
    scale = 1
    base_width, base_height = 150, 50
    width, height = base_width * scale, base_height * scale
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.load_default(size=25)
    self.current_captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    
    for i, char in enumerate(self.current_captcha_text):
        x = (10 + i * 20 + random.randint(-3, 3)) * scale
        y = (random.randint(5, 15)) * scale
        draw.text((x, y), char, font=font, fill=random_color(self))
    
    for _ in range(100):
        x, y = random.randint(0, width), random.randint(0, height)
        draw.point((x, y), random_color(self))
    
    image = image.filter(ImageFilter.GaussianBlur(1))
    image = image.resize((base_width, base_height), resample=Image.Resampling.LANCZOS)
    
    from io import BytesIO
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    
    q_image = QtGui.QImage()
    q_image.loadFromData(buffer.read(), "PNG")
    # Вместо self.ui.captchaLabel используем self.captchaLabel
    self.captchaLabel.setPixmap(QtGui.QPixmap.fromImage(q_image))

def random_color(self):
    # возвращает случайни цвет
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def validate_credentials(self):
    username = self.usernameLineEdit.text().strip()
    password = self.passwordLineEdit.text().strip()
    captcha_input = self.captchaLineEdit.text().strip()

    # if not username or not password or not captcha_input:
    #     self.show_error("Все поля обязательны для заполнения")
    #     return

    # if captcha_input != self.current_captcha_text:
    #     self.show_error("Неверная капча")
    #     self.ui.captchaLineEdit.clear()
    #     self.generate_captcha()
    #     return
    try:
        db = next(get_db())
        employee = db.query(Employee).filter(Employee.username == username).first()
    except Exception as e:
        show_error("Ошибка подключения к базе данных", exception=e)
        return
    
    if employee and password == employee.password_hash:  # пароль пока сравнивается в открытом виде
        self.ui.ErrorLabel.hide()
        self.successful_login.emit(str(employee.role_id))
        self.accept()
    else:
        self.show_error("Неверный логин или пароль")

def show_error(self, message, exception=None):
    self.ui.ErrorLabel.setText(message)
    self.ui.ErrorLabel.show()