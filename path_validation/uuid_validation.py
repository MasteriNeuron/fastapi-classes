"""
UUID Path Validation Example

Description:
Validate UUID path parameters.

How to run:
1. uvicorn uuid_validation:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test GET /invoices/{invoice_id} using "Try it out"
"""

from fastapi import FastAPI, Path
from uuid import UUID

app = FastAPI(title="UUID Path Validation Example")

@app.get("/invoices/{invoice_id}")
def read_invoice(
    invoice_id: UUID = Path(..., description="Valid invoice UUID")
):
    return {"invoice_id": str(invoice_id)}
