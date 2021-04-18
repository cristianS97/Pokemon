from clases import Pokemon
from conf import base_stats
from manejo_archivos import *

resp = input('Desea actualizar la información? (y/n): ')
if resp.lower() == 'y':
    from consultas_api import *
    TIPOS_POKEMON = get_pokemon_types()
    POKEMON_LIST = get_pokemon_list()
    POKEMONS = get_pokemon_data(POKEMON_LIST)
    write_types(TIPOS_POKEMON)
    write_pokemons(POKEMONS)
else:
    TIPOS_POKEMON = read_types()
    POKEMONS = read_pokemons()

pokemon_ids = [1, 4, 7]
pokemons = list()

for pokemon_id in pokemon_ids:
    pokemons.append(
        Pokemon(
            pokemon_id,
            POKEMONS[str(pokemon_id)]['name'],
            POKEMONS[str(pokemon_id)]['types'],
            base_stats(
                POKEMONS[str(pokemon_id)]['stats']['hp'],
                POKEMONS[str(pokemon_id)]['stats']['attack'],
                POKEMONS[str(pokemon_id)]['stats']['defense'],
                POKEMONS[str(pokemon_id)]['stats']['special-attack'],
                POKEMONS[str(pokemon_id)]['stats']['special-defense'],
                POKEMONS[str(pokemon_id)]['stats']['speed']
            )
        )
    )

for pokemon in pokemons:
    print(pokemon.get_info())
    # print("ATTACKS")
    # print(pokemon.get_attacks())
    print("STATS")
    print(pokemon.get_stats())
    print("\n==================\n")
