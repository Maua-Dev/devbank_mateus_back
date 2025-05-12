from typing import Dict
from ..entities.transaction import Transaction
from ..enums.transaction_type_enum import TransactionTypeEnum
from .transaction_repository_interface import ITransactionRepository


class TransactionRepositoryMock(ITransactionRepository):
    transactions: Dict[int, Transaction]

    def __init__(self):
        self.transactions = {
            1: Transaction(transaction_type=TransactionTypeEnum.DEPOSIT, bills={
                "2": 1,
                "5": 1,
                "10": 1,
                "20": 1,
                "50": 1,
                "100": 1,
                "200": 1
            }),
            2: Transaction(transaction_type=TransactionTypeEnum.WITHDRAW, bills={
                "2": 1,
                "5": 1,
                "10": 1,
                "20": 1,
                "50": 1,
                "100": 1,
                "200": 1
            }),
        }

    def get_all_transactions(self) -> list:
        return self.transactions.values()
    
    def create_transaction(self, transaction: Transaction) -> Transaction:
        self.transactions[
            len(self.transactions) + 1
        ] = transaction
        return transaction