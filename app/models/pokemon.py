from sqlalchemy import Column, Integer, String
from ..database import Base

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    level = Column(Integer)

    @classmethod
    def default_pokemon(cls):
        return cls(id=1, name="Bulbasaur", type="Grass/Poison", level=5)

    @classmethod
    def from_attributes(cls, id, name, type, level):
        return cls(id=id, name=name, type=type, level=level)