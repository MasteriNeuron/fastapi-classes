"""
Numeric Range Path Validation Example

Description:
Validate numeric path parameters with bounds (ge, le, gt, lt).

How to run:
1. uvicorn numeric_range_validation:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test GET /pages/{page} and GET /products/{price} using "Try it out"
"""

from fastapi import FastAPI, Path

app = FastAPI(title="Numeric Range Validation Example")

@app.get("/pages/{page}")
def read_page(
    page: int = Path(..., ge=1, le=500, description="1 ≤ page ≤ 500")
):
    return {"page": page}

@app.get("/products/{price}")
def product_by_price(
    price: float = Path(..., gt=0.0, lt=10000.0, description="0 < price < 10000")
):
    return {"price": price}
