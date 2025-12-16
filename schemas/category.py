from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    codigo: str
    nombre: str
    descripcion: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    id: int

    class Config:
        orm_mode = True
