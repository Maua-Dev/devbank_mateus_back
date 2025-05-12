import pytest
from src.app.entities.transaction_history import TransactionHistory
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.errors.entity_errors import ParamNotValidated


class Test_TransactionHistory:
    def test_transaction_history(self):
        transaction_history = TransactionHistory(
            type=TransactionTypeEnum.DEPOSIT,
            value=100.0,
            current_balance=1000.0,
            timestamp="2023-10-01T10:00:00Z",
        )
        assert transaction_history.type == TransactionTypeEnum.DEPOSIT
        assert transaction_history.value == 100.0
        assert transaction_history.current_balance == 1000.0
        assert transaction_history.timestamp == "2023-10-01T10:00:00Z"

    def test_transaction_history_dict(self):
        transaction_history = TransactionHistory(
            type=TransactionTypeEnum.DEPOSIT,
            value=100.0,
            current_balance=1000.0,
            timestamp="2023-10-01T10:00:00Z",
        )
        assert transaction_history.to_dict() == {
            'type': 'deposit',
            'value': 100.0,
            'current_balance': 1000.0,
            'timestamp': '2023-10-01T10:00:00Z'
        }

    def test_transaction_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                type=None,
                value=100.0,
                current_balance=1000.0,
                timestamp="2023-10-01T10:00:00Z",
            )

    def test_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                type=TransactionTypeEnum.DEPOSIT,
                value=None,
                current_balance=1000.0,
                timestamp="2023-10-01T10:00:00Z",
            )

    def test_value_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                type=TransactionTypeEnum.DEPOSIT,
                value="invalid_value",
                current_balance=1000.0,
                timestamp="2023-10-01T10:00:00Z",
            )

    def test_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                type=TransactionTypeEnum.DEPOSIT,
                value=100.0,
                current_balance=None,
                timestamp="2023-10-01T10:00:00Z",
            )

    def test_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                type=TransactionTypeEnum.DEPOSIT,
                value=100.0,
                current_balance="invalid_balance",
                timestamp="2023-10-01T10:00:00Z",
            )

    def test_timestamp_is_none(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                type=TransactionTypeEnum.DEPOSIT,
                value=100.0,
                current_balance=1000.0,
                timestamp=None,
            )