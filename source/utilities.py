from datetime import datetime
from typing import Optional


def format_card_number(card_number: str) -> str:
    """
    Форматирует номер карты в формате XXXX XX** **** XXXX.
    """
    # Находим индекс, начиная с которого начинаются цифры
    digit_start_index = len(card_number)
    for i, char in enumerate(card_number):
        if char.isdigit():
            digit_start_index = i
            break
    # Разделяем текст и цифры
    card_name = card_number[:digit_start_index - 1]
    card_digits = card_number[digit_start_index:]
    # Маскируем цифры
    masked_digits = f"{card_digits[:4]} {card_digits[4:6]}** **** {card_digits[-4:]}"
    # Выводим результат
    masked_number = f"{card_name} {masked_digits}"
    return masked_number


def format_amount(amount: float, currency: str) -> str:
    """
    Форматирует сумму в нужной валюте.
    """
    return f"{amount:,.2f} {currency}"


def format_operation(date: str, operation: str, card_number: Optional[str], account: Optional[str]) -> str:
    """
    Форматирует описание операции.
    """
    formatted_date = datetime.fromisoformat(date).strftime('%d.%m.%Y')
    return f"{formatted_date} {operation}\n{format_card_number(card_number)} -> {format_card_number(account)}"
