"""
Subpath Capture Example

Description:
Capture a nested file path in the URL using {param:path}. Useful for assets or storage paths.

How to run:
1. uvicorn subpath_capture:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test GET /assets/{file_path} using "Try it out"

Example URL:
- /assets/css/app/main.css
- /assets/images/users/profile.jpg
"""

from fastapi import FastAPI

app = FastAPI(title="Subpath Capture Example")

@app.get("/assets/{file_path:path}")
def read_asset(file_path: str):
    return {"file_path": file_path}
