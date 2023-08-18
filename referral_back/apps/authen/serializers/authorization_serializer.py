from rest_framework import serializers

from apps.authen.serializers.phone_serializer import PhoneSerializer


class AuthorizationSerializer(PhoneSerializer):
    """Сериализатор данных для авторизации"""
    auth_code = serializers.CharField(
        max_length=4,
        min_length=4,
        allow_null=False,
        allow_blank=False
    )


class AuthorizationResponseSerializer(serializers.Serializer):
    """Сериализатор ответа системы в случае успешной авторизации"""
    token = serializers.CharField(
        max_length=2048,
        allow_blank=False,
        allow_null=False
    )
    user_id = serializers.IntegerField()
