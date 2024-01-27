from pprint import pprint

from settings import JSON_FILE
from src.operation import Operation
from src.utils import read_json

json_file = read_json(JSON_FILE)
# pprint(json_file)
list_operation = []
for count, operation in enumerate(json_file, start=1):
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
    except Exception as e:
        print(f"Ошибка операции номер {count}")

for data in list_operation:
    data.reformat_date()
    print(data)