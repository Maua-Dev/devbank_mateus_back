from src.app.entities.transaction_history import TransactionHistory
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.repo.transaction_history_repository_mock import TransactionHistoryRepositoryMock


class Test_TransactionHistoryRepositoryMock:
    def test_get_all_transaction_history(self):
        repo = TransactionHistoryRepositoryMock()
        assert all([transaction_expect == transaction for transaction_expect, transaction in zip(repo.transaction_history, repo.get_transaction_history())])

    def test_create_transaction_history(self):
        repo = TransactionHistoryRepositoryMock()
        len_before = len(repo.transaction_history)
        transaction_history = TransactionHistory(
            type=TransactionTypeEnum.DEPOSIT,
            value=100.0,
            current_balance=1000.0,
            timestamp="2023-10-01T10:00:00Z",
        )
        
        repo.create_transaction_history(transaction_history=transaction_history)
        len_after = len(repo.transaction_history)

        assert len_after == len_before + 1