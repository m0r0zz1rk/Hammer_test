from django.contrib import admin
from django.contrib.auth.models import User

from apps.authen.models.auth_requests import AuthRequests
from apps.authen.models.profiles import Profiles


@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
    pass


@admin.register(AuthRequests)
class AuthRequestsAdmin(admin.ModelAdmin):
    list_display = ['django_username', 'auth_code']

    def django_username(self, obj) -> str:
        """Получение имени пользователя Django"""
        return User.objects.get(id=obj.django_user.id).username

    django_username.short_description = 'Пользователь'
