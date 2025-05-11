from src.app.entities.account import Account
from src.app.repo.account_repository_mock import AccountRepositoryMock


class Test_AccountRepositoryMock:
    def test_get_account(self):
        repo = AccountRepositoryMock()
        account = repo.get_account()
        assert account.name == "Test Account"
        assert account.current_balance == 1000.0
        assert account.agency == "1234"
        assert account.account == "12345-6"

    def test_create_account(self):
        repo = AccountRepositoryMock()
        new_account = Account(
            name="New Account",
            current_balance=2000.0,
            agency="5678",
            account="67890-1",
        )
        created_account = repo.create_account(new_account)
        assert created_account.name == "New Account"
        assert created_account.current_balance == 2000.0
        assert created_account.agency == "5678"
        assert created_account.account == "67890-1"

    def test_update_account(self):
        repo = AccountRepositoryMock()
        updated_account = Account(
            name="Updated Account",
            current_balance=3000.0,
            agency="9101",
            account="23456-7",
        )
        account = repo.update_account(updated_account)
        assert account.name == "Updated Account"
        assert account.current_balance == 3000.0
        assert account.agency == "9101"
        assert account.account == "23456-7"

    def test_set_balance(self):
        repo = AccountRepositoryMock()
        new_balance = 5000.0
        account = repo.set_balance(new_balance)
        assert account.current_balance == new_balance

    def test_get_balance(self):
        repo = AccountRepositoryMock()
        balance = repo.get_balance()
        assert balance == 1000.0