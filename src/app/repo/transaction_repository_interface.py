from abc import ABC, abstractmethod

from ..entities import transaction

class ITransactionRepository(ABC):

    @abstractmethod
    def get_all_transactions(self) -> list:
        '''
        Returns all the transactions in the database 
        '''
        pass

    @abstractmethod
    def create_transaction(self, transaction: transaction):
        '''
        Creates a new transaction in the database
        '''
        pass