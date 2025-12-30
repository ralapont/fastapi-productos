from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models.category import Category
from schemas.category import CategoryCreate, CategoryRead

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryRead)
def create_category(category: CategoryCreate, session: Session = Depends(get_session)):
    db_category = Category.from_orm(category)
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category

@router.get("/", response_model=list[CategoryRead])
def list_categories(session: Session = Depends(get_session)):
    return session.exec(select(Category)).all()


@router.get("/{category_id}", response_model=CategoryRead)
def get_category(category_id: int, session: Session = Depends(get_session)):
    db_category = session.get(Category, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.delete("/{category_id}")
def delete_category(category_id: int, session: Session = Depends(get_session)):
    db_category = session.get(Category, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")

    session.delete(db_category)
    session.commit()
    return {"ok": True, "message": "Category deleted"}


@router.put("/{category_id}", response_model=CategoryRead)
def update_category(category_id: int, category: CategoryCreate, session: Session = Depends(get_session)):
    db_category = session.get(Category, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")

    db_category.codigo = category.codigo
    db_category.nombre = category.nombre
    db_category.descripcion = category.descripcion

    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category
