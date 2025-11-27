"""
Basic Query Parameters Example

Description:
Demonstrates basic and default query parameters. Shows how FastAPI automatically parses query strings.

How to run:
1. uvicorn basic_query_parameters:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test GET /items, /search, /reports, /paginate, /convert

Examples:
- /items?q=pen&limit=5
- /search?q=fastapi
- /reports?year=2025
- /paginate?page=2&per_page=50
- /convert?count=10&price=99.9&active=true
"""

from typing import Optional
from fastapi import FastAPI

app = FastAPI(title="Basic Query Parameters Example")

@app.get("/items")
def list_items(q: str = "all", limit: int = 10):
    return {"q": q, "limit": limit}

@app.get("/search")
def search(q: Optional[str] = None):
    return {"q": q}

@app.get("/reports")
def reports(year: int):
    return {"year": year}

@app.get("/paginate")
def paginate(page: int = 1, per_page: int = 20):
    return {"page": page, "per_page": per_page}

@app.get("/convert")
def convert(count: int, price: float, active: bool):
    return {"count": count, "price": price, "active": active}
