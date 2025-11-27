"""
Error Handling Example

Description:
Shows usage of HTTPException and custom exception handlers in FastAPI.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="Error Handling Example")

# Pretend database
db = {1: {"id": 1, "title": "A"}}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in db:
        raise HTTPException(status_code=404, detail="Book not found")
    return db[book_id]

# Custom exception
class OutOfCreditError(Exception):
    pass

@app.exception_handler(OutOfCreditError)
def handle_credit(request: Request, exc: OutOfCreditError):
    return JSONResponse(status_code=402, content={"detail": "Insufficient credit"})

@app.get("/charge")
def charge(amount: float):
    if amount > 100:
        raise OutOfCreditError()
    return {"charged": amount}
