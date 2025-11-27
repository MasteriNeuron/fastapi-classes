"""
Custom Validation Example (Pydantic v2)

Description:
Demonstrates field-level and model-level validation in Pydantic models.
Includes normalization and cross-field validation.

How to run:
1. uvicorn custom_validation:app --reload
2. Open Swagger UI: http://127.0.0.1:8000/docs
3. Test POST /signup
"""

from fastapi import FastAPI
from pydantic import BaseModel, field_validator, model_validator

app = FastAPI(title="Custom Validation Example")

class Signup(BaseModel):
    email: str
    password: str
    confirm: str

    @field_validator("email")
    @classmethod
    def normalize_email(cls, v: str) -> str:
        """Normalize email: strip spaces and lowercase"""
        return v.strip().lower()

    @model_validator(mode="after")
    def passwords_match(self):
        """Ensure password and confirm match"""
        if self.password != self.confirm:
            raise ValueError("password and confirm must match")
        return self

@app.post("/signup")
def signup(user: Signup):
    return {"email": user.email, "status": "success"}
