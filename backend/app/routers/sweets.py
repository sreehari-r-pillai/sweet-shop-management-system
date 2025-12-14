
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Sweet
from app.schemas import PurchaseRequest

# Import the refactored stock validation helper
from app.utils.stock_validation import validate_stock_availability

router = APIRouter()


@router.post("/api/sweets/{sweet_id}/purchase")
def purchase_sweet(
    sweet_id: int,
    purchase: PurchaseRequest,
    db: Session = Depends(get_db)
):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()

    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    # Refactor step: validate stock before purchase
    validate_stock_availability(sweet, purchase.quantity)

    sweet.quantity -= purchase.quantity
    db.commit()
    db.refresh(sweet)

    return {"message": "Purchase successful"}
