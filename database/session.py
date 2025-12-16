from sqlmodel import SQLModel, create_engine, Session
from core.config import settings

# Crear el engine usando la URL de la base de datos definida en .env
engine = create_engine(settings.database_url, echo=settings.debug)

# Inicializar las tablas en la base de datos
def init_db():
    SQLModel.metadata.create_all(engine)

# Dependencia para inyectar sesión en routers/servicios
def get_session():
    with Session(engine) as session:
        yield session
