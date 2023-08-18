import random
import string

from django.contrib.auth.models import User

from apps.commons.int import IntUtils


class RandomUtils:
    """Класс методов для работы с генератором случайных чисел"""

    @staticmethod
    def generate_invite_code() -> str:
        """Сгенерировать инвайт-код"""
        code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        return code.upper()

    @staticmethod
    def generate_auth_code() -> int:
        """Сгенерировать код авторизации"""
        code = ''
        for _ in range(4):
            while True:
                digit = random.choice(string.digits)
                if digit != '0':
                    break
            code += digit
        return IntUtils.value_to_int(code)

    @staticmethod
    def generate_username() -> str:
        """Сгенерировать уникальное имя пользователя Django"""
        username = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        while True:
            if not User.objects.filter(username=username).exists():
                break
            username = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        return username

    @staticmethod
    def generate_password() -> str:
        """Сгенерировать пароль пользователя Django"""
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
