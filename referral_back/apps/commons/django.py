from typing import Optional, Union

from django.conf import settings
from django.contrib.auth.models import User

from apps.authen.models.profiles import Profiles
from apps.commons.random import RandomUtils


class DjangoUtils:
    """Класс методов для работы с элементами Django"""

    @staticmethod
    def is_settings_parameter_exists(param: str) -> bool:
        """Проверка на существующий в settings параметр"""
        if hasattr(settings, param):
            return True
        return False

    def get_parameter_from_settings(self, param: str) -> Optional[Union[str, int, float, list]]:
        """Получение значения параметра из settings"""
        if self.is_settings_parameter_exists(param):
            return getattr(settings, param, None)
        return None

    @staticmethod
    def create_django_user() -> (User, Profiles):
        """
            Создание пользователя Django
        :return: Получение пользователя и его профиля
        """
        user = User.objects.create_user(
            username=RandomUtils.generate_username(),
            password=RandomUtils.generate_password()
        )
        profile = Profiles.objects.get(django_user_id=user.id)
        return user, profile
