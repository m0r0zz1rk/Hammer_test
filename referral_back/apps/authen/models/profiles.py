from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.commons.models.base_table import BaseTable
from apps.commons.random import RandomUtils
from apps.commons.string import StringUtils


class Profiles(BaseTable):
    """Модель профилей пользователей"""
    django_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Пользователь Django'

    )
    phone = models.CharField(
        max_length=18,
        unique=True,
        blank=False,
        null=False,
        default='+7 (999) 999-99-99',
        verbose_name='Номер телефона'
    )
    invite_code = models.CharField(
        max_length=6,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Собственный инвайт-код'
    )
    activated_invite_code = models.CharField(
        max_length=6,
        blank=True,
        null=True,
        default=None,
        verbose_name='Активированный инвайт-код'
    )

    def __str__(self):
        display_name = StringUtils.convert_obj_to_str(self.object_id)
        if not StringUtils.is_str_null_or_empty(self.phone):
            display_name = StringUtils.convert_obj_to_str(self.phone)
        return display_name

    def is_invite_code_activated(self) -> bool:
        """Активировал ли пользователь инвайт-код"""
        return not StringUtils.is_str_null_or_empty(self.activated_invite_code)

    def get_referrals(self) -> list:
        """Получение списка номеров телефона с использованным инвайт-кодом владельца профиля"""
        referrals = []
        if Profiles.objects.filter(activated_invite_code=self.invite_code).exists():
            referrals = [ref.phone for ref in Profiles.objects.filter(activated_invite_code=self.invite_code)]
        return referrals

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


def get_unique_invite_code() -> str:
    """Получить уникальный инвайт-код"""
    code = RandomUtils.generate_invite_code()
    while True:
        if not Profiles.objects.filter(invite_code=code).exists():
            break
        code = RandomUtils.generate_invite_code()
    return code


@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    """Создание профиля в случае добавления нового пользователя в систему"""
    if created:
        Profiles.objects.create(django_user_id=instance.id,
                                invite_code=get_unique_invite_code())
