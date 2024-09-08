from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/pokemons", response_model=list[schemas.Pokemon])
def read_pokemons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pokemons = db.query(models.Pokemon).offset(skip).limit(limit).all()
    return pokemons

@router.post("/pokemons", response_model=schemas.Pokemon)
def create_pokemon(pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)):
    db_pokemon = models.Pokemon(**pokemon.dict())
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon