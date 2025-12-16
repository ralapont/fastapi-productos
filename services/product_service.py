from sqlmodel import Session, select
from models.product import Product
from models.category import Category
from schemas.product import ProductCreate
from fastapi import HTTPException

def create_product(session: Session, product_data: ProductCreate) -> Product:
    # Validar que la categoría existe
    category = session.get(Category, product_data.categoria_id)
    if not category:
        raise HTTPException(status_code=400, detail="Categoría no encontrada")

    db_product = Product(**product_data.model_dump())
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

def list_products(session: Session) -> list[Product]:
    return session.exec(select(Product)).all()
