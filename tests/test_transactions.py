from source.transactions import load_transactions_from_json, get_last_transactions


def test_load_transactions_from_json():
    assert load_transactions_from_json() == []
    ...


def test_get_last_transactions():
    assert get_last_transactions() == []
    ...
