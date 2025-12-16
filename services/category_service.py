from sqlmodel import Session, select
from models.category import Category
from schemas.category import CategoryCreate

def create_category(session: Session, category_data: CategoryCreate) -> Category:
    db_category = Category(**category_data.model_dump())
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category

def list_categories(session: Session) -> list[Category]:
    return session.exec(select(Category)).all()
