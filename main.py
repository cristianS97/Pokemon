from clases import Pokemon
from conf import base_stats
from manejo_archivos import *
import os
import random

os.system('cls')

resp = input('Desea actualizar la información? (y/n): ')
if resp.lower() == 'y':
    from consultas_api import *
    TIPOS_POKEMON = get_pokemon_types()
    POKEMON_LIST = get_pokemon_list()
    POKEMONS = get_pokemon_data(POKEMON_LIST)
    NATURES = get_pokemon_natures()
    write_types(TIPOS_POKEMON)
    write_pokemons(POKEMONS)
    write_natures(NATURES)
else:
    TIPOS_POKEMON = read_types()
    POKEMONS = read_pokemons()
    NATURES = read_natures()

players = list()

os.system('cls')

for i in range(2):
    name = input(f'Player {i+1}: ')
    players.append(name) # Lista para almacenar los pokemons deseados

os.system('cls')

while True:
    try:
        pokemons_lenght = int(input('How many pokemons do you want?: '))
    except:
        pokemons_lenght = 0
    if pokemons_lenght < 1 or pokemons_lenght > 6:
        print('Your team can\'t have more of 6 pokemons or less than 1')
    else:
        break

pokemon_ids = {
    players[0]: list(), # Ids de pokemons deseados
    players[1]: list() # Ids de pokemons deseados
}
for player in players:
    os.system('cls')
    i = 0
    while i < pokemons_lenght:
        name = input(f'{player} - What\'s the pokemon name: ')
        finded = False
        added = False
        for id in POKEMONS:
            if POKEMONS[id]['name'].lower() == name.lower():
                finded = True
                if id not in pokemon_ids[player]:
                    added = True
                    pokemon_ids[player].append(id)
                    i += 1
                    break
        if not finded:
            print('The name is incorrect')
        elif not added:
            print('Can\'t have two times the same pokemon')
        else:
            print(f'{name.lower()} added to your team')
    input('Press enter to continue')

os.system('cls')

pokemons = dict()
for player in players:
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
                ),
                random.choice(NATURES)
            )
        )

for player in players:
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
