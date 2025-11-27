"""
Security: OAuth2 + JWT Example

Description:
Implements OAuth2 password flow with JWT tokens.
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
import jwt

app = FastAPI(title="OAuth2 JWT Example")

SECRET = "change-me"
ALGO = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends()):
    payload = {"sub": form.username, "exp": datetime.utcnow() + timedelta(minutes=30)}
    token = jwt.encode(payload, SECRET, algorithm=ALGO)
    return {"access_token": token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        data = jwt.decode(token, SECRET, algorithms=[ALGO])
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return data["sub"]

@app.get("/me")
def me(user: str = Depends(get_current_user)):
    return {"username": user}
