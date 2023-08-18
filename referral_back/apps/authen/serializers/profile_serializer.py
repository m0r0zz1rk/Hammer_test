from rest_framework import serializers

from apps.referral.serializers.referral_list_serializer import ReferralListSerializer


class ProfileSerializer(serializers.Serializer):
    """Сериализатор для данных пользователя из профиля"""
    phone = serializers.CharField(
        max_length=18,
        allow_null=False,
        allow_blank=False
    )
    invite_code = serializers.CharField(
        max_length=6,
        allow_null=False,
        allow_blank=False
    )
    activated_invite_code = serializers.CharField(
        max_length=6,
        allow_blank=True,
        allow_null=True
    )
    referrals = ReferralListSerializer()
