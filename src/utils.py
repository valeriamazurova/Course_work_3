import json
from src.operation import Operation


def read_json(filename: str) -> list[dict]:
    """ Читает json файл """
    with open(filename, "r", encoding="utf-8") as file:
        result = json.load(file)
    return result


def create_operations(list_operation_dict: list[dict]) -> list[Operation]:
    """Создать список экземпляров класса Operation"""
    list_operation = []
    for count, operation in enumerate(list_operation_dict, start=1):
        try:
            list_operation.append(
                Operation(
                    operation.get("date"),
                    operation.get("state"),
                    operation.get("operationAmount").get("amount"),
                    operation.get("operationAmount").get("currency").get("name"),
                    operation.get("description"),
                    operation.get("from"),
                    operation.get("to")
                )
            )
        except BaseException as e:
            print(f"Ошибка {e} в операции номер {count}")
    return list_operation
