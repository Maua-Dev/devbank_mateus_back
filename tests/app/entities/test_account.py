import pytest
from src.app.entities.account import Account
from src.app.errors.entity_errors import ParamNotValidated


class Test_Account:
    def test_account(self):
        account = Account(
            name="Test Account",
            current_balance=1000.0,
            agency="1234",
            account="12345-6",
        )

        assert account.name == "Test Account"
        assert account.current_balance == 1000.0
        assert account.agency == "1234"
        assert account.account == "12345-6"

    def test_account_invalid_name(self):
        with pytest.raises(ParamNotValidated):
            Account(
                name=None,
                current_balance=1000.0,
                agency="1234",
                account="12345-6",
            )

    def test_account_invalid_agency(self):
        with pytest.raises(ParamNotValidated):
            Account(
                name="Test Account",
                current_balance=1000.0,
                agency=None,
                account="12345-6",
            )

    def test_account_invalid_account(self):
        with pytest.raises(ParamNotValidated):
            Account(
                name="Test Account",
                current_balance=1000.0,
                agency="1234",
                account=None,
            )

    def test_account_invalid_balance(self):
        with pytest.raises(ParamNotValidated):
            Account(
                name="Test Account",
                current_balance=None,
                agency="1234",
                account="12345-6",
            )

    def test_account_invalid_balance_type(self):
        with pytest.raises(ParamNotValidated):
            Account(
                name="Test Account",
                current_balance="1000.0",
                agency="1234",
                account="12345-6",
            )
    
    def test_account_invalid_balance_value(self):
        with pytest.raises(ParamNotValidated):
            Account(
                name="Test Account",
                current_balance=-1000.0,
                agency="1234",
                account="12345-6",
            )