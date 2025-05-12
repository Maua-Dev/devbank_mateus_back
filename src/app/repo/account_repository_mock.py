from ..entities.account import Account
from .account_repository_interface import IAccountRepository

class AccountRepositoryMock(IAccountRepository):
    account: Account

    def __init__(self):
        self.account = Account(
            name="Test Account",
            current_balance=1000.0,
            agency="1234",
            account="12345-6",
        )

    def get_account(self) -> Account:
        return self.account
    
    def create_account(self, account: Account) -> Account:
        self.account = account
        return account
    
    def update_account(self, account: Account) -> Account:
        self.account = account
        return account
    
    def set_balance(self, balance: float) -> Account:
        self.account.current_balance = balance
        return self.account
    
    def get_balance(self) -> float:
        return self.account.current_balance