from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class PhoneValidators:
    """Класс валидации номером телефона"""

    __model_phone_validator = RegexValidator('^((\+7)[\- ]\(\d{3}\)[\- ])[\d\- ]\d{2}-\d{2}-\d{2}$',
                                         'Недопустимый формат для отправки SMS')
    __sms_phone_validator = RegexValidator('^(\+)?((\d{2,3}) ?\d|\d)(([ -]?\d)|( ?(\d{2,3}) ?)){5,12}\d$',
                                           'Недопустимый формат для модели Django')

    def sms_validate(self, value: str) -> bool:
        """Валидация номера телефона для использования в сервисе отправки SMS сообщений"""
        try:
            self.__sms_phone_validator(value)
            return True
        except ValidationError:
            return False

    def model_validate(self, value: str) -> bool:
        """Валидация номера телефона для сохранения/хранения в модели профиля пользователя"""
        try:
            self.__model_phone_validator(value)
            return True
        except ValidationError:
            return False
