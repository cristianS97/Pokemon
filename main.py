# -*- coding: utf-8 -*-
# Autor: Cristian Sáez Mardones
# Fecha: 18-04-2021
# Versión: 1.0.0
# Objetivo: Crear un juego de batallas pokemon

# Importación de archivo
    # Si hay
# Importación de bibliotecas
    # Si hay
# Importación de funciones
    # Si hay

## Importaciones ##
# Clase para definir un Pokemon
from clases import Pokemon
# Función que configura los stats base del pokemon
from conf import base_stats
# Funciones de manejos de los ficheros json
from manejo_archivos import *
## Bibliotecas ##
# Biblioteca para el manejo del so
import os
# Biblioteca para la obtención de números aleatorios y selección aleatoria de un iterable
import random

# Se limpia la pantalla de la consola
os.system('cls')

resp = input('Desea actualizar la información? (y/n): ')
if resp.lower() == 'y':
    # Funciones para consultar la API y actualizar los ficheros json
    from consultas_api import *
    # Se consultan los endpoint de la API y se pide la información
    TIPOS_POKEMON = get_pokemon_types()
    POKEMON_LIST = get_pokemon_list()
    POKEMONS = get_pokemon_data(POKEMON_LIST)
    NATURES_LIST = get_pokemon_natures()
    NATURES = get_nature_data(NATURES_LIST)
    # Se almacena la información en archivos json
    write_types(TIPOS_POKEMON)
    write_pokemons(POKEMONS)
    write_natures(NATURES)
else:
    # Se consultan ficheros json con los datos guardados
    TIPOS_POKEMON = read_types()
    POKEMONS = read_pokemons()
    NATURES = read_natures()

# Lista para guardar los nombres de los jugadores
players = list()

# Se limpia la pantalla de la consola
os.system('cls')

# Se consultan los nombres de los jugadores
for i in range(2):
    name = input(f'Player {i+1}: ')
    players.append(name) # Lista para almacenar los pokemons deseados

# Se limpia la pantalla de la consola
os.system('cls')

# Se consulta la cantidad de pokemons a utilizar
while True:
    try:
        pokemons_lenght = int(input('How many pokemons do you want?: '))
    except:
        pokemons_lenght = 0
    # Se verifica si se escogeran entre 1 y 6 pokemon
    if pokemons_lenght < 1 or pokemons_lenght > 6:
        print('Your team can\'t have more of 6 pokemons or less than 1')
    else:
        break

# Diccionario para guardar los id de los pokemon a ocupar
pokemon_ids = {
    players[0]: list(), # Ids de pokemons deseados
    players[1]: list() # Ids de pokemons deseados
}

# Se consultan los pokemon para cada jugador
for player in players:
    # Se limpia la pantalla de la consola
    os.system('cls')
    i = 0
    while i < pokemons_lenght:
        name = input(f'{player} - What\'s the pokemon name: ')
        finded = False
        added = False
        # Se buscan los ids del pokemon deseado
        for id in POKEMONS:
            if POKEMONS[id]['name'].lower() == name.lower():
                finded = True
                # Comprobamos que el pokemon no exista en el equipo
                if id not in pokemon_ids[player]:
                    added = True
                    pokemon_ids[player].append(id)
                    i += 1
                    break
                else:
                    print('You can\'t repeat pokemons n your team')
        if not finded:
            print('The name is incorrect')
        elif not added:
            print('Can\'t have two times the same pokemon')
        else:
            print(f'{name.lower()} added to your team')
    input('Press enter to continue')

# Se limpia la pantalla de la consola
os.system('cls')

# Diccionario para poder almacenar los equipos pokemon
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
                # Se escoge la naturaleza de manera aleatoria
                random.choice(list(NATURES.keys()))
            )
        )

# Imprimimos los datos de los pokemon de cada jugador
for player in players:
    print(player)
    for pokemon in pokemons[player]:
        pokemon.update_stats(NATURES)
        print(pokemon.get_info())
        print("STATS")
        print(pokemon.get_stats())
        print("\n==================\n")
    print("\n==================\n")
    print()
