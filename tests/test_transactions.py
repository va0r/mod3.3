import pytest

from source.transactions import convert_transactions, Transaction


@pytest.fixture
def data_transactions():
    return [
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412",
            "operationAmount": {
                "amount": "25780.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 26406253703545413262",
            "to": "Счет 20735820461482021315"
        },
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
            "operationAmount": {
                "amount": "92688.46",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265"
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


def test_convert_transactions(data_transactions, valid_transaction):
    transactions = convert_transactions(data_transactions)
    assert transactions[0] == valid_transaction

# import pytest
#
# import source.transactions
# from source.transactions import load_transactions_from_json, get_last_transactions
#
#
# def test_load_transactions_from_json():
#     fixture = 'operations.json'
#     assert type(load_transactions_from_json(fixture)) == list
#     assert type(load_transactions_from_json(fixture)[0]) == source.transactions.Transaction
#     assert len(load_transactions_from_json(fixture)) == 76
#     with pytest.raises(FileNotFoundError):
#         assert load_transactions_from_json('some.json')
#
#
# def test_get_last_transactions():
#     fixture = load_transactions_from_json('operations.json')
#     assert type(get_last_transactions(fixture)) == list
#     assert type(get_last_transactions(fixture)[0]) == source.transactions.Transaction
#     assert len(get_last_transactions(fixture)) == 5
