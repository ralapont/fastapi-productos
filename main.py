from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import init_db, engine, get_session
from routers import products, categories

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código que se ejecuta al iniciar la app
    init_db()
    yield
    # Código que se ejecuta al cerrar la app (ej. cerrar conexiones)
    print("Aplicación cerrándose...")

app = FastAPI(title="Microservicio Productos y Categorías", lifespan=lifespan)

app.include_router(products.router)
app.include_router(categories.router)
