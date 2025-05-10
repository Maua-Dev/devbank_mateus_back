from src.app.errors.entity_errors import ParamNotValidated


class Account:
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(self, name: str=None, agency: str=None, account: str=None, current_balance: float=1000.0):
        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name

        validation_agency = self.validate_agency(agency)
        if validation_agency[0] is False:
            raise ParamNotValidated("agency", validation_agency[1])
        self.agency = agency

        validation_account = self.validate_account(account)
        if validation_account[0] is False:
            raise ParamNotValidated("account", validation_account[1])
        self.account = account

        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance

    @staticmethod
    def validate_name(name: str) -> tuple[bool, str]:
        if name is None:
            return (False, "Name is required")
        if type(name) != str:
            return (False, "Name must be a string")
        if len(name) < 3:
            return (False, "Name must be at least 3 characters long")
        return (True, "")
    
    @staticmethod
    def validate_agency(agency: str) -> tuple[bool, str]:
        if agency is None:
            return (False, "Agency is required")
        if type(agency) != str:
            return (False, "Agency must be a string")
        if len(agency) < 4:
            return (False, "Agency must be at least 4 characters long")
        return (True, "")

    @staticmethod
    def validate_account(account: str) -> tuple[bool, str]:
        if account is None:
            return (False, "Account is required")
        if type(account) != str:
            return (False, "Account must be a string")
        if len(account) < 7:
            return (False, "Account must be at least 7 characters long")
        return (True, "")
    
    @staticmethod
    def validate_current_balance(current_balance: float) -> tuple[bool, str]:
        if current_balance is None:
            return (False, "Current balance is required")
        if type(current_balance) != float:
            return (False, "Current balance must be a float")
        if current_balance < 0:
            return (False, "Current balance must be a positive number")
        return (True, "")
    
    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'agency': self.agency,
            'account': self.account,
            'current_balance': self.current_balance
        }
        