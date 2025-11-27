"""
Basic Path Validation Example

Description:
Fetch a user by their numeric ID. Demonstrates required path parameter with metadata.

How to run:
1. uvicorn basic_path_validation:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test GET /users/{user_id} using "Try it out"
"""

from fastapi import FastAPI, Path

app = FastAPI(title="Basic Path Validation Example")

@app.get("/users/{user_id}")
def read_user(
    user_id: int = Path(
        ...,
        title="User ID",
        description="System-generated numerical identifier",
        example=42
    )
):
    return {"user_id": user_id}
