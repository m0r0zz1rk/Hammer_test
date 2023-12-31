# Generated by Django 4.2.4 on 2023-08-17 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('object_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID объекта')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания объекта')),
                ('first_login', models.BooleanField(default=True, verbose_name='Первый вход в систему')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=50, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=18, unique=True, verbose_name='Номер телефона')),
                ('invite_code', models.CharField(max_length=6, unique=True, verbose_name='Собственный инвайт-код')),
                ('activated_invite_code', models.CharField(default=None, max_length=6, null=True, verbose_name='Активированный инвайт-код')),
                ('django_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь Django')),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователей',
            },
        ),
    ]
