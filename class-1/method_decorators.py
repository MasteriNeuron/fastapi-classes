

"""
Calculator API using FastAPI
============================

How to run the application:
---------------------------
1. Open terminal inside the project folder.
2. Run the command:
       uvicorn method_decorators:app --reload
3. Open the browser and test the API using either:
       ▶ Direct URLs
       ▶ Swagger UI docs at: http://127.0.0.1:8000/docs

How to test using Swagger UI (/docs):
-------------------------------------
1) Go to:
       http://127.0.0.1:8000/docs
2) You will see all endpoints on the left panel.
3) Click on **GET /add**
4) Click **Try it out**
5) Enter values for `a` and `b` and click **Execute**
6) Scroll down to see the JSON response.

You may repeat this process for all other endpoints:
   • GET /subtract
   • POST /multiply
   • PUT /divide
   • PATCH /power
   • DELETE /clear-history

Available API Endpoints (Manual Testing Examples):
--------------------------------------------------

1) GET – Addition
   URL:
       http://127.0.0.1:8000/add?a=10&b=5
   Description:
       Performs addition using query parameters.

2) GET – Subtraction
   URL:
       http://127.0.0.1:8000/subtract?a=10&b=5
   Description:
       Performs subtraction using query parameters.

3) POST – Multiplication
   Endpoint:
       POST /multiply
   Request Body (JSON):
       {
         "a": 4,
         "b": 6
       }
   Description:
       Performs multiplication using JSON payload(The data that the client sends to the server in the request body.).

4) PUT – Division
   Endpoint:
       PUT /divide
   Request Body (JSON):
       {
         "a": 10,
         "b": 2
       }
   Description:
       Performs division using JSON payload.

5) PATCH – Power
   Endpoint:
       PATCH /power
   Request Body (JSON):
       {
         "a": 2,
         "b": 5
       }
   Description:
       Raises 'a' to the power of 'b'.

6) DELETE – Clear Calculation History
   Endpoint:
       DELETE /clear-history
   Description:
       Clears the stored calculation history.



Important Notes:
----------------
✔ Each decorator registers the path and HTTP method — not the function name.
   For example:

       @app.get("/add")
       def any_name_here(a: int, b: int):
           ...

   This still works because **decorator + path** decide the route.

✔ FastAPI automatically generates Swagger UI and OpenAPI documentation.
   URL:  http://127.0.0.1:8000/docs
✔ Visual documentation using ReDoc is also available.
   URL:  http://127.0.0.1:8000/redoc
"""


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Calculator API", version="1.0.0")


# ========= Data Model =========
class Operation(BaseModel):
    a: float
    b: float


# ========== GET (Read Operation) ==========
@app.get("/add")
def add(a: float, b: float):
    return {"operation": "addition", "result": a + b}


@app.get("/subtract")
def subtract(a: float, b: float):
    return {"operation": "subtraction", "result": a - b}


# ========== POST (Create Calculation Request) ==========
@app.post("/multiply")
def multiply(payload: Operation): # Payload(just a variable name) = the JSON data sent in the request body (e.g., in POST/PUT/PATCH) that FastAPI receives and processes.
    result = payload.a * payload.b
    return {"operation": "multiplication", "result": result}


# ========== PUT (Replace - divide) ==========
@app.put("/divide")
def divide(payload: Operation):
    if payload.b == 0:
        return {"error": "Cannot divide by zero"}
    result = payload.a / payload.b
    return {"operation": "division", "result": result}


# ========== PATCH (Special Operation - Power) ==========
@app.patch("/power")
def power(payload: Operation):
    result = payload.a ** payload.b
    return {"operation": "power", "result": result}


# ========== DELETE (Reset Calculator History) ==========
history = []  # dummy history storage

@app.delete("/clear-history")
def clear_history():
    history.clear()
    return {"message": "Calculation history cleared successfully"}

