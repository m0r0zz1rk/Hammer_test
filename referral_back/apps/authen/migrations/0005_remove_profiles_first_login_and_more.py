# Generated by Django 4.2.4 on 2023-08-18 03:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0004_authrequests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='first_login',
        ),
        migrations.AlterField(
            model_name='authrequests',
            name='auth_code',
            field=models.PositiveIntegerField(default=8681, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1000)], verbose_name='Код авторизации'),
        ),
    ]