from datetime import datetime


def format_account(account_data: str) -> str:
    """
    Маскирует карту или счет клиента.
    """
    digit_start_index = len(account_data)
    for i, char in enumerate(account_data):
        if char.isdigit():
            digit_start_index = i
            break
    account_name = account_data[:digit_start_index - 1]
    account_digits = account_data[digit_start_index:]
    if len(account_digits) == 20:
        masked_digits = f"**{account_digits[-4:]}"
    else:
        masked_digits = f"{account_digits[:4]} {account_digits[4:6]}** **** {account_digits[-4:]}"
    masked_number = f"{account_name} {masked_digits}"
    return masked_number


def format_amount(amount: float, currency: str) -> str:
    """
    Форматирует сумму в нужной валюте.
    """
    return f"{amount:,.2f} {currency}"


def format_operation(date: str, operation: str, account_from: str, account_to: str) -> str:
    """
    Форматирует описание операции.
    """
    formatted_date = datetime.fromisoformat(date).strftime('%d.%m.%Y')
    return f"{formatted_date} {operation}\n{format_account(account_from)} -> {format_account(account_to)}"
