from abc import abstractmethod, ABC


class AbstractStorage(ABC):
    @abstractmethod
    def add(self, name: str, amount: int) -> None:
        ...

    @abstractmethod
    def remove(self, name: str, amount: int) -> None:
        ...

    @abstractmethod
    def get_free_space(self):
        ...

    @abstractmethod
    def get_items(self):
        ...

    @abstractmethod
    def get_unique_items_count(self):
        ...
