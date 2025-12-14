
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Sweet
from ..dependencies import get_current_user, admin_only

router = APIRouter(prefix="/api/sweets")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", dependencies=[Depends(admin_only)])
def add_sweet(data: dict, db: Session = Depends(get_db)):
    sweet = Sweet(**data)
    db.add(sweet); db.commit()
    return sweet

@router.get("/", dependencies=[Depends(get_current_user)])
def list_sweets(db: Session = Depends(get_db)):
    return db.query(Sweet).all()

@router.get("/search", dependencies=[Depends(get_current_user)])
def search(name: str = "", category: str = "", min_price: float = 0, max_price: float = 1e9, db: Session = Depends(get_db)):
    return db.query(Sweet).filter(
        Sweet.name.contains(name),
        Sweet.category.contains(category),
        Sweet.price.between(min_price, max_price)
    ).all()

@router.put("/{id}", dependencies=[Depends(admin_only)])
def update_sweet(id: int, data: dict, db: Session = Depends(get_db)):
    sweet = db.get(Sweet, id)
    if not sweet:
        raise HTTPException(404)
    for k, v in data.items():
        setattr(sweet, k, v)
    db.commit()
    return sweet

@router.delete("/{id}", dependencies=[Depends(admin_only)])
def delete_sweet(id: int, db: Session = Depends(get_db)):
    sweet = db.get(Sweet, id)
    if not sweet:
        raise HTTPException(404)
    db.delete(sweet); db.commit()
    return {"message": "deleted"}

@router.post("/{id}/purchase", dependencies=[Depends(get_current_user)])
def purchase(id: int, db: Session = Depends(get_db)):
    sweet = db.get(Sweet, id)
    if not sweet or sweet.quantity <= 0:
        raise HTTPException(400, "Out of stock")
    sweet.quantity -= 1; db.commit()
    return sweet

@router.post("/{id}/restock", dependencies=[Depends(admin_only)])
def restock(id: int, amount: int, db: Session = Depends(get_db)):
    sweet = db.get(Sweet, id)
    if not sweet:
        raise HTTPException(404)
    sweet.quantity += amount; db.commit()
    return sweet
