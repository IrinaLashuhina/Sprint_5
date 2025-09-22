import random
import string


class EmailPasswordGenerator:
    @staticmethod
    def generate_email():
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"{username}@yandex.ru"

    @staticmethod
    def generate_password():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))