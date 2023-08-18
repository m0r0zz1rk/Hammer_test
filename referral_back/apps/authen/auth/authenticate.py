import jwt

from datetime import datetime
from typing import Optional
from django.contrib.auth.models import User
from rest_framework import authentication

from apps.commons.django import DjangoUtils


class AuthenticateCredential:
    """Класс получения данных при аутентификации по JWT токену"""

    _token = None

    def __init__(self, token):
        """
            Инициализация класса - установка полученного значения токена, создание сущности записи сообщений
            в журнал системных событий
        """
        self.du = DjangoUtils()
        self._token = token

    def validate_and_check_token(self) -> bool:
        """Валидация и проверка полученного токена"""
        try:
            payload = jwt.decode(
                self._token,
                self.du.get_parameter_from_settings('SECRET_KEY'),
                algorithms=self.du.get_parameter_from_settings('JWT_ALGORITHM')
            )
        except jwt.PyJWTError:
            return False

        token_expire = datetime.fromtimestamp(payload['exp'])
        if token_expire < datetime.utcnow():
            return False
        return True

    def authenticate_credential(self):
        """Получение пользователя Django на основе токена"""
        if self.validate_and_check_token():
            payload = jwt.decode(self._token,
                                 self.du.get_parameter_from_settings('SECRET_KEY'),
                                 algorithms=self.du.get_parameter_from_settings('JWT_ALGORITHM'))
            if User.objects.filter(id=payload['user_id']).exists():
                user = User.objects.get(id=payload['user_id'])
                return user, None
        return None


class AuthBackend(authentication.BaseAuthentication):
    """Аутентификация на основе JWT токена"""

    @staticmethod
    def _validate_header(header: list) -> bool:
        """Валидация полученного заголовка запроса"""

        if not header or header[0].lower() != b'token':
            return False

        if len(header) == 1:
            return False
        elif len(header) > 2:
            return False
        else:
            return True

    def authenticate(self, request, token=None, **kwargs) -> Optional[User]:
        """Валидация заголовка запроса и аутентификация"""
        auth_header = authentication.get_authorization_header(request).split()

        if not self._validate_header(auth_header):
            return None

        try:
            token = auth_header[1].decode('utf-8')
            return AuthenticateCredential(token).authenticate_credential()
        except UnicodeError:
            return None
