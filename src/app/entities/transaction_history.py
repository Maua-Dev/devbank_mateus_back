from ..enums.transaction_type_enum import TransactionTypeEnum
from ..errors.entity_errors import ParamNotValidated


class TransactionHistory:
    type: TransactionTypeEnum
    value: float
    current_balance: float
    timestamp: str

    def __init__(self, type: TransactionTypeEnum, value: float, current_balance: float, timestamp: str):
        validation_transaction_type = self.validate_transaction_type(type)
        if validation_transaction_type[0] is False:
            raise ParamNotValidated("transaction_type", validation_transaction_type[1])
        
        self.type = type

        validation_value = self.validate_value(value)
        if validation_value[0] is False:
            raise ParamNotValidated("value", validation_value[1])
        
        self.value = value

        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        
        self.current_balance = current_balance

        validation_timestamp = self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        
        self.timestamp = timestamp

    @staticmethod
    def validate_transaction_type(type: TransactionTypeEnum) -> tuple[bool, str]:
        if type is None:
            return (False, "Transaction type is required")
        if type not in TransactionTypeEnum:
            return (False, "Transaction type must be a TransactionTypeEnum")
        return (True, "")
    
    @staticmethod
    def validate_value(value: float) -> tuple[bool, str]:
        if value is None:
            return (False, "Value is required")
        if type(value) != float:
            return (False, "Value must be a float")
        return (True, "")
    
    @staticmethod
    def validate_current_balance(current_balance: float) -> tuple[bool, str]:
        if current_balance is None:
            return (False, "Current balance is required")
        if type(current_balance) != float:
            return (False, "Current balance must be a float")
        return (True, "")
    
    @staticmethod
    def validate_timestamp(timestamp: str) -> tuple[bool, str]:
        if timestamp is None:
            return (False, "Timestamp is required")
        if type(timestamp) != str:
            return (False, "Timestamp must be a string")
        return (True, "")
    
    def to_dict(self) -> dict:
        return {
            'type': self.type.value,
            'value': self.value,
            'current_balance': self.current_balance,
            'timestamp': self.timestamp
        }
    
    