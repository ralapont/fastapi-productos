from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class ProductBase(BaseModel):
    codigo: str
    nombre: str
    descripcion: Optional[str] = None
    precio_unitario: Decimal
    categoria_id: int

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int

    model_config = {
        "from_attributes": True
    }

