import bson
from fastapi import APIRouter, HTTPException

from src.mongo import db
from src.models import Transaction

router = APIRouter(prefix="/transactions")


@router.get("/", response_model=list[Transaction])
async def get_transactions(limit: int = 10):
    transactions = await db.transactions.find().to_list(length=limit)
    return transactions


@router.post("/", response_model=Transaction)
async def create_transaction(transaction: Transaction):
    result = await db.transactions.insert_one(transaction.model_dump())
    if not result.acknowledged:
        return HTTPException(status_code=400, detail="Failed to create transaction")
    return transaction


@router.get("/{transaction_id}", response_model=Transaction)
async def read_transaction(transaction_id: str):
    if not bson.ObjectId.is_valid(transaction_id):
        return HTTPException(
            status_code=404, detail="Invalid transaction ID, not a bson.ObjectId"
        )

    transaction = await db.transactions.find_one({"_id": bson.ObjectId(transaction_id)})
    if not transaction:
        return HTTPException(status_code=400, detail="Transaction not found")
    return transaction


@router.put("/{transaction_id}", response_model=Transaction)
async def update_transaction(transaction_id: str, transaction_data: Transaction):
    if not bson.ObjectId.is_valid(transaction_id):
        return HTTPException(
            status_code=404, detail="Invalid transaction ID, not a bson.ObjectId"
        )

    transaction = await db.transactions.find_one_and_update(
        filter={"_id": bson.ObjectId(transaction_id)},
        update={"$set": transaction_data.model_dump()},
    )
    return transaction


@router.delete("/{transaction_id}")
async def remove_transaction(transaction_id: str):
    if not bson.ObjectId.is_valid(transaction_id):
        return HTTPException(
            status_code=404, detail="Invalid transaction ID, not a bson.ObjectId"
        )

    result = await db.transactions.delete_one({"_id": bson.ObjectId(transaction_id)})
    if not result.acknowledged:
        return HTTPException(status_code=400, detail="Failed to delete transaction")

    return {"message": f"Transaction {transaction_id} deleted"}
