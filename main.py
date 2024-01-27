from settings import JSON_FILE
from src.utils import read_json, create_operations

json_file = read_json(JSON_FILE)
list_operation = create_operations(json_file)
list_operation.sort(key=lambda data: data.date, reverse=True)
executed_list_operation = [exec_operation for exec_operation in list_operation if exec_operation.state in "EXECUTED"]

for data in executed_list_operation[:5]:
    data.reformat_date()
    data.prepare_mask_number()
    print(data)
