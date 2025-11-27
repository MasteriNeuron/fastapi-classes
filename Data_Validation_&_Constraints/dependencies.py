"""
Dependency Injection Example

Description:
Shows function and class dependencies, including header-based auth.
"""

from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI(title="Dependency Injection Example")

# Function dependency
def get_token(x_token: str | None = Header(default=None)):
    if x_token != "secret":
        raise HTTPException(status_code=401, detail="Invalid token")
    return x_token

@app.get("/secure")
def secure_area(token: str = Depends(get_token)):
    return {"ok": True}

# Class dependency
class Repo:
    def __init__(self, db: dict):
        self.db = db
    def get(self, id: int):
        return self.db.get(id, {"id": id, "title": "Unknown"})

def get_repo():
    db = {1: {"id": 1, "title": "A"}}
    return Repo(db)

@app.get("/books/{book_id}")
def get_book(book_id: int, repo: Repo = Depends(get_repo)):
    return repo.get(book_id)
