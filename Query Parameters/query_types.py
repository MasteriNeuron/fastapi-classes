"""
Different Types of Query Parameters

Description:
Shows string, numeric, boolean, list, set, and CSV parsing in query parameters.

How to run:
1. uvicorn query_types:app --reload
2. Open browser: http://127.0.0.1:8000/docs
3. Test endpoints using "Try it out"

Examples:
- /greet?name=John
- /square?n=5
- /ratio?x=20&y=4
- /features?enabled=false
- /colors?tags=red&tags=blue
- /unique-tags?tags=python&tags=fastapi
- /csv-tags?tags=red,green,blue
"""

from fastapi import FastAPI, Query
from typing import List, Set

app = FastAPI(title="Different Types of Query Parameters Example")

@app.get("/greet")
def greet(name: str = Query("world", min_length=1)):
    return {"message": f"Hello, {name}!"}

@app.get("/square")
def square(n: int = Query(..., ge=0)):
    return {"n": n, "square": n * n}

@app.get("/ratio")
def ratio(x: float = Query(..., gt=0), y: float = Query(..., gt=0)):
    return {"ratio": x / y}

@app.get("/features")
def features(enabled: bool = Query(True)):
    return {"enabled": enabled}

@app.get("/colors")
def colors(tags: List[str] = Query([])):
    return {"tags": tags}

@app.get("/unique-tags")
def unique_tags(tags: Set[str] = Query(set())):
    return {"tags": sorted(tags)}

@app.get("/csv-tags")
def csv_tags(tags: str = Query("")):
    parsed = [t for t in tags.split(",") if t] if tags else []
    return {"tags": parsed}
