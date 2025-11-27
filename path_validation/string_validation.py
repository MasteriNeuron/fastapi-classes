"""
String Path Validation Example

Description:
Validate string path parameters using min_length, max_length, and regex pattern.

How to run:
1. uvicorn string_validation:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test GET /users/by-name/{username} using "Try it out"
"""

from fastapi import FastAPI, Path

app = FastAPI(title="String Path Validation Example")

@app.get("/users/by-name/{username}")
def by_name(
    username: str = Path(
        ...,
        min_length=3,
        max_length=20,
        pattern=r"^[A-Za-z0-9_]+$",
        description="3–20 characters: letters, numbers, or underscore"
    )
):
    return {"username": username}
