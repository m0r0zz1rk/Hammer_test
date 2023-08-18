from django.contrib.auth.models import User

from apps.authen.models.profiles import Profiles


class ProfilesUtils:
    """Класс для работы с профилями пользователей"""

    @staticmethod
    def set_phone_to_profile(phone: str, profile: Profiles):
        """Установка номера телефона в профиль пользователя"""
        profile.phone = phone
        profile.save()

    @staticmethod
    def get_profile_by_user(user: User) -> Profiles:
        """Получение профиля пользователя"""
        return Profiles.objects.get(django_user_id=user.id)

    @staticmethod
    def get_user_by_phone(phone: str) -> User:
        """Получение пользователя по номеру телефона"""
        return User.objects.get(id=Profiles.objects.get(phone=phone).django_user_id)

    def get_username_by_phone(self, phone: str) -> str:
        username = 'Unknown'
        try:
            user = self.get_user_by_phone(phone)
            username = user.username
        except Exception:
            pass
        return username

    @staticmethod
    def is_first_time_logon(user_id: int) -> bool:
        """Проверка первого входа в систему"""
        return Profiles.objects.get(django_user_id=user_id).first_login

    @staticmethod
    def set_false_to_first_time_logon(user_id: int):
        """Установка значения False на поле first_login в профиле"""
        profile = Profiles.objects.get(django_user_id=user_id)
        profile.first_login = False
        profile.save()
