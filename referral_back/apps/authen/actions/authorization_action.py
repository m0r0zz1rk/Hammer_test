from django.contrib.auth import login

from apps.authen.auth.authenticate import AuthBackend
from apps.authen.auth.sms_service import SMSService
from apps.commons.auth_requests import AuthRequestsUtils
from apps.commons.int import IntUtils
from apps.commons.profiles import ProfilesUtils
from apps.commons.rest import RestUtils
from apps.commons.token import TokenUtils


class AuthorizationAction:
    """Класс авторизационных действий"""

    def __init__(self, request):
        self.error = ''
        self.ru = RestUtils()
        self.pu = ProfilesUtils()
        self.request = request
        self.phone = ''

    def _is_first_time_logon(self, user_id: int) -> bool:
        """Проверка первого входа в систему"""
        return self.pu.is_first_time_logon(user_id)

    def set_false_to_first_time_logon(self, user_id: int):
        """Установка значения False на поле first_login в профиле"""
        return self.pu.set_false_to_first_time_logon(user_id)

    @property
    def is_request_auth(self) -> bool:
        """Проверка на авторизацию поступившего запроса"""
        auth = AuthBackend()
        __user = auth.authenticate(self.request)
        return __user is not None

    def authorization_user(self) -> dict:
        """Авторизация пользователя"""
        self.error = ''
        try:
            self.phone = self.ru.get_request_parameter_by_key(self.request, 'phone')
            if SMSService.is_client_phone_exists(self.phone):
                user = self.pu.get_user_by_phone(self.phone)
                code = IntUtils.value_to_int(self.ru.get_request_parameter_by_key(self.request, 'auth_code'))
                __last_code = AuthRequestsUtils.get_code_by_last_auth_request(user)
                if code == __last_code:
                    login(self.request, user)
                    AuthRequestsUtils.delete_user_auth_requests(user)
                    auth_data = TokenUtils(user.id).jwt_token()
                    return {
                        'token': auth_data['access_token'],
                        'user_id': user.id
                    }
                else:
                    self.error = 'Неверный код авторизации'
            else:
                self.error = 'Пользователь с указанным номером телефона не найден'
        except Exception:
            self.error = 'Произошла системная ошибка. Повторите попытку позже'
        return {
            'error': self.error
        }
