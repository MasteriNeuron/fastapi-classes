"""
Advanced Query Parameter Patterns

Description:
Demonstrates centralized dependencies, cross-field validation, and Pydantic models as query bundles.

How to run:
1. uvicorn advanced_query_parameters:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test endpoints using "Try it out"

Examples:
- /items-adv?page=2&per_page=50
- /range?start=10&end=20
- /search-adv?q=fastapi&lang=en&limit=10
"""

from fastapi import FastAPI, Depends, Query, HTTPException
from pydantic import BaseModel, field_validator

app = FastAPI(title="Advanced Query Parameter Patterns")

# Dependency Class for Pagination
class Pagination:
    def __init__(self, page: int, per_page: int):
        self.page = page
        self.per_page = per_page

def pagination_dep(
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100)
) -> Pagination:
    return Pagination(page, per_page)

@app.get("/items-adv")
def items_adv(p: Pagination = Depends(pagination_dep)):
    return {"page": p.page, "per_page": p.per_page}

# Cross-Field Validation
@app.get("/range")
def range_query(start: int = Query(..., ge=0), end: int = Query(..., ge=0)):
    if start > end:
        raise HTTPException(400, detail="start must be <= end")
    return {"start": start, "end": end}

# Pydantic Model as Query Bundle
class SearchParams(BaseModel):
    q: str
    lang: str | None = None
    limit: int = 20

    @field_validator("q")
    def q_not_blank(cls, v):
        if not v.strip():
            raise ValueError("q cannot be blank")
        return v

def search_params_dep(
    q: str = Query(..., min_length=1),
    lang: str | None = Query(None, min_length=2, max_length=2),
    limit: int = Query(20, ge=1, le=100)
) -> SearchParams:
    return SearchParams(q=q, lang=lang, limit=limit)

@app.get("/search-adv")
def search_adv(params: SearchParams = Depends(search_params_dep)):
    return params.model_dump()
