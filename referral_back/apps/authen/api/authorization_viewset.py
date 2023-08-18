from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from apps.authen.actions.authorization_action import AuthorizationAction
from apps.authen.auth.sms_service import SMSService
from apps.authen.serializers.authorization_serializer import AuthorizationSerializer, AuthorizationResponseSerializer
from apps.authen.serializers.phone_serializer import PhoneSerializer
from apps.commons.auth_requests import AuthRequestsUtils
from apps.commons.dict import DictUtils
from apps.commons.django import DjangoUtils
from apps.commons.profiles import ProfilesUtils
from apps.commons.response import ResponsesClass
from apps.commons.rest import RestUtils
from apps.commons.validators.phone import PhoneValidators


class AuthorizationViewSet(viewsets.ViewSet):
    """Авторизация пользователя в системе"""

    ru = RestUtils()
    du = DictUtils()

    @staticmethod
    @swagger_auto_schema(
        operation_description="Проверка авторизации пользователя",
        responses={'401': 'Пользователь не авторизован',
                   '200': 'Пользователь авторизован'}
    )
    def check_auth(request, *args, **kwargs):
        """Проверка авторизации пользователя"""
        init = AuthorizationAction(request=request)
        if init.is_request_auth:
            return ResponsesClass.ok_response_no_data()
        else:
            return ResponsesClass.unauthorized_no_data()

    @swagger_auto_schema(
        request_body=PhoneSerializer,
        operation_description="Отправка запроса на авторизацию (Телефон должен быть предоставлен"
                              " в формате +7 (###) ###-##-##)",
        responses={'400': 'Произошла ошибка в процессе создания запроса на авторизацию (error в ответе)',
                   '200': 'Запрос на авторизацию создан, сформирован код авторизации и отправлен пользователю'}
    )
    def send_auth_request(self, request, *args, **kwargs):
        """Отправка кода авторизации в СМС"""
        params = ['phone']
        if not self.ru.validate_params_to_list(request, params):
            return ResponsesClass.bad_request_response(
                'Произошла ошибка - были получены некорректные данные'
            )
        request_phone = self.ru.get_request_parameter_by_key(request, 'phone')
        if not PhoneValidators().model_validate(request_phone):
            return ResponsesClass.bad_request_response(
                'Произошла ошибка - корректный формат номера телефона:+7 (XXX) XXX-XX-XX'
            )
        if not SMSService.is_client_phone_exists(request_phone):
            user, profile = DjangoUtils.create_django_user()
            ProfilesUtils.set_phone_to_profile(request_phone, profile)
        else:
            user = ProfilesUtils.get_user_by_phone(request_phone)
        auth_code = AuthRequestsUtils.create_auth_request(user)
        result = SMSService().send_sms(
            request_phone,
            auth_code
        )
        if self.du.exist_key_in_dict('error', result):
            return ResponsesClass.bad_request_response(
                f'Произошла ошибка - {self.du.get_str_value_in_dict_by_key("error", result)}'
            )
        return ResponsesClass.ok_response(
            self.du.get_str_value_in_dict_by_key("success", result)
        )

    @swagger_auto_schema(
        request_body=AuthorizationSerializer,
        operation_description="Авторизация пользователя",
        responses={'400': 'Произошла ошибка в процессе создания запроса на авторизацию (error в ответе)',
                   '200': AuthorizationResponseSerializer}
    )
    def user_authorization(self, request, *args, **kwargs):
        """Авторизация пользователя"""
        params = ['phone', 'auth_code']
        if not self.ru.validate_params_to_list(request, params):
            return ResponsesClass.bad_request_response(
                'Произошла ошибка - были получены некорректные данные'
            )
        request_phone = self.ru.get_request_parameter_by_key(request, 'phone')
        if not PhoneValidators().model_validate(request_phone):
            return ResponsesClass.bad_request_response(
                'Произошла ошибка - корректный формат номера телефона:+7 (XXX) XXX-XX-XX'
            )
        init = AuthorizationAction(request=request)
        result = init.authorization_user()
        if self.du.exist_key_in_dict('error', result):
            error = self.du.get_str_value_in_dict_by_key("error", result)
            return ResponsesClass().bad_request_response(
                f'Произошла ошибка - {error}'
            )
        return ResponsesClass.ok_response(
            result
        )
