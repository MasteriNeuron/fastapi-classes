"""
Project Management Example

Description:
Manage user projects with multiple path parameters, enum statuses, and UUIDs.

How to run:
1. uvicorn project:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test endpoints using "Try it out"

Example URLs:
- /users/12/projects/active
- /reports/2025/2
- /invoices/8aa1b2f5-8e3d-45a3-83b5-6c2a4e9623f7
- /storage/documents/2025/january/budget.xlsx
"""

from fastapi import FastAPI, Path
from enum import Enum
from typing import Annotated
from uuid import UUID

app = FastAPI(title="Advanced Path Operations Example")

@app.get("/users/me")
def me():
    return {"me": True}

class Status(str, Enum):
    active = "active"
    archived = "archived"

UserId = Annotated[int, Path(..., ge=1, description="Positive integer user ID")]

@app.get("/users/{user_id}/projects/{status}")
def list_projects(user_id: UserId, status: Status):
    return {"user_id": user_id, "status": status}

@app.get("/tags/{tag}")
def by_tag(
    tag: str = Path(..., pattern=r"^[a-z0-9-]{1,30}$", description="Slug format")
):
    return {"tag": tag}

@app.get("/reports/{year}/{quarter}")
def report(
    year: int = Path(..., ge=2000, le=2100),
    quarter: int = Path(..., ge=1, le=4)
):
    return {"year": year, "quarter": quarter}

@app.get("/invoices/{invoice_id}")
def invoice(invoice_id: UUID):
    return {"invoice_id": str(invoice_id)}

@app.get("/storage/{path:path}")
def storage(path: str):
    return {"path": path}
