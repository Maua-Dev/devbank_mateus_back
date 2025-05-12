from abc import ABC, abstractmethod
from typing import List

from src.app.entities.transaction_history import TransactionHistory

class ITransactionHistoryRepository(ABC):

    @abstractmethod
    def get_transaction_history(self) -> List[TransactionHistory]:
        '''
        Returns the transaction history for a given user
        '''
        pass

    @abstractmethod
    def create_transaction_history(self, transaction_history: TransactionHistory) -> None:
        '''
        Creates a new transaction history for a given user
        '''
        pass