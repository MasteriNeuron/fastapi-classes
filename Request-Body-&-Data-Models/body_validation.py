"""
Request Body Validation Example

Description:
Shows advanced validation in Pydantic models using Field().
Includes min/max length, regex patterns, numeric bounds, optional fields, and examples.

How to run:
1. uvicorn body_validation:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test POST /users with JSON body

Example JSON:
{
  "username": "fastapi_user",
  "age": 25,
  "email": "user@example.com",
  "bio": "Loves FastAPI",
  "country": "IN"
}
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Body Validation Example")

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, regex=r"^[a-zA-Z0-9_]+$")
    age: int = Field(..., ge=13, le=120)
    email: str = Field(..., regex=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    bio: str | None = Field(None, max_length=160, description="Short profile bio")
    country: str = Field("IN", example="IN")

@app.post("/users")
def create_user(user: User):
    return {"created_user": user}
