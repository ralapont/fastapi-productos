from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .product import Product  # solo para el tipado

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str
    nombre: str
    descripcion: Optional[str] = None

    products: List["Product"] = Relationship(back_populates="category")
