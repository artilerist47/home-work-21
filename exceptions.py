class BaseError(Exception):
    message = "Неожиданная ошибка"


class NotEnoughSpace(BaseError):
    message = "Нет места на складе"


class NotEnoughProduct(BaseError):
    message = "Нет товара на складе"


class TooManyDifferentProduct(BaseError):
    message = "Превышено допустимое количество товаров"


class InvalidRequest(BaseError):
    message = "Не верный запрос. Попробуйте снова."


class InvalidStorageName(BaseError):
    message = "Введите существующий склад"
