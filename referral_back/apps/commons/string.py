from typing import Union, Any, Optional

from django.db.models import CharField, TextField


class StringUtils:
    """Класс методов для работы со строками"""

    @staticmethod
    def is_str_null_or_empty(text: Union[str, CharField, TextField]) -> bool:
        """Проверка является ли строка пустой или None"""
        if text is not None:
            if len(text) > 0:
                return False
        return True

    @staticmethod
    def convert_obj_to_str(obj: Any) -> Optional[str]:
        """Конвертация объекта в строку"""
        try:
            return str(obj)
        except Exception:
            return None
