from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtGui
import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from service.user_manager import *
from view.clients_list_window import ClientsListWindow


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
    self.captchaLabel.setPixmap(QtGui.QPixmap.fromImage(q_image))
    self.captchaLineEdit.clear()

def random_color(self):
    # возвращает случайни цвет
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def open_clients_list_window(self):
    self.clients_list_window = ClientsListWindow()
    self.clients_list_window.show()
    self.hide()

def validate_credentials(self):
    user_manager = UserManager()
    login = self.usernameLineEdit.text().strip()
    password = self.passwordLineEdit.text().strip()
    captcha = self.captchaLineEdit.text().strip()
    result = user_manager.get_user(login, password)

    # if login == "" or password == "" or captcha == "":
    #     self.ErrorLabel.setText("Заполните все поля")
    # elif result == "":
    #     if captcha == self.current_captcha_text:
    #         open_clients_list_window(self)
    #     else:
    #         self.ErrorLabel.setText("Неверная капча")
    #         generate_captcha(self)
    # else:
    #     self.ErrorLabel.setText(result)
    #     generate_captcha(self)

    if login == "" or password == "":
        self.ErrorLabel.setText("Заполните все поля")
    elif result == "":
            open_clients_list_window(self)
    else:
        self.ErrorLabel.setText(result)
        generate_captcha(self)