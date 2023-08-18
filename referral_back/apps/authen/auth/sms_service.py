import time

# import requests

from typing import Union
from django.db.models import CharField

from apps.authen.models.profiles import Profiles
from apps.commons.converts.phone import PhoneConvert
# from apps.commons.django import DjangoUtils
from apps.commons.string import StringUtils


class SMSService:
    """Отправка сообщения по номеру телефона"""

    __smsru_api_url = f'https://sms.ru/sms/send'

    @staticmethod
    def is_client_phone_exists(phone: str) -> bool:
        """Проверка на наличие в системе клиента с указанным номером телефона"""
        return Profiles.objects.filter(phone=phone).exists()

    def send_sms(self, phone: Union[str, CharField], text: str) -> dict:
        """
            Отправка SMS-сообщения клиенту
        :param phone: номер телефона клиента (формат: +7ХХХХХХХХХХ)
        :param text: текст сообщения
        :return: словарь, содержащий success и сообщение об успешной отправке
                 или error и сообщение об ошибке
        """
        result = {}
        if isinstance(phone, CharField):
            phone = StringUtils.convert_obj_to_str(phone)
        if self.is_client_phone_exists(phone):
            sms_phone = PhoneConvert().convert_model_to_sms(phone)
            if sms_phone is not None:
                try:
                    # Настройка API для сервиса отправки сообщений
                    # payload = {
                    #     'api_id': DjangoUtils().get_parameter_from_settings("SMSRU_API_KEY"),
                    #     'to': sms_phone,
                    #     'msg': text,
                    #     'json': 1
                    # }
                    # requests.get(self.__smsru_api_url,
                    #             params=payload)
                    time.sleep(2)
                    result['success'] = f'Сообщение успешно отправлено (код, который будет в СМС - {text})'
                except Exception:
                    result['error'] = 'Произошла ошибка в работе сервиса отправки сообщений'
            else:
                result['error'] = 'Произошла ошибка при конвертации номера телефона для использования сервисом' \
                                  ' отправки сообщений'
        else:
            result['error'] = 'Пользователь с указанным номером телефона не найден'
        return result
