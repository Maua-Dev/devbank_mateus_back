from abc import ABC, abstractmethod

from ..entities.account import Account

class IAccountRepository(ABC):

    @abstractmethod
    def get_account(self) -> Account:
        '''
        Returns the account in the database 
        '''
        pass

    @abstractmethod
    def create_account(self, account: Account) -> Account:
        '''
        Creates a new account in the database
        '''
        pass

    @abstractmethod
    def update_account(self, account: Account) -> Account:
        '''
        Updates the account in the database
        '''
        pass

    @abstractmethod
    def set_balance(self, balance: float) -> Account:
        '''
        Sets the balance of the account in the database
        '''
        pass

    @abstractmethod
    def get_balance(self) -> float:
        '''
        Returns the balance of the account in the database
        '''
        pass