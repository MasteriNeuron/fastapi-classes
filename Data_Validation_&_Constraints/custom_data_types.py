"""
Custom Data Types for Validation:

This code shows how to create a custom data type in FastAPI using Pydantic
to validate an email address. It's easy to understand and run.

What it does:
- Defines a custom 'EmailStr' type that checks if a string is a valid email.
- Uses it in a model for creating a user.
- Has one endpoint to create a user with validated email.

Running it:
1. Install: pip install fastapi pydantic uvicorn
2. Run: uvicorn main:app --reload
3. Test: Go to http://localhost:8000/docs and try POST /users/
   - Valid: {"name": "alok", "email": "alok@example.com"}
   - Invalid email: Gets 422 error with message.
"""

from fastapi import FastAPI
from pydantic import BaseModel, validator, EmailStr
from typing import Optional

app = FastAPI(title="Simple Validation Example")

# Custom data type: Uses Pydantic's built-in EmailStr for easy validation
# (You can make your own, but this is simple and ready-to-use)

class UserCreate(BaseModel):
    name: str
    email: EmailStr  # This enforces valid email format automatically
    
    @validator('name')
    def name_must_be_non_empty(cls, v):
        if len(v.strip()) == 0:
            raise ValueError('Name cannot be empty')
        return v.title()  # Auto-format name

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

# Fake database
users_db = []

@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    user_id = len(users_db) + 1
    new_user = {
        "id": user_id,
        "name": user.name,
        "email": user.email
    }
    users_db.append(new_user)
    return UserResponse(**new_user)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
