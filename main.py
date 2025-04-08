from fastapi import FastAPI
from routes.routes import router
from db.database import Base, engine

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

# Para ejecutar: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)