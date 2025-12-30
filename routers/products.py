from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from sqlmodel import Session, select
from database import get_session
from models.product import Product
from models.category import Category
from schemas.product import ProductCreate, ProductRead

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductRead)
def create_product(product: ProductCreate, session: Session = Depends(get_session)):
    # Validar que la categoría existe
    category = session.get(Category, product.categoria_id)
    if not category:
        raise HTTPException(status_code=400, detail="Categoría no encontrada")

    db_product = Product.from_orm(product)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

@router.get("/", response_model=list[ProductRead])
def list_products(categoria_id: Optional[int] = None, session: Session = Depends(get_session)):
    if categoria_id is None:
        return session.exec(select(Product)).all()
    return session.exec(select(Product).where(Product.categoria_id == categoria_id)).all()


@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: int, session: Session = Depends(get_session)):
    db_product = session.get(Product, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.put("/{product_id}", response_model=ProductRead)
def update_product(product_id: int, product: ProductCreate, session: Session = Depends(get_session)):
    db_product = session.get(Product, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Validar que la categoría existe
    category = session.get(Category, product.categoria_id)
    if not category:
        raise HTTPException(status_code=400, detail="Categoría no encontrada")

    db_product.codigo = product.codigo
    db_product.nombre = product.nombre
    db_product.descripcion = product.descripcion
    db_product.precio_unitario = product.precio_unitario
    db_product.categoria_id = product.categoria_id

    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


@router.delete("/{product_id}")
def delete_product(product_id: int, session: Session = Depends(get_session)):
    db_product = session.get(Product, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    session.delete(db_product)
    session.commit()
    return {"ok": True, "message": "Product deleted"}
