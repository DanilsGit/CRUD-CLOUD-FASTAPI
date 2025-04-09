from fastapi import FastAPI
from routes.routes import router
from db.database import Base, engine
from fastapi.staticfiles import StaticFiles

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear aplicación FastAPI
app = FastAPI(
    title="Event Management API",
    description="API para gestionar eventos",
    version="1.0.0"
)

# Incluir las rutas
app.include_router(router, prefix="/api")

# Configuración para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/", StaticFiles(directory="static", html=True), name="frontend")
