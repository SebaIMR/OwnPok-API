from fastapi import FastAPI
from .routers import example, pokemons
from .database import engine, Base

app = FastAPI()

# Importa y crea las tablas si no existen
Base.metadata.create_all(bind=engine)

# Incluir routers
app.include_router(example.router)
app.include_router(pokemons.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the ownpok API!"}