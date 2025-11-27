'''
Path Parameters Example using FastAPI
=====================================
This FastAPI application demonstrates the use of various types of path parameters.
It includes endpoints that accept different data types as path parameters, such as integers,'''
from fastapi import FastAPI
from uuid import UUID

app = FastAPI(title="Path Parameters Example")

# 1. Basic path parameter (int)
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"message": "User profile fetched", "user_id": user_id}

# 2. Mixed: Multiple path parameters + query parameter
@app.get("/users/{user_id}/orders/{order_id}")
def get_user_order(user_id: int, order_id: int, include_items: bool = False):
    return {
        "message": "Order fetched",
        "user_id": user_id,
        "order_id": order_id,
        "include_items": include_items
    }

# 3. String path parameter (filename)
@app.get("/files/{filename}")
def get_file(filename: str):
    return {"message": "File requested", "filename": filename}

# 4. Float path parameter
@app.get("/temperature/{celsius}")
def convert_temperature(celsius: float):
    fahrenheit = celsius * 9/5 + 32
    return {"celsius": celsius, "fahrenheit": fahrenheit}

# 5. Boolean path parameter
@app.get("/features/{enabled}")
def feature_status(enabled: bool):
    return {"feature_enabled": enabled}

# 6. UUID path parameter
@app.get("/payments/{payment_id}")
def get_payment(payment_id: UUID):
    return {"payment_id": str(payment_id), "status": "verified"}

# 7. Capture nested file path (supports slashes)
@app.get("/storage/{file_path:path}")
def retrieve_deep_file(file_path: str):
    return {"file_path": file_path}


"""Detailed Explanation:

How to run the application:
---------------------------
1. Open a terminal in the project directory.
2. Run the command:
       uvicorn path_params:app --reload
3. Open the browser and test the API using either:
       • Direct URLs
       • Swagger UI documentation at: http://127.0.0.1:8000/docs

Testing via Swagger UI:
----------------------
1. Go to http://127.0.0.1:8000/docs
2. Click on any endpoint in the left panel.
3. Click "Try it out", fill in the path/query parameters, and click "Execute".
4. Review the response returned by FastAPI.

Available API Endpoints:
------------------------

1) Basic Path Parameter (Integer)
   GET /users/{user_id}
   Example: /users/42
   Description: Fetch user profile by ID.

2) Multiple Path Parameters + Query Parameter
   GET /users/{user_id}/orders/{order_id}?include_items=true
   Example: /users/12/orders/55?include_items=true
   Description: Fetch a specific order for a user. Optional query parameter 'include_items'.

3) String Path Parameter
   GET /files/{filename}
   Example: /files/report%20Q4.txt
   Description: Retrieve a file by name.

4) Float Path Parameter
   GET /temperature/{celsius}
   Example: /temperature/36.6
   Description: Convert Celsius to Fahrenheit.

5) Boolean Path Parameter
   GET /features/{enabled}
   Example: /features/true, /features/0, /features/off
   Description: Enable or disable a feature.

6) UUID Path Parameter
   GET /payments/{payment_id}
   Example: /payments/8aa1b2f5-8e3d-45a3-83b5-6c2a4e9623f7
   Description: Fetch a payment by UUID.

7) Capture Subpath (with slashes)
   GET /storage/{file_path}
   Example: /storage/documents/2025/january/budget.xlsx
   Description: Retrieve a file located in nested folders.

Notes:
------
• Path parameters are automatically converted based on type hints.
• If conversion fails (e.g., passing a string where int is expected), FastAPI returns 422 Unprocessable Entity.
• Use Swagger UI (/docs) to easily test endpoints with "Try it out".
"""