"""
Multiple Body Parameters Example

Description:
Shows how to use multiple Pydantic models in a single POST request body.

How to run:
1. uvicorn multiple_body_parameters:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test POST /catalogs/{catalog_id}/place

Example JSON body:
{
  "book": {
    "id": 2,
    "title": "FastAPI for Experts",
    "price": 49.9,
    "in_stock": true
  },
  "shelf": {
    "name": "Fiction"
  }
}
"""

from fastapi import FastAPI
from models import Book
from pydantic import BaseModel

app = FastAPI(title="Multiple Body Parameters Example")

class Shelf(BaseModel):
    name: str

@app.post("/catalogs/{catalog_id}/place")
def place_book(catalog_id: int, book: Book, shelf: Shelf):
    return {"catalog_id": catalog_id, "book": book, "shelf": shelf}
