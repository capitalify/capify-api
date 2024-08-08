from fastapi import APIRouter, HTTPException
from src.models import (
    Transaction,
    TransactionCreateResponse,
    TransactionReadResponse,
    TransactionUpdateResponse,
    TransactionRemoveResponse,
)

db = []
router = APIRouter(prefix="/transactions")


@router.get("/")
async def get_transactions():
    return {}


@router.post("/")
async def create_transaction(transaction: Transaction):
    return TransactionCreateResponse(id=..., message="Transaction added")


@router.get("/{transaction_id}")
async def read_transaction(transaction_id: int):
    return TransactionReadResponse(id=transaction_id, message="Transaction read")


@router.delete("/{transaction_id}")
async def remove_transaction(transaction_id: int):
    return TransactionRemoveResponse(id=transaction_id, message="Transaction removed")


@router.put("/{transaction_id}")
async def update_transaction(transaction_id: int, transaction_data: Transaction):
    if transaction_data:
        return TransactionUpdateResponse(
            id=transaction_id, message="Transaction updated"
        )
    return HTTPException(status_code=404, detail="Transaction not found")
