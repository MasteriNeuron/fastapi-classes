from fastapi import FastAPI

# Creating FastAPI application instance with metadata
app = FastAPI(
    title="My First FastAPI App",
    description="This is a basic FastAPI application showcasing a simple GET endpoint.",
    version="1.0.0",
    docs_url="/docs",          # Swagger UI path
    redoc_url="/redoc",        # ReDoc UI path
    openapi_url="/openapi.json",  # OpenAPI schema path
    contact={
        "name": "API Support",
        "email": "support@pw.live"
    },
    license_info={
        "name": "MIT License"
    },
    terms_of_service="https://pw.live/terms"
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI! Your API is running successfully."}
