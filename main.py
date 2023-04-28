from source.transactions import load_transactions_from_json, get_last_transactions
from source.utilities import format_amount, format_operation


def main() -> None:
    # Загрузка транзакций из JSON-файла
    transactions = load_transactions_from_json('operations.json')

    # Вывод последних пяти транзакций
    last_transactions = get_last_transactions(transactions)
    for transaction in last_transactions:
        amount_formatted = format_amount(transaction.amount, transaction.currency)
        operation_formatted = format_operation(
            transaction.date,
            transaction.description,
            transaction.from_account,
            transaction.to_account
        )
        print(f"{operation_formatted}\n{amount_formatted}\n")


if __name__ == '__main__':
    main()
