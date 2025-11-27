"""
Database Integration Example (SQLAlchemy)

Description:
Demonstrates synchronous SQLAlchemy integration with FastAPI.
"""

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

app = FastAPI(title="SQLAlchemy Integration Example")

class BookORM(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    price = Column(Float)
    in_stock = Column(Boolean)

Base.metadata.create_all(bind=engine)

class Book(BaseModel):
    id: int
    title: str
    price: float
    in_stock: bool

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books", response_model=Book, status_code=201)
def create_book(book: Book, db: Session = Depends(get_session)):
    row = BookORM(**book.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row
