from typing import Optional

from django.contrib.auth.models import User

from apps.authen.models.auth_requests import AuthRequests
from apps.commons.random import RandomUtils


class AuthRequestsUtils:
    """Класс методов для работы с запросами на авторизаццию"""

    @staticmethod
    def create_auth_request(user: User) -> str:
        """
            Создание запроса на авторизацию
        :param user: пользователь Django
        :return: код авторизации
        """
        new_request = AuthRequests.objects.create(
            django_user=user,
            auth_code=RandomUtils.generate_auth_code()
        )
        return new_request.auth_code

    @staticmethod
    def get_code_by_last_auth_request(user: User) -> Optional[int]:
        """Получение кода авторизации крайнего запроса пользователя"""
        if AuthRequests.objects.filter(django_user=user).exists():
            return AuthRequests.objects.filter(django_user=user).order_by('-created_at').first().auth_code
        return None

    @staticmethod
    def delete_user_auth_requests(user: User):
        """Удаление всех запросов авторизации пользователя"""
        for request in AuthRequests.objects.filter(django_user=user):
            request.delete()
