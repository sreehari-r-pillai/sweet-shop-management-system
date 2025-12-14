
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import User
from ..security import hash_password, verify_password, create_token

router = APIRouter(prefix="/api/auth")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(data: dict, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == data["username"]).first():
        raise HTTPException(400, "User exists")
    user = User(
        username=data["username"],
        password=hash_password(data["password"]),
        role=data.get("role", "USER")
    )
    db.add(user); db.commit()
    return {"message": "registered"}

@router.post("/login")
def login(data: dict, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data["username"]).first()
    if not user or not verify_password(data["password"], user.password):
        raise HTTPException(401, "Invalid credentials")
    return {"access_token": create_token({"username": user.username, "role": user.role})}
