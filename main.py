from fastapi import FastAPI
from routers import personajes

app = FastAPI(
    title="Universo Personajes",
    description="API para el censo de personajes creados por los aprendices del curso de FastAPI",
    version="1.0.0"
)

app.include_router(personajes.router)

@app.get("/")
def ruta_raiz():
        return {
            "mensaje": "OK"
        },
    personajes = [
    {
        "nombre": "Personaje Existente",
        "clase": "Guerrero",
        "nivel": 5
    },
    {
        "nombre": "Lorena",
        "clase": "Maga",
        "nivel": 10
    }
]
