from sqlalchemy import Column, Integer, String
from ..database import Base

class Pokemon:
    def __init__(self, id, name, type, level):
        self.id = id
        self.name = name
        self.type = type
        self.level = level

    @classmethod
    def default_pokemon(cls):
        return cls(id=1, name="Bulbasaur", type="Grass/Poison", level=5)

    @classmethod
    def from_attributes(cls, id, name, type, level):
        return cls(id=id, name=name, type=type, level=level)