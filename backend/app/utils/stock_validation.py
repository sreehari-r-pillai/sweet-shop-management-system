
from fastapi import HTTPException

def validate_stock_availability(sweet, quantity: int):
    """
    Refactor helper:
    Ensures sufficient stock exists before purchase.
    """
    if sweet.quantity < quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient stock to complete purchase"
        )
