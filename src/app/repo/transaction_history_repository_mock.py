from typing import List
from ..entities.transaction_history import TransactionHistory
from ..enums.transaction_type_enum import TransactionTypeEnum
from .transaction_history_repository_interface import ITransactionHistoryRepository


class TransactionHistoryRepositoryMock(ITransactionHistoryRepository):
    def __init__(self):
        self.transaction_history = [
            TransactionHistory(
                type=TransactionTypeEnum.DEPOSIT,
                value=100.0,
                current_balance=1000.0,
                timestamp="2023-10-01T10:00:00Z",
            ),
            TransactionHistory(
                type=TransactionTypeEnum.WITHDRAW,
                value=50.0,
                current_balance=950.0,
                timestamp="2023-10-02T11:00:00Z",
            ),
            TransactionHistory(
                type=TransactionTypeEnum.DEPOSIT,
                value=200.0,
                current_balance=1150.0,
                timestamp="2023-10-03T12:00:00Z",
            ),
        ]

    def get_transaction_history(self) -> List[TransactionHistory]:
        return self.transaction_history
    
    def create_transaction_history(self, transaction_history: TransactionHistory) -> None:
        self.transaction_history.append(transaction_history)
        return None