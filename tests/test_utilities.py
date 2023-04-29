import pytest

from source.utilities import format_amount, format_operation, format_account


@pytest.mark.parametrize(
    'amount, currency, expected',
    [
        (100, 'USD', '100.00 USD'),
        (100.20, 'EUR', '100.20 EUR'),
        (148.68, 'RUB', '148.68 RUB'),
    ]
)
def test_format_amount(amount, currency, expected):
    assert format_amount(amount, currency) == expected


@pytest.mark.parametrize(
    'date, operation,  account_from, account_to, expected',
    [
        ('2018-03-09T23:57:37.537412', 'Перевод организации', 'МИР 5211277418228469', 'Visa Gold 8326537236216459',
         '09.03.2018 Перевод организации\nМИР 5211 27** **** 8469 -> Visa Gold 8326 53** **** 6459'),
        ('2018-06-20T03:59:34.851630', 'Перевод с карты на счет', 'МИР 3766446452238784', 'Счет 86655182730188443980',
         '20.06.2018 Перевод с карты на счет\nМИР 3766 44** **** 8784 -> Счет **3980'),
        ('2018-12-24T20:16:18.819037', 'Перевод со счета на счет', 'Счет 71687416928274675290',
         'Счет 87448526688763159781', '24.12.2018 Перевод со счета на счет\nСчет **5290 -> Счет **9781')
    ]
)
def test_format_operation(date, operation, account_from, account_to, expected):
    assert format_operation(date, operation, account_from, account_to) == expected


@pytest.mark.parametrize(
    'account_data, expected',
    [
        ('МИР 5211277418228469', 'МИР 5211 27** **** 8469'),
        ('Visa Gold 8326537236216459', 'Visa Gold 8326 53** **** 6459'),
        ('МИР 3766446452238784', 'МИР 3766 44** **** 8784'),
        ('Счет 71687416928274675290', 'Счет **5290')
    ]
)
def test_format_account(account_data, expected):
    assert format_account(account_data) == expected
