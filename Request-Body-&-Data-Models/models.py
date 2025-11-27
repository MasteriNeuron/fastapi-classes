"""
Pydantic Models Example

Description:
Defines reusable Pydantic models for FastAPI request bodies. Shows basic, complex, nested, and optional fields.

How to use:
1. Import models in your main FastAPI app
2. Use them as type hints for request body parameters
"""

from typing import List, Dict, Set, Optional
from pydantic import BaseModel

# Basic Book model
class Book(BaseModel):
    id: int
    title: str
    price: float
    in_stock: bool

# Nested Author model
class Author(BaseModel):
    name: str
    email: str

# Complex Catalog model
class Catalog(BaseModel):
    name: str
    count: int
    rating: float
    live: bool
    tags: List[str]
    meta: Dict[str, str]
    unique_isbns: Set[str]
    author: Author
    description: Optional[str] = None
