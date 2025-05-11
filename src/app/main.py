import datetime
from fastapi import FastAPI, HTTPException
from mangum import Mangum

from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum

from .environments import Environments

from .repo.item_repository_mock import ItemRepositoryMock

from .errors.entity_errors import ParamNotValidated

from .enums.item_type_enum import ItemTypeEnum

from .entities.item import Item


app = FastAPI()

repo = Environments.get_item_repo()()

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

@app.get("/items/get_all_items")
def get_all_items():
    items = repo.get_all_items()
    return {
        "items": [item.to_dict() for item in items]
    }

@app.get("/items/{item_id}")
def get_item(item_id: int):
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo.get_item(item_id)
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item Not found")
    
    return {
        "item_id": item_id,
        "item": item.to_dict()    
    }

@app.post("/items/create_item", status_code=201)
def create_item(request: dict):
    item_id = request.get("item_id")
    
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo.get_item(item_id)
    if item is not None:
        raise HTTPException(status_code=409, detail="Item already exists")
    
    name = request.get("name")
    price = request.get("price")
    item_type = request.get("item_type")
    if item_type is None:
        raise HTTPException(status_code=400, detail="Item type is required")
    if type(item_type) != str:
        raise HTTPException(status_code=400, detail="Item type must be a string")
    if item_type not in [possible_type.value for possible_type in ItemTypeEnum]:
        raise HTTPException(status_code=400, detail="Item type is not a valid one")
    
    admin_permission = request.get("admin_permission")
    
    try:
        item = Item(name=name, price=price, item_type=ItemTypeEnum[item_type], admin_permission=admin_permission)
    except ParamNotValidated as err:
        raise HTTPException(status_code=400, detail=err.message)
    
    item_response = repo.create_item(item, item_id)
    return {
        "item_id": item_id,
        "item": item_response.to_dict()    
    }
    
@app.delete("/items/delete_item")
def delete_item(request: dict):
    item_id = request.get("item_id")
    
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo.get_item(item_id)
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item Not found")
    
    if item.admin_permission == True:
        raise HTTPException(status_code=403, detail="Item Not found")
    
    item_deleted = repo.delete_item(item_id)
    
    return {
        "item_id": item_id,
        "item": item_deleted.to_dict()    
    }
    
@app.put("/items/update_item")
def update_item(request: dict):
    item_id = request.get("item_id")
    
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo.get_item(item_id)
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item Not found")
    
    if item.admin_permission == True:
        raise HTTPException(status_code=403, detail="Item Not found")
    
    name = request.get("name")
    price = request.get("price")
    admin_permission = request.get("admin_permission")
    
    item_type_value = request.get("item_type")
    if item_type_value != None:
        if type(item_type_value) != str:
            raise HTTPException(status_code=400, detail="Item type must be a string")
        if item_type_value not in [possible_type.value for possible_type in ItemTypeEnum]:
            raise HTTPException(status_code=400, detail="Item type is not a valid one")
        item_type = ItemTypeEnum[item_type_value]
    else:
        item_type = None
        
    item_updated = repo.update_item(item_id, name, price, item_type, admin_permission)
    
    return {
        "item_id": item_id,
        "item": item_updated.to_dict()    
    }
    


handler = Mangum(app, lifespan="off")
