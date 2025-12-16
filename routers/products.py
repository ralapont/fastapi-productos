from fastapi import APIRouter, Depends, HTTPException
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
def list_products(session: Session = Depends(get_session)):
    return session.exec(select(Product)).all()
