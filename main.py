from clases import Pokemon
from conf import base_stats
from manejo_archivos import write_types

resp = input('Desea actualizar la información? (y/n): ')
if resp.lower() == 'y':
    from consultas_api import get_pokemon_type, get_pokemon_list
    TIPOS_POKEMON = get_pokemon_type()
    POKEMONS = get_pokemon_list()
    write_types(TIPOS_POKEMON)
else:
    import json
    from pathlib import Path
    ruta = Path(__file__).resolve().parent
    with open(ruta.joinpath('archivos').joinpath('types.json')) as json_file:
        TIPOS_POKEMON = json.load(json_file)['types']

print(TIPOS_POKEMON)

# pokemons = [
#     Pokemon(1, 'bulbasaur', [TIPOS_POKEMON[11], TIPOS_POKEMON[3]], ['tackle', 'vine whip'], base_stats(45, 49, 49, 65, 65, 45)),
#     Pokemon(4, 'charmander', [TIPOS_POKEMON[9]], ['growl', 'scratch'], base_stats(39, 52, 43, 60, 50, 65)),
#     Pokemon(7, 'squirtle', [TIPOS_POKEMON[10]], ['growl', 'scratch'], base_stats(44, 48, 65, 50, 64, 43))
# ]

# for pokemon in pokemons:
#     print(pokemon.get_info())
#     print("ATTACKS")
#     print(pokemon.get_attacks())
#     print("STATS")
#     print(pokemon.get_stats())
#     print("\n==================\n")
