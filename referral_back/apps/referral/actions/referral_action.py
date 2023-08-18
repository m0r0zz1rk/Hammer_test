from django.contrib.auth.models import User
from django.db import transaction

from apps.authen.models.profiles import Profiles
from apps.commons.error import ErrorHandling


class ReferralAction:
    """Класс для работы с реферальными операциями"""

    @staticmethod
    def is_invite_code_exists(invite_code: str) -> bool:
        """Проверка на существующий инвайт-код"""
        return Profiles.objects.filter(invite_code=invite_code).exists()

    def activate_invite_code(self, user: User, invite_code: str) -> (bool, str):
        """
            Активация инвайт-кода в профиле пользователя
        :param user: пользователь Django
        :param invite_code: инвайт-код
        :return: сообщение об успехе или ошибке
        """
        success = False
        result = ''
        if self.is_invite_code_exists(invite_code):
            try:
                with transaction.atomic():
                    profile = Profiles.objects.get(django_user_id=user.id)
                    if profile.is_invite_code_activated():
                        result = 'Ранее уже был активирован инвайт-код'
                    else:
                        if profile.invite_code == invite_code:
                            result = 'Нельзя установить свой инвайт-код'
                        else:
                            profile.activated_invite_code = invite_code
                            profile.save()
                            result = 'Инвайт-код успешно активирован'
                            success = True
            except Exception:
                result = ErrorHandling.get_traceback()
        else:
            result = 'Инвайт-код не найден'
        return success, result
