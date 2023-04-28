import pytest

import source.transactions
from source.transactions import load_transactions_from_json, get_last_transactions


def test_load_transactions_from_json():
    fixture = 'operations.json'
    assert type(load_transactions_from_json(fixture)) == list
    assert type(load_transactions_from_json(fixture)[0]) == source.transactions.Transaction
    assert len(load_transactions_from_json(fixture)) == 76
    with pytest.raises(FileNotFoundError):
        assert load_transactions_from_json('some.json')


def test_get_last_transactions():
    fixture = load_transactions_from_json('operations.json')
    assert type(get_last_transactions(fixture)) == list
    assert type(get_last_transactions(fixture)[0]) == source.transactions.Transaction
    assert len(get_last_transactions(fixture)) == 5