from rest_framework import serializers


class PhoneSerializer(serializers.Serializer):
    """Сериализатор для номеров телефона"""
    phone = serializers.CharField(
        max_length=18,
        min_length=18,
        allow_null=False,
        allow_blank=False
    )
