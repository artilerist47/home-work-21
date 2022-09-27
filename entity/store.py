from entity.base_storage import BaseStorage


class Store(BaseStorage):
    def __int__(self, items: dict[str, int], capacity: int = 100):
        super().__int__(items, capacity)