from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from decimal import Decimal

if TYPE_CHECKING:
    from .category import Category
    
class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str
    nombre: str
    descripcion: Optional[str] = None
    precio_unitario: Decimal = Field(...)
    categoria_id: Optional[int] = Field(default=None, foreign_key="category.id")

    category: Optional["Category"] = Relationship(back_populates="products")


