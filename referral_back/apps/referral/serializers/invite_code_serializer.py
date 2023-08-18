from rest_framework import serializers


class InviteCodeSerializer(serializers.Serializer):
    """Сериализатор инвайт кодов"""
    invite_code = serializers.CharField(
        min_length=6,
        max_length=6,
        allow_null=False,
        allow_blank=False
    )
