from src.app.enums.transaction_bills import TransactionBills
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.errors.entity_errors import ParamNotValidated


class Transaction:
    transaction_type: TransactionTypeEnum
    bills: dict[str, int]

    def __init__(self, transaction_type: TransactionTypeEnum, bills: dict[str, int]):
        validation_transaction_type = self.validate_transaction_type(transaction_type)
        if validation_transaction_type[0] is False:
            raise ParamNotValidated("transaction_type", validation_transaction_type[1])
        self.transaction_type = transaction_type

        validation_bills = self.validate_bills(bills)
        if validation_bills[0] is False:
            raise ParamNotValidated("bills", validation_bills[1])
        self.bills = bills

    @staticmethod
    def validate_transaction_type(transaction_type: TransactionTypeEnum) -> tuple[bool, str]:
        if transaction_type is None:
            return (False, "Transaction type is required")
        if type(transaction_type) != TransactionTypeEnum:
            return (False, "Transaction type must be a TransactionTypeEnum")
        return (True, "")
    
    @staticmethod
    def validate_bills(bills: dict[str, int]) -> tuple[bool, str]:
        if bills is None:
            return (False, "Bills are required")
        if type(bills) != dict:
            return (False, "Bills must be a dictionary")
        if list(bills.keys()) != TransactionBills:
            return (False, "Bills must be a dictionary with keys in TransactionBills")
        return (True, "")
    
    def to_dict(self) -> dict:
        return {
            'transaction_type': self.transaction_type.value,
            'bills': self.bills
        }