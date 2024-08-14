from datetime import datetime
from pydantic import BaseModel


class Transaction(BaseModel):
    date: datetime
    is_income: bool
    amount: float
    description: str | None
    category: str
    subcategory: str
