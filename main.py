from entity.shop import Shop
from entity.store import Store
from entity.request import Request
from entity.courier import Courier
from exceptions import *

store = Store(items={
    "печенька": 25,
    "собачка": 25,
    "коробка": 25
})

shop = Shop(items={
    "печенька": 2,
    "собачка": 2,
    "коробка": 2
})

storages = {
    "магазин": shop,
    "склад": store
}


def main():
    print("""\nДобрый день!\n""")

    while True:
        for storage_name in storages:
            print(f"сейчас в {storage_name}:\n {storages[storage_name]}")

        user_input = (
            """
            введите запрос в формате "Доставить 3 печеньки из склада в магазин"\n
            введите "стоп", если хотите закончить:\n
        """
        )

        if user_input in ("стоп", "stop"):
            break

        try:
            request = Request(request=user_input, storages=storages)
        except (InvalidRequest, InvalidStorageName) as error:
            print(error.message)
            continue

        courier = Courier(request=request, storages=storages)

        try:
            courier.move()
        except BaseError as error:
            print(error.message)


if __name__ == "__main__":
    main()
