from ..models.pokemon import Pokemon
def get_dummy_pokemons():
    return [
        Pokemon(id=1, name="Bulbasaur", type="Grass/Poison", level=5),
        Pokemon(id=2, name="Charmander", type="Fire", level=5),
        Pokemon(id=3, name="Squirtle", type="Water", level=5),
        Pokemon(id=4, name="Pikachu", type="Electric", level=5),
        Pokemon(id=5, name="Jigglypuff", type="Fairy", level=3),
    ]