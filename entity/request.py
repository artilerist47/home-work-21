from exceptions import *
from entity.abstract_storage import AbstractStorage


class Request:
    def __int__(self, request: str, storages: dict[str, AbstractStorage]):
        splitted_request = request.lower().split(' ')
        if len(splitted_request) != 7:
            raise InvalidRequest

        self.amount = int(splitted_request[1])
        self.product = str(splitted_request[2])
        self.departure = str(splitted_request[4])
        self.destination = str(splitted_request[6])

        if self.departure not in storages or self.destination not in storages:
            raise InvalidStorageName
