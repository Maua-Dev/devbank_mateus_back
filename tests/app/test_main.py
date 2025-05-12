from fastapi.exceptions import HTTPException
import pytest

from src.app.main import deposit, get_account_details, get_transaction_history, withdraw
from src.app.repo.account_repository_mock import AccountRepositoryMock
from src.app.repo.transaction_history_repository_mock import TransactionHistoryRepositoryMock

class Test_Main:
    def __init__(self):
        self.account_repo = AccountRepositoryMock()
        self.transaction_history_repo = TransactionHistoryRepositoryMock()

    def test_get_account_details(self):
        response = get_account_details()
        assert response == {
            'name': self.account_repo.account.name,
            'agency': self.account_repo.account.agency,
            'account': self.account_repo.account.account,
            'current_balance': self.account_repo.account.current_balance
        }

    def test_deposit(self):
        old_balance = self.account_repo.get_balance()

        bills = {
            '2': 0,
            '5': 0,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 2,
        }

        response = deposit(request=bills)
        assert response == {
            'current_balance': old_balance + sum([
                bills[bill] * int(bill) for bill in bills
            ]),
            'timestamp': response.get('timestamp')
        }
    
    def test_deposit_bills_is_none(self):
        body = None
        with pytest.raises(HTTPException) as err:
            deposit(request=body)

    def test_withdraw(self):
        old_balance = self.account_repo.get_balance()
        
        bills = {
            '2': 1,
            '5': 0,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 0,
        }

        response = withdraw(request=bills)
        assert response == {
            'current_balance': old_balance - sum([
                bills[bill] * int(bill) for bill in bills
            ]),
            'timestamp': response.get('timestamp')
        }

    def test_transaction_history(self):
        response = get_transaction_history()
        transaction_history = self.transaction_history_repo.get_transaction_history()

        assert response == {
            "all_transactions": [transaction for transaction in transaction_history]
        }