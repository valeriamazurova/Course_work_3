from settings import JSON_FILE
from src.operation import Operation
from src.utils import read_json, create_operations


def test_read_json():
    assert read_json(JSON_FILE) is not None


def test_create_ex_class():
    list_operation = read_json(JSON_FILE)[0]
    operation = Operation(
                    list_operation.get("date"),
                    list_operation.get("state"),
                    list_operation.get("operationAmount").get("amount"),
                    list_operation.get("operationAmount").get("currency").get("name"),
                    list_operation.get("description"),
                    list_operation.get("from"),
                    list_operation.get("to")
                )
    assert isinstance(operation, Operation)
    operation.prepare_mask_number()
    assert operation.from_ == 'Maestro 1596 83** **** 5199'
    operation.reformat_date()
    assert operation.date == '26.08.2019'


def test_create_operations():
    list_operation = read_json(JSON_FILE)
    operations = create_operations(list_operation)
    assert isinstance(operations[0], Operation)

