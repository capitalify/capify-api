from datetime import datetime
from pydantic import BaseModel


class Transaction(BaseModel):
    id: int
    date: datetime
    is_income: bool
    amount: float
    description: str | None
    category: str
    subcategory: str


class TransactionCreateResponse(BaseModel):
    id: int
    message: str


class TransactionReadResponse(BaseModel):
    id: int
    message: str


class TransactionUpdateResponse(BaseModel):
    id: int
    message: str


class TransactionRemoveResponse(BaseModel):
    id: int
    message: str
