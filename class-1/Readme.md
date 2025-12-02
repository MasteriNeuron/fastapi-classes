# Testing FastAPI APIs Using Postman

## What is Postman?

Postman is a **powerful API testing tool** that allows developers and testers to interact with APIs without writing any client code. It provides a **graphical interface** for sending HTTP requests, inspecting responses, and managing API workflows. Postman can handle all HTTP methods like `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`, making it ideal for testing RESTful APIs such as the Calculator API built with FastAPI.

---

## Why Postman is Needed

When developing an API, it’s important to **verify that endpoints work correctly** before integrating them with a frontend or other systems. Postman helps in the following ways:

1. **Manual Testing of Endpoints**

   * You can manually call API endpoints to check if they behave as expected.
   * Example: Testing `/add?a=10&b=5` to ensure it returns the correct sum.

2. **Supports All HTTP Methods**

   * FastAPI endpoints use multiple HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).
   * Postman can handle requests with query parameters, JSON bodies, and path parameters.

3. **Validates Input & Output**

   * Allows you to send both valid and invalid requests to check how your API handles errors.
   * Example: Sending `b=0` to `/divide` to confirm the API returns a proper error message.

4. **Inspect Responses Easily**

   * View response data, status codes, headers, and JSON formatting.
   * Helps debug issues quickly without writing extra code.

5. **Automates Testing**

   * Postman allows saving requests and creating **collections** for repeated testing.
   * You can even write **tests** inside Postman to automatically validate responses.

6. **Supports Authentication & Headers**

   * Useful for APIs that require tokens, API keys, or custom headers.

7. **Visual API Documentation**

   * Postman provides an organized view of endpoints with parameters and examples, which complements FastAPI’s Swagger UI.

---

## How Postman Works with FastAPI

FastAPI provides a live server that listens to HTTP requests. Postman acts as a **client** sending requests to the server and receiving responses. Here’s how it connects:

1. **Start FastAPI Server**

   * Run your app using:

     ```bash
     uvicorn method_decorators:app --reload
     ```
   * Server runs at `http://127.0.0.1:8000`.

2. **Send HTTP Requests**

   * Open Postman, choose the request method (`GET`, `POST`, etc.), and enter the URL.
   * For GET requests, add query parameters directly in the URL or in the Params tab.
   * For POST, PUT, PATCH requests, send **JSON payload** in the request body.

3. **Receive Responses**

   * FastAPI sends back JSON responses automatically.
   * Postman displays the response body, HTTP status code, and headers.

4. **Test Edge Cases**

   * Send invalid data or missing fields to verify validation and error handling.
   * Example: POST `/multiply` with `"a": "text"` triggers a validation error.

---

## Example: Testing Calculator API Endpoints

* **GET /add** → Send query parameters `a` and `b`, check result.
* **POST /multiply** → Send JSON body with `a` and `b`, check multiplication.
* **PUT /divide** → Send JSON body, verify division and error handling.
* **PATCH /power** → Send JSON body, verify `a` raised to `b`.
* **DELETE /clear-history** → Call endpoint, confirm history cleared.

---
# Step-by-Step Postman Workflow for Calculator API

---

## **Step 0: Pre-requisites**

1. Ensure FastAPI server is running:

```bash
uvicorn method_decorators:app --reload
```

2. Open Postman.

---

## **Step 1: Test GET /add**

1. Click **New Request** → Name it `Addition`.
2. Select **GET** as the method.
3. URL:

```
http://127.0.0.1:8000/add?a=10&b=5
```

4. Click **Send**.
5. Expected Response:

```json
{
  "operation": "addition",
  "result": 15
}
```

> Tip: You can also click **Params** tab and enter `a` and `b` as key-value pairs.

---

## **Step 2: Test GET /subtract**

1. Create a new request → Name it `Subtraction`.
2. Method: **GET**
3. URL:

```
http://127.0.0.1:8000/subtract?a=10&b=5
```

4. Click **Send**.
5. Expected Response:

```json
{
  "operation": "subtraction",
  "result": 5
}
```

---

## **Step 3: Test POST /multiply**

1. New request → Name it `Multiplication`.
2. Method: **POST**
3. URL:

```
http://127.0.0.1:8000/multiply
```

4. Go to **Body** tab → Select **raw** → **JSON**.
5. Enter JSON payload:

```json
{
  "a": 4,
  "b": 6
}
```

6. Click **Send**.
7. Expected Response:

```json
{
  "operation": "multiplication",
  "result": 24
}
```

---

## **Step 4: Test PUT /divide**

1. New request → Name it `Division`.
2. Method: **PUT**
3. URL:

```
http://127.0.0.1:8000/divide
```

4. Body → **raw** → **JSON**

```json
{
  "a": 10,
  "b": 2
}
```

5. Click **Send**.
6. Expected Response:

```json
{
  "operation": "division",
  "result": 5
}
```

> Edge Case: Set `"b": 0` to test error handling. Expected Response:

```json
{
  "error": "Cannot divide by zero"
}
```

---

## **Step 5: Test PATCH /power**

1. New request → Name it `Power`.
2. Method: **PATCH**
3. URL:

```
http://127.0.0.1:8000/power
```

4. Body → **raw** → **JSON**

```json
{
  "a": 2,
  "b": 5
}
```

5. Click **Send**.
6. Expected Response:

```json
{
  "operation": "power",
  "result": 32
}
```

---

## **Step 6: Test DELETE /clear-history**

1. New request → Name it `Clear History`.
2. Method: **DELETE**
3. URL:

```
http://127.0.0.1:8000/clear-history
```

4. Click **Send**.
5. Expected Response:

```json
{
  "message": "Calculation history cleared successfully"
}
```

---

## **Step 7: Tips for Efficient Postman Testing**

* **Save Requests in a Collection**: Create a `Calculator API` collection to organize all endpoints.
* **Use Environment Variables**: Store base URL (`http://127.0.0.1:8000`) as a variable to avoid repeating it.
* **Test Query Parameters via Params Tab**: For GET requests, enter `a` and `b` in **Params** instead of URL string.
* **Validate Responses Automatically**: Postman allows writing tests to assert `status code` and `response body`.
* **Reuse JSON Payloads**: Save example bodies for POST, PUT, PATCH requests.

---
for more practice you can refer to this doc for realtime weather data :https://docs.google.com/document/d/1ZKqv8zjNYfCxMZippAyfFZviipCekdI6aX59Fc0MwFQ/edit?usp=sharing
This workflow allows **anyone to test all Calculator API endpoints** manually without writing a client application.

---

