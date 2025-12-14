
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        return jwt.decode(token, "CHANGE_ME", algorithms=["HS256"])
    except:
        raise HTTPException(status_code=401, detail="Unauthorized")

def admin_only(user=Depends(get_current_user)):
    if user.get("role") != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin only")
    return user
