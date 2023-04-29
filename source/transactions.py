from dataclasses import dataclass
from typing import List


@dataclass
class Transaction:
    """
    id (int): Идентификатор транзакции.
    state (str): Статус транзакции, возможные значения: EXECUTED, CANCELED.
    date (str): Дата выполнения транзакции в формате ГГГГ-ММ-ДДTЧЧ:ММ:СС.МСК.
    amount (float): Сумма операции.
    currency (str): Название валюты операции.
    description (str): Описание операции.
    from_account (str): Номер счета или карты, с которого была произведена операция.
    to_account (str): Номер счета или карты, на который была произведена операция.
    """
    id: int
    state: str
    date: str
    amount: float
    currency: str
    description: str
    from_account: str
    to_account: str


def load_transactions_from_json(file_path: str) -> List[Transaction]:
    """
    Возвращает список объектов класса Transaction.
    :param file_path: Путь к файлу с транзакциями.
    :return: Список объектов класса Transaction.
    """
    import json
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return convert_transactions(data)


def convert_transactions(data: List[dict]) -> List[Transaction]:
    """
    Возвращает список отобранных транзакций.
    :param data: Все транзакции из json-файла.
    :return: Список отобранных по параметрам транзакций.
    """
    transactions = []
    for item in data:
        if 'from' in item and item['state'] == 'EXECUTED':
            transactions.append(Transaction(
                id=item['id'],
                state=item['state'],
                date=item['date'],
                amount=float(item['operationAmount']['amount']),
                currency=item['operationAmount']['currency']['name'],
                description=item['description'],
                from_account=item["from"],
                to_account=item['to']
            ))
    return transactions


def get_last_transactions(transactions: List[Transaction], count: int = 5) -> List[Transaction]:
    """
    Возвращает нужное количество последних транзакций из списка объектов класса Transaction.
    :param transactions: Список объектов класса Transaction.
    :param count: Количество транзакций, по умолчания равно 5.
    :return: Список объектов класса Transaction.
    """
    return sorted(transactions, key=lambda t: t.date, reverse=True)[:count]
