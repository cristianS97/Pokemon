# -*- coding: utf-8 -*-
# Autor: Cristian Sáez Mardones
# Fecha: 18-04-2021
# Versión: 2.0.1
# Objetivo: Crear un juego de batallas pokemon

# Importación de archivo
    # Si hay
# Importación de bibliotecas
    # Si hay
# Importación de funciones
    # Si hay

## Importaciones ##
# Clase para definir un Pokemon
from .clases import Pokemon, Batalla
# Función que configura los stats base del pokemon
from .conf import base_stats
# Clase para conectarse a la bbdd
from .conexiones import Conexion
## Bibliotecas ##
# Biblioteca para el manejo del so
import os
# Biblioteca para la obtención de números aleatorios y selección aleatoria de un iterable
import random

# Objeto para conectarse a la bbdd
obj_conexion = Conexion()

# Lista para guardar los nombres de los jugadores
players = list()
# Diccionario para guardar los id de los pokemon a ocupar
pokemon_ids = dict()
# Diccionario para poder almacenar los equipos pokemon
pokemons = dict()


#####################################################################
# Función: Ingresar los nombres de los jugadores
# Entrada: No hay
# Salida: No hay
def player_choice() -> None:
    # Se consultan los nombres de los jugadores
    global players
    global pokemon_ids
    while True:
        name = input(f'Player {len(players) + 1}: ')
        if name not in players:
            players.append(name) # Lista para almacenar los pokemons deseados
            pokemon_ids[name] = list()
            if len(players) == 2:
                break
        else:
            print('The player name already exists')


#####################################################################
# Función: Consultar la cantidad de pokemons en el equipo
# Entrada: No hay
# Salida: Número de pokemons
def get_pokemon_team_lenght() -> int:
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
    return pokemons_lenght


#####################################################################
# Función: Buscar los ids de los pokemon para cada equipo
# Entrada: No hay
# Salida: Número de pokemons
def search_pokemon_id(pokemons_lenght:int) -> None:
    global players
    global pokemon_ids
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
            pokemon_bbdd = obj_conexion.consultar_tabla_porsonalizada(f"select * from pokemon where name = lower('{name}')")
            if len(pokemon_bbdd) == 1:
                finded = True
                if pokemon_bbdd[0][0] not in pokemon_ids[player]:
                    added = True
                    pokemon_ids[player].append(pokemon_bbdd[0][0])
                    i += 1
                else:
                    print('You can\'t repeat pokemons on your team')
            if not finded:
                print('The name is incorrect')
            elif not added:
                print('Can\'t have two times the same pokemon')
            else:
                print(f'{name.lower()} added to your team')
        input('Press enter to continue')


#####################################################################
# Función: Crear los equipos pokemon
# Entrada: No hay
# Salida: No hay
def create_team() -> None:
    global pokemons
    global players
    global pokemon_ids
    for player in players:
        pokemons[player] = list()
        for pokemon_id in pokemon_ids[player]:
            stats = obj_conexion.consultar_tabla_porsonalizada(f"select * from base_stats where id_pokemon = {pokemon_id}")[0]
            types = list()
            types_bbdd = obj_conexion.consultar_tabla_porsonalizada(f"select type from pokemon_type pt inner join type t on t.id_type = pt.id_type inner join pokemon p on p.id_pokemon = pt.id_pokemon where p.id_pokemon = {pokemon_id}")
            for pokemon_type in types_bbdd:
                types.append(pokemon_type[0])
            pokemons[player].append(
                Pokemon(
                    pokemon_id,
                    obj_conexion.consultar_tabla_porsonalizada(f"select name from pokemon where id_pokemon = {pokemon_id}")[0][0],
                    types,
                    base_stats(
                        stats[3],
                        stats[4],
                        stats[5],
                        stats[6],
                        stats[7],
                        stats[8]
                    ),
                    # Se escoge la naturaleza de manera aleatoria
                    random.choice(obj_conexion.consultar_tabla_porsonalizada(f"select nature from nature"))[0]
                )
            )


# Se limpia la pantalla de la consola
os.system('cls')
player_choice()
# Se limpia la pantalla de la consola
os.system('cls')
pokemons_lenght = get_pokemon_team_lenght()
search_pokemon_id(pokemons_lenght)
# Se limpia la pantalla de la consola
os.system('cls')
create_team()

# Se limpia la pantalla de la consola
os.system('cls')
obj_batalla = Batalla()

# Registramos los equipos en el objeto de batalla
obj_batalla.set_teams(pokemons)
# Seleccionamos el jugador que incia
obj_batalla.get_starter_player()
# Mostramos los equipos
obj_batalla.show_teams()