from ..models.pokemon import Pokemon

class PokemonService:
    def __init__(self):
        self.pokemons = [
            Pokemon(id=1, name="Bulbasaur", type="Grass/Poison", level=5),
            Pokemon(id=2, name="Charmander", type="Fire", level=5),
            Pokemon(id=3, name="Squirtle", type="Water", level=5),
            Pokemon(id=4, name="Pikachu", type="Electric", level=5),
            Pokemon(id=5, name="Jigglypuff", type="Fairy", level=3),
        ]

    def get_all_pokemons(self):
        return self.pokemons

    def get_pokemon_by_id(self, pokemon_id: int):
        for pokemon in self.pokemons:
            if pokemon.id == pokemon_id:
                return pokemon
        return None