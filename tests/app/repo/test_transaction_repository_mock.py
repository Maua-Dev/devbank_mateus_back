from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock


class Test_TransactionRepositoryMock:
    def test_get_all_transactions(self):
        repo = TransactionRepositoryMock()
        assert all([transaction_expect == transaction for transaction_expect, transaction in zip(repo.transactions.values(), repo.get_all_transactions())])

    def test_create_transaction(self):
        repo = TransactionRepositoryMock()
        len_before = len(repo.transactions)
        transaction = Transaction(transaction_type=TransactionTypeEnum.DEPOSIT, bills={
            "2": 1,
            "5": 1,
            "10": 1,
            "20": 1,
            "50": 1,
            "100": 1,
            "200": 1
        })
        
        repo.create_transaction(transaction=transaction)
        len_after = len(repo.transactions)

        assert len_after == len_before + 1