import json


def read_json(filename: str) -> list[dict]:
    """ Читает json файл """
    with open(filename, "r", encoding="utf-8") as file:
        result = json.load(file)
    return result
