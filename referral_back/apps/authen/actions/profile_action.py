from django.contrib.auth.models import User

from apps.authen.models.profiles import Profiles


class ProfileAction:
    """Работа с профилем пользоателя"""

    @staticmethod
    def get_user_profile_data(user: User) -> dict:
        """Получение данных из профиля полученного пользователя"""
        data = {}
        if Profiles.objects.filter(django_user_id=user.id).exists():
            profile = Profiles.objects.filter(django_user_id=user.id).first()
            data['phone'] = profile.phone
            data['invite_code'] = profile.invite_code
            data['activated_invite_code'] = profile.activated_invite_code
            data['referrals'] = {
                'phones': profile.get_referrals()
            }
        return data
