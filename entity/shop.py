from exceptions import *
from entity.base_storage import BaseStorage


class Shop(BaseStorage):
    def __int__(self, items: dict, capacity: int = 20):
        super().__int__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProduct

        super().add(name, amount)