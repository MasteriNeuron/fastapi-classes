"""
Response Models Example

Description:
Shows how to use response_model to filter output and ensure correct schema.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Response Models Example")

class Book(BaseModel):
    id: int
    title: str
    price: float
    in_stock: bool

class PublicBook(BaseModel):
    id: int
    title: str

@app.post("/books", response_model=PublicBook)
def create_book(book: Book):
    # Only exposes id and title in the response
    return book
