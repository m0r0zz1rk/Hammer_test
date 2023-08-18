from rest_framework import serializers


class ReferralListSerializer(serializers.Serializer):
    """Сериализатор списка рефералов пользователя"""
    phones = serializers.ListField(
        child=serializers.CharField(
            max_length=18,
            allow_null=False,
            allow_blank=False,
        )
    )
