"""
Correct Path Ordering Example

Description:
Demonstrates route ordering to avoid ambiguity. Fixed paths should come before dynamic paths.

How to run:
1. uvicorn correct_path_ordering:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test GET /users/me and GET /users/{username} using "Try it out"

Example URLs:
- /users/me
- /users/johndoe
"""

from fastapi import FastAPI, Path

app = FastAPI(title="Correct Path Ordering Example")

@app.get("/users/me")
def read_me():
    return {"me": True}

@app.get("/users/{username}")
def read_user(username: str):
    return {"username": username}
