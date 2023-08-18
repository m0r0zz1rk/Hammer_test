from typing import Any, Optional


class IntUtils:
    """Класс методов для работы с целочисленными переменными"""

    @staticmethod
    def is_object_int(obj: Any) -> bool:
        """Проверка является ли объект целым числом"""
        return isinstance(obj, int)

    @staticmethod
    def value_to_int(obj: Any) -> Optional[int]:
        """Преобразование объекта в целочисленный формат"""
        try:
            return int(obj)
        except Exception:
            return None

    def is_object_positive_int(self, obj: Any) -> bool:
        """Проверка является ли объект положительным целым числом"""
        int_obj = obj
        if self.is_object_int(obj):
            if obj > 0:
                return True
        return False