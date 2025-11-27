"""
Annotated Path Validation Example

Description:
Reusable annotated type with Path() for validation.

How to run:
1. uvicorn annotated_validation:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test GET /users/{user_id} using "Try it out"
"""

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI(title="Annotated Path Validation Example")

UserId = Annotated[int, Path(..., ge=1, description="User ID ≥ 1")]

@app.get("/users/{user_id}")
def read_user(user_id: UserId):
    return {"user_id": user_id}
