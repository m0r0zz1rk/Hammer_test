from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions

from apps.commons.dict import DictUtils
from apps.commons.profiles import ProfilesUtils
from apps.commons.response import ResponsesClass
from apps.commons.rest import RestUtils
from apps.referral.actions.referral_action import ReferralAction
from apps.referral.serializers.invite_code_serializer import InviteCodeSerializer
from apps.referral.serializers.referral_list_serializer import ReferralListSerializer


class ReferralViewSet(viewsets.ViewSet):
    """Операции по активации инвайт-кода и получения списка рефералов"""
    permission_classes = [permissions.IsAuthenticated, ]

    ra = ReferralAction()
    ru = RestUtils()
    du = DictUtils()

    @swagger_auto_schema(
        operation_description="Активация полученного инвайт-кода в профиле пользователя",
        request_body=InviteCodeSerializer,
        responses={'400': 'Внутренняя ошибка сервера (error в теле ответа)',
                   '403': 'Пользователь не авторизован',
                   '200': 'Код успешно активирован (success в теле ответа)'}
    )
    def activate_invite_code(self, request, *args, **kwargs):
        """Активация полученного из request инвайт-кода в профиле пользователя"""
        params = ['invite_code']
        if not self.ru.validate_params_to_list(request, params):
            return ResponsesClass.bad_request_response(
                'Произошла ошибка - были получены некорректные данные'
            )
        invite_code = self.ru.get_request_parameter_by_key(request, 'invite_code')
        success, result = self.ra.activate_invite_code(request.user, invite_code)
        if success:
            return ResponsesClass.ok_response(result)
        else:
            return ResponsesClass.bad_request_response(result)

    @staticmethod
    @swagger_auto_schema(
        operation_description="Получение списка рефералов пользователя",
        responses={'400': 'Внутренняя ошибка сервера при сериализации данных',
                   '403': 'Пользователь не авторизован',
                   '200': ReferralListSerializer}
    )
    def get_referrals(request, *args, **kwargs):
        """Получение списка рефералов пользователя"""
        profile = ProfilesUtils.get_profile_by_user(request.user)
        refferals = {
            'phones': profile.get_referrals()
        }
        serialize = ReferralListSerializer(data=refferals)
        if serialize.is_valid():
            return ResponsesClass.ok_response(serialize.data)
        else:
            return ResponsesClass.bad_request_response(serialize.errors)
