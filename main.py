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

players = dict()

for i in range(2):
    name = input(f'Player {i+1}: ')
    players[name] = list() # Lista para almacenar los pokemons deseados

print()

while True:
    try:
        pokemons_lenght = int(input('How many pokemons do you want?: '))
    except:
        pokemons_lenght = 0
    if pokemons_lenght < 1 or pokemons_lenght > 6:
        print('Your team can\'t have more of 6 pokemons or less than 1')
    else:
        break

print()

pokemon_ids = {
    list(players.keys())[0]: list(), # Ids de pokemons deseados
    list(players.keys())[1]: list() # Ids de pokemons deseados
}
for player in players.keys():
    i = 0
    while i < pokemons_lenght:
        name = input(f'{player} - What\'s the pokemon name: ')
        finded = False
        for id in POKEMONS:
            if POKEMONS[id]['name'].lower() == name.lower():
                pokemon_ids[player].append(id)
                finded = True
                i += 1
                break
        if not finded:
            print('The name is incorrect')
        else:
            print(f'{name.lower()} added to your team')

print()

pokemons = dict()
for player in players.keys():
    pokemons[player] = list()
    for pokemon_id in pokemon_ids[player]:
        pokemons[player].append(
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

for player in players.keys():
    print(player)
    for pokemon in pokemons[player]:
        print(pokemon.get_info())
        # print("ATTACKS")
        # print(pokemon.get_attacks())
        print("STATS")
        print(pokemon.get_stats())
        print("\n==================\n")
    print("\n==================\n")
    print()
