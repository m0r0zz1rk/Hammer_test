from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.commons.models.base_table import BaseTable
from apps.commons.random import RandomUtils


class AuthRequests(BaseTable):
    """Модель запросов на авторизацию (пользователь - код в СМС сообщении для входа)"""
    django_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Авторизующийся пользователь Django'
    )
    auth_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(9999), MinValueValidator(1000)],
        default=RandomUtils.generate_auth_code(),
        blank=False,
        null=False,
        verbose_name='Код авторизации'
    )

    def __str__(self):
        return f'Код авторизации для пользователя {self.django_user.username}'

    class Meta:
        verbose_name = 'Запрос на авторизацию'
        verbose_name_plural = 'Запросы на авторизацию'
