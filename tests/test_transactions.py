import pytest

import source.transactions
from source.transactions import convert_transactions, Transaction, load_transactions_from_json, get_last_transactions


@pytest.fixture
def data_transactions():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {
                "amount": "79931.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215"
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
            "operationAmount": {
                "amount": "77751.04",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 3928549031574026",
            "to": "Счет 84163357546688983493"
        },
    ]


@pytest.fixture()
def valid_transaction(data_transactions):
    item = data_transactions[0]
    return Transaction(
        id=item['id'],
        state=item['state'],
        date=item['date'],
        amount=float(item['operationAmount']['amount']),
        currency=item['operationAmount']['currency']['name'],
        description=item['description'],
        from_account=item["from"],
        to_account=item['to']
    )


@pytest.fixture()
def error_file_path():
    return 'error.json'


def test_convert_transactions(data_transactions, valid_transaction):
    transactions = convert_transactions(data_transactions)
    assert transactions[0] == valid_transaction
    assert len(transactions) == 3
    assert type(transactions) == list
    assert type(transactions[0]) == source.transactions.Transaction


def test_load_transactions_from_json(error_file_path):
    with pytest.raises(FileNotFoundError):
        assert load_transactions_from_json(error_file_path)


def test_get_last_transactions(data_transactions, valid_transaction):
    transactions = convert_transactions(data_transactions)
    two_last_transactions = get_last_transactions(transactions, 2)
    assert two_last_transactions[0] == valid_transaction
    assert type(two_last_transactions) == list
    assert type(two_last_transactions[0]) == source.transactions.Transaction
    assert len(two_last_transactions) == 2
    print(two_last_transactions)
