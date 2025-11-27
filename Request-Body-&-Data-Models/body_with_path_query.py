"""
Body with Path and Query Parameters Example

Description:
Shows how to combine path parameters, query parameters, and request body in a single endpoint.

How to run:
1. uvicorn body_with_path_query:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test POST /catalogs/{catalog_id}/books with JSON body

Example:
POST /catalogs/10/books?featured=true
Body:
{
  "id": 5,
  "title": "Advanced FastAPI",
  "price": 59.9,
  "in_stock": true
}
"""

from typing import Optional
from fastapi import FastAPI
from models import Book

app = FastAPI(title="Body with Path & Query Parameters Example")

@app.post("/catalogs/{catalog_id}/books")
def add_book(
    catalog_id: int,                # path
    book: Book,                     # body
    featured: Optional[bool] = False  # query
):
    return {"catalog_id": catalog_id, "featured": featured, "book": book}
