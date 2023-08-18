from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions

from apps.authen.actions.profile_action import ProfileAction
from apps.authen.serializers.profile_serializer import ProfileSerializer
from apps.commons.response import ResponsesClass


class ProfileViewSet(viewsets.ViewSet):
    """Получение профиля пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    @swagger_auto_schema(
        operation_description="Получение данных профиля пользователя",
        responses={'400': 'Внутренняя ошибка сервера при сериализации данных',
                   '403': 'Пользователь не авторизован',
                   '200': ProfileSerializer()}
    )
    def get_profile(self, request, *args, **kwargs):
        """Получение пользовательских данных из профиля пользователя"""
        data = ProfileAction.get_user_profile_data(request.user)
        serialize = self.serializer_class(data=data)
        if serialize.is_valid():
            return ResponsesClass.ok_response(serialize.data)
        else:
            return ResponsesClass.bad_request_response(
                f'Произошла ошибка при попытке получения данных: {serialize.errors}'
            )
