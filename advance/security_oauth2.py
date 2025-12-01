"""
Security: OAuth2 + JWT Example

Run the app with:
    uvicorn security_oauth2:app --reload

Requirements (install with pip):
    fastapi
    uvicorn
    PyJWT
"""

from datetime import datetime, timedelta
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt  # from PyJWT

# ------------------------------------------------------------------------------
# FastAPI app initialization
# ------------------------------------------------------------------------------
app = FastAPI(title="OAuth2 JWT Example")

# ------------------------------------------------------------------------------
# JWT / OAuth2 configuration
# ------------------------------------------------------------------------------
# NOTE: In production, NEVER hard-code this. Load from environment variable
# or a secret manager.
SECRET_KEY = "b36fd98c4da5a40f8faa86a566e9e0d6a45ea7f8b22bbbdbee52c6dce24ec232"  # <- change this to a strong random string
ALGORITHM = "HS256"

# tokenUrl should match the path for obtaining tokens (our /token endpoint)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# ------------------------------------------------------------------------------
# Fake user store (demo only)
# ------------------------------------------------------------------------------
# In a real app, you would query your database and verify hashed passwords.
fake_user_db = {
    "Bahubali": {
        "username": "Bahubali",
        # Never store plain passwords in production. Use hashed passwords!
        "password": "devsena",  # demo only
    }
}


def authenticate_user(username: str, password: str) -> Optional[dict]:
    """
    Very basic "authentication":
    - Look up the user in our fake db
    - Check plain-text password (for demo ONLY)
    """
    user = fake_user_db.get(username)
    if not user or user["password"] != password:
        return None
    return user


def create_access_token(subject: str, expires_delta: timedelta) -> str:
    """
    Create a signed JWT token with:
    - sub: the subject (e.g., username)
    - exp: expiration time
    """
    payload = {
        "sub": subject,
        "exp": datetime.utcnow() + expires_delta,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


# ------------------------------------------------------------------------------
# Routes
# ------------------------------------------------------------------------------


@app.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends()):
    """
    OAuth2 Password Flow endpoint.

    Receives form data:
        - username
        - password

    Returns:
        - access_token (JWT)
        - token_type ("bearer")

    Test with:
        curl -X POST -F "username=Bahubali" -F "password=devsena" http://localhost:8000/token
    """
    user = authenticate_user(form.username, form.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Token will be valid for 30 minutes
    access_token_expires = timedelta(minutes=30)
    token = create_access_token(subject=user["username"], expires_delta=access_token_expires)

    return {"access_token": token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    """
    Dependency that:
    - Extracts the JWT from the Authorization header (via OAuth2PasswordBearer)
    - Decodes and verifies it
    - Returns the username (sub) if valid
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: missing subject",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except jwt.ExpiredSignatureError:
        # Token has expired
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.PyJWTError:
        # Any other JWT error
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return username


@app.get("/me")
def me(current_user: str = Depends(get_current_user)):
    """
    Protected endpoint that returns the current user.

    Requires "Authorization: Bearer <token>" header.
    You can get a token from the /token endpoint.
    """
    return {"username": current_user}


# ------------------------------------------------------------------------------
# Optional: run with `python main.py`
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn

    # Runs on http://localhost:8000
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
