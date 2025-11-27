"""
Single Body Parameter Example

Description:
Demonstrates how to receive a single Pydantic model in the request body.

How to run:
1. uvicorn single_body_parameter:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test POST /books with JSON body

Example JSON:
{
  "id": 1,
  "title": "Pragmatic FastAPI",
  "price": 29.9,
  "in_stock": true
}
"""

from fastapi import FastAPI
from models import Book

app = FastAPI(title="Single Body Parameter Example")

@app.post("/books")
def create_book(book: Book):
    return {"created": book}
