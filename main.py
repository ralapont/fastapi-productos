from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import init_db, engine, get_session
from routers import products, categories
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código que se ejecuta al iniciar la app
    init_db()
    yield
    # Código que se ejecuta al cerrar la app (ej. cerrar conexiones)
    print("Aplicación cerrándose...")

app = FastAPI(title="Microservicio Productos y Categorías", lifespan=lifespan)

# Configuración de CORS 
app.add_middleware( CORSMiddleware, 
        allow_origins=["http://localhost:5173"], # origen de tu frontend 
        allow_credentials=True, 
        allow_methods=["*"], # GET, POST, PUT, DELETE... 
        allow_headers=["*"], # Authorization, Content-Type...
    )
                   
app.include_router(products.router)
app.include_router(categories.router)
