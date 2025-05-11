import pytest
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.errors.entity_errors import ParamNotValidated


class Test_Transaction:
    def test_transaction(self):
        transaction = Transaction(TransactionTypeEnum.DEPOSIT, {
            "2": 1,
            "5": 1,
            "10": 1,
            "20": 1,
            "50": 1,
            "100": 1,
            "200": 1
        })
        assert transaction.transaction_type == TransactionTypeEnum.DEPOSIT
        assert transaction.bills == {
            "2": 1,
            "5": 1,
            "10": 1,
            "20": 1,
            "50": 1,
            "100": 1,
            "200": 1
        }

    def test_transaction_dict(self):
        transaction = Transaction(TransactionTypeEnum.DEPOSIT, {
            "2": 1,
            "5": 1,
            "10": 1,
            "20": 1,
            "50": 1,
            "100": 1,
            "200": 1
        })
        assert transaction.to_dict() == {
            'transaction_type': 'deposit',
            'bills': {
                "2": 1,
                "5": 1,
                "10": 1,
                "20": 1,
                "50": 1,
                "100": 1,
                "200": 1
            }
        }

    def test_transaction_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type=None, bills={
                "2": 1,
                "5": 1,
                "10": 1,
                "20": 1,
                "50": 1,
                "100": 1,
                "200": 1
            })

    def test_transaction_type_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type=1.0, bills={
                "2": 1,
                "5": 1,
                "10": 1,
                "20": 1,
                "50": 1,
                "100": 1,
                "200": 1
            })

    def test_transaction_bills_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type=TransactionTypeEnum.DEPOSIT, bills=None)

    def test_transaction_bills_is_not_dict(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type=TransactionTypeEnum.DEPOSIT, bills=1.0)

    def test_transaction_bills_is_not_dict_with_7_elements(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type=TransactionTypeEnum.DEPOSIT, bills={
                "2": 1,
                "5": 1,
                "10": 1,
                "20": 1,
                "50": 1,
                "100": 1
            })

    def test_transaction_bills_is_not_dict_with_all_bills(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type=TransactionTypeEnum.DEPOSIT, bills={
                "2": 1,
                "5": 1,
                "10": 1,
                "20": 1,
                "50": 1,
                "100": 1,
                "500": 1
            })