"""
Multiple Path Parameters Example

Description:
Fetch a specific item in a shop by shop ID and item ID. Demonstrates multiple path parameters with validation.

How to run:
1. uvicorn multiple_path_parameters:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test GET /shops/{shop_id}/items/{item_id} using "Try it out"

Example URL:
- /shops/5/items/12
"""

from fastapi import FastAPI, Path

app = FastAPI(title="Multiple Path Parameters Example")

@app.get("/shops/{shop_id}/items/{item_id}")
def read_item(
    shop_id: int = Path(..., ge=1, description="Shop ID must be ≥ 1"),
    item_id: int = Path(..., ge=1, description="Item ID must be ≥ 1")
):
    return {"shop_id": shop_id, "item_id": item_id}
