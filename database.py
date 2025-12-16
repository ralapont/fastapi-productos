from sqlmodel import SQLModel, create_engine, Session
from core.config import settings

# Crear el engine usando la URL del .env
engine = create_engine(settings.database_url, echo=settings.debug)

# Inicializar las tablas
def init_db():
    SQLModel.metadata.create_all(engine)

# Dependencia para inyectar sesión en routers/servicios
def get_session():
    with Session(engine) as session:
        yield session
