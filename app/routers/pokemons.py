from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..dummys.pokemons import get_dummy_pokemons
from ..services.pokemon_service import PokemonService

router = APIRouter()

# Instancia del servicio de Pokémon
pokemon_service = PokemonService()

@router.get("/pokemones", response_model=list[schemas.Pokemon])
def read_pokemons():
    return pokemon_service.get_all_pokemons()

@router.get("/pokemones/{pokemon_id}", response_model=schemas.Pokemon)
def get_pokemon_by_id(pokemon_id: int):
    pokemon = pokemon_service.get_pokemon_by_id(pokemon_id)
    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon
@router.post("/pokemones/create_dummy", response_model=schemas.Pokemon)
def create_dummy_pokemon():
    pokemon = models.Pokemon.default_pokemon()
    return pokemon

@router.post("/pokemons/create_custom", response_model=schemas.Pokemon)
def create_custom_pokemon(pokemon: schemas.PokemonCreate):
    new_pokemon = models.Pokemon.from_attributes(
        id=pokemon.id, name=pokemon.name, type=pokemon.type, level=pokemon.level
    )
    return new_pokemon

#rutas antiguas
@router.get("/pokemons", response_model=list[schemas.Pokemon])
def read_pokemons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pokemons = db.query(models.Pokemon).offset(skip).limit(limit).all()
    return pokemons

@router.post("/pokemons", response_model=schemas.Pokemon)
def crear_pokemon(pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)):
    db_pokemon = models.Pokemon(**pokemon.dict())
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon