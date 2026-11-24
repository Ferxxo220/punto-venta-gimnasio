from fastapi import FastAPI

# Importa models para registrar las tablas en Base.metadata antes de crearlas.
from app import models  # noqa: F401
from app.database import Base, engine
from app.routers import planes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Punto de Venta para Gimnasio",
    version="0.1.0",
)

app.include_router(planes.router)
