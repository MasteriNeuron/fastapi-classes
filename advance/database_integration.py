"""
Database Integration Example (SQLAlchemy + FastAPI)


Run with:     uvicorn database_integration:app --reload
"""

from typing import Generator, List

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# -------------------------------------------------------------------
# Database setup
# -------------------------------------------------------------------
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},  # needed only for SQLite
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

Base = declarative_base()

# -------------------------------------------------------------------
# ORM model
# -------------------------------------------------------------------
class BookORM(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, default=True)


# Create tables
Base.metadata.create_all(bind=engine)

# -------------------------------------------------------------------
# Pydantic models
# -------------------------------------------------------------------
class BookCreate(BaseModel):
    title: str
    price: float
    in_stock: bool


class Book(BaseModel):
    # Used for responses (includes DB-generated ID)
    id: int
    title: str
    price: float
    in_stock: bool

    # Pydantic v2 style config
    model_config = ConfigDict(from_attributes=True)


# -------------------------------------------------------------------
# Dependency
# -------------------------------------------------------------------
def get_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------------------------------------------------
# FastAPI app
# -------------------------------------------------------------------
app = FastAPI(title="SQLAlchemy Integration Example")


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_session)):
    row = BookORM(**book.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@app.get("/books", response_model=List[Book])
def list_books(db: Session = Depends(get_session)):
    return db.query(BookORM).all()


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_session)):
    book = db.query(BookORM).filter(BookORM.id == book_id).first()
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    return book


# -------------------------------------------------------------------
# Run with: python main.py  (optional helper)
# -------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


"""
try this in httpie or curl:
 {
    "title": "Mastering FastAPI",
    "price": 29.0,
    "in_stock": true
  },
  {
    "title": "Deep Dive into SQLAlchemy",
    "price": 24.75,
    "in_stock": true
  },
  {
    "title": "The Art of Testing",
    "price": 17.99,
    "in_stock": true
  },
  {
    "title": "Clean Architecture in Practice",
    "price": 21.49,
    "in_stock": true
  },
  {
    "title": "Async Python Patterns",
    "price": 18.0,
    "in_stock": true
  },
  {
    "title": "Microservices Cookbook",
    "price": 26.5,
    "in_stock": true
  }
"""
