"""
Enum Path Parameter Example

Description:
Restrict a path parameter to a fixed set of values using Enum. Demonstrates cleaner validation and docs.

How to run:
1. uvicorn enum_validation:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test GET /roles/{role} using "Try it out"

Example URLs:
- /roles/admin
- /roles/editor
- /roles/viewer
"""

from fastapi import FastAPI
from enum import Enum

app = FastAPI(title="Enum Path Parameter Example")

class Role(str, Enum):
    admin = "admin"
    editor = "editor"
    viewer = "viewer"

@app.get("/roles/{role}")
def get_role(role: Role):
    return {"role": role.value}
