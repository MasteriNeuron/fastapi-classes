"""
Query Parameter Validation Example

Description:
Demonstrates validation using fastapi.Query for string length, numeric bounds, regex, and aliases.

How to run:
1. uvicorn query_validation:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test endpoints using "Try it out"

Examples:
- /validate?q=fastapi&page=2
- /tags?tag=python
- /price-range?min_price=10&max_price=500
- /slugs?slug=my-first-slug
- /analytics?start-date=2025-01-01&end-date=2025-12-31
- /feed?limit=50&cursor=abc123
"""

from fastapi import FastAPI, Query, HTTPException

app = FastAPI(title="Query Parameter Validation Example")

@app.get("/validate")
def validate(
    q: str = Query(..., min_length=3, max_length=50, description="Search term"),
    page: int = Query(1, ge=1, description="1-based page index")
):
    return {"q": q, "page": page}

@app.get("/tags")
def tags(tag: str = Query(..., min_length=1, max_length=30)):
    return {"tag": tag}

@app.get("/price-range")
def price_range(
    min_price: float = Query(0.0, ge=0.0),
    max_price: float = Query(1000.0, le=10000.0)
):
    if min_price > max_price:
        raise HTTPException(400, detail="min_price cannot exceed max_price")
    return {"min_price": min_price, "max_price": max_price}

@app.get("/slugs")
def slugs(slug: str = Query(..., pattern=r"^[a-z0-9-]+$")):
    return {"slug": slug}

@app.get("/analytics")
def analytics(
    start: str = Query(..., alias="start-date"),
    end: str = Query(..., alias="end-date"),
):
    return {"start": start, "end": end}

@app.get("/feed")
def feed(
    limit: int = Query(20, ge=1, le=100, description="Items per page"),
    cursor: str | None = Query(None, description="Pagination cursor"),
):
    return {"limit": limit, "cursor": cursor}
