import re
from typing import Optional

from apps.commons.validators.phone import PhoneValidators


class PhoneConvert:
    """Класс конвертации номера телефона в нужный формат"""

    __pv = PhoneValidators()

    def convert_model_to_sms(self, phone: str) -> Optional[str]:
        """
            Конвертация номера телефона из профиля пользователя в номер для отправки SMS
        :param phone: номер телефона в формате +7 (XXX) XXX-XX-XX
        :return: номер телефона в формате 7XXXXXXXXXX или None в случае ошибки
        """
        print(phone)
        if self.__pv.model_validate(phone):
            convert_phone = re.sub("[+ ()-]", "", phone)
            return convert_phone
        else:
            return None
