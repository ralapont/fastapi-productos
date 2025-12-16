from fastapi import APIRouter, Depends
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
