import datetime
from fastapi import FastAPI, HTTPException
from mangum import Mangum

from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum

from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum

from src.app.environments import Environments

app = FastAPI()

account_repo = Environments.get_account_repo()()
transaction_repo = Environments.get_transaction_repo()()
transaction_history_repo = Environments.get_transaction_history_repo()()

@app.get("/")
def get_account_details():
    account = account_repo.get_account()
    return account.to_dict()

@app.post("/deposit", status_code=201)
def deposit(request: dict):
    bills = request

    validation_bills = Transaction.validate_bills(bills=bills)
    if not validation_bills[0]:
        raise HTTPException(status_code=400, detail=validation_bills[1])
    
    totalSum = sum([
        bills[bill] * int(bill) for bill in bills
    ])

    old_balance = account_repo.get_balance()

    if totalSum > old_balance * 2:
        raise HTTPException(status_code=403, detail="Depósito suspeito")
    
    newTransaction = Transaction(
        transaction_type=TransactionTypeEnum.DEPOSIT,
        bills=bills
    )

    transaction_repo.create_transaction(newTransaction)

    updatedAccount = account_repo.set_balance(
        old_balance + totalSum
    )

    transaction_history_repo.create_transaction_history({
        "type": TransactionTypeEnum.DEPOSIT,
        "value": totalSum,
        "current_balance": updatedAccount.current_balance,
        "timestamp": datetime.datetime.now().isoformat(),
    })

    return {
        "current_balance": updatedAccount.current_balance,
        "timestamp": datetime.datetime.now().isoformat(),
    }

@app.post("/withdraw", status_code=201)
def withdraw(request: dict):
    bills = request

    validation_bills = Transaction.validate_bills(bills=bills)
    if not validation_bills[0]:
        raise HTTPException(status_code=400, detail=validation_bills[1])
    
    totalSum = sum([
        bills[bill] * int(bill) for bill in bills
    ])

    old_balance = account_repo.get_balance()

    if totalSum > old_balance:
        raise HTTPException(status_code=403, detail="Saque insuficiente para a transação")
    
    newTransaction = Transaction(
        transaction_type=TransactionTypeEnum.WITHDRAW,
        bills=bills
    )

    transaction_repo.create_transaction(newTransaction)

    updatedAccount = account_repo.set_balance(
        old_balance - totalSum
    )

    transaction_history_repo.create_transaction_history({
        "type": TransactionTypeEnum.WITHDRAW,
        "value": totalSum,
        "current_balance": updatedAccount.current_balance,
        "timestamp": datetime.datetime.now().isoformat(),
    })

    return {
        "current_balance": updatedAccount.current_balance,
        "timestamp": datetime.datetime.now().isoformat(),
    }

@app.get("/history")
def get_transaction_history():
    transaction_history = transaction_history_repo.get_transaction_history()
    print(transaction_history[0].to_dict())

    return {
        "all_transactions": [
            transaction for transaction in transaction_history
        ]
    }

handler = Mangum(app, lifespan="off")
