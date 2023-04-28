from datetime import datetime
from typing import Optional


def format_card_account_number(card_account_number: str) -> str:
    """
    Форматирует номер карты или счёта в нужном формате.
    """
    return card_account_number


def format_amount(amount: float, currency: str) -> str:
    """
    Форматирует сумму в нужной валюте.
    """
    return f"{amount:,.2f} {currency}"


def format_operation(date: str, operation: str, card_account_number: Optional[str], account: Optional[str]) -> str:
    """
    Форматирует описание операции.
    """
    formatted_date = datetime.fromisoformat(date).strftime('%d.%m.%Y')
    return f"{formatted_date} {operation}\n{format_card_account_number(card_account_number)} -> {format_card_account_number(account)}"
