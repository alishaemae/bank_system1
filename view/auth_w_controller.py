from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtGui
import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from service.user_manager import *
from view.clients_list_window import ClientsListWindow


def generate_captcha(self):
    scale = 1
    base_width, base_height = 150, 50
    width, height = base_width * scale, base_height * scale
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default(size=25)
    self.current_captcha_text = ''.join(random.choices(
        string.ascii_letters + string.digits, k=6))

    for i, char in enumerate(self.current_captcha_text):
        x = (10 + i * 20 + random.randint(-3, 3)) * scale
        y = (random.randint(5, 15)) * scale
        draw.text((x, y), char, font=font, fill=random_color(self))

    for _ in range(100):
        x, y = random.randint(0, width), random.randint(0, height)
        draw.point((x, y), random_color(self))

    image = image.filter(ImageFilter.GaussianBlur(1))
    image = image.resize((base_width, base_height),
                         resample=Image.Resampling.LANCZOS)

    from io import BytesIO
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    q_image = QtGui.QImage()
    q_image.loadFromData(buffer.read(), "PNG")
    self.captchaLabel.setPixmap(QtGui.QPixmap.fromImage(q_image))
    self.captchaLineEdit.clear()


def random_color(self):
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def open_clients_list_window(self):
    self.clients_list_window = ClientsListWindow()
    self.clients_list_window.show()
    self.hide()


def validate_credentials(self):
    # Создаем экземпляр класса, который отвечает за проверку логина и пароля.
    user_manager = UserManager()

    # Получаем текст, введённый пользователем в поле логина, удаляя лишние пробелы по краям.
    login = self.usernameLineEdit.text().strip()
    # Получаем текст, введённый пользователем в поле пароля, удаляя лишние пробелы по краям.
    password = self.passwordLineEdit.text().strip()
    # Получаем текст, введённый пользователем в поле капчи, удаляя лишние пробелы по краям.
    captcha = self.captchaLineEdit.text().strip()

    # Вызываем метод get_user для проверки корректности логина и пароля.
    # Если пользователь найден, метод возвращает пустую строку, в противном случае – сообщение об ошибке.
    result = user_manager.get_user(login, password)

    # Если хотя бы одно из обязательных полей (логин, пароль, капча) не заполнено,
    # устанавливаем сообщение об ошибке для пользователя.
    if login == "" or password == "" or captcha == "":
        self.ErrorLabel.setText("Заполните все поля")
    # Если логин и пароль корректны
    elif result == "":
        # Проверяем, правильно ли введена капча, сравнивая введённое значение с сгенерированным.
        if captcha == self.current_captcha_text:
            # Если капча введена верно, переходим в окно со списком клиентов.
            open_clients_list_window(self)
        else:
            # Если капча введена неверно, выводим сообщение об ошибке.
            self.ErrorLabel.setText("Неверная капча")
            # Генерируем новую капчу для возможности повторной авторизации.
            generate_captcha(self)
    else:
        # Если метод get_user вернул сообщение об ошибке (например, неверный логин или пароль),
        # отображаем это сообщение в виджете ErrorLabel.
        self.ErrorLabel.setText(result)
        # Генерируем новую капчу для попытки повторной авторизации.
        generate_captcha(self)
