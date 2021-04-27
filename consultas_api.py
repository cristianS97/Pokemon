# -*- coding: utf-8 -*-
# Autor: Cristian Sáez Mardones
# Fecha: 18-04-2021
# Versión: 1.0.0
# Objetivo: Crear un juego de batallas pokemon

# Importación de archivo
    # No hay
# Importación de bibliotecas
    # Si hay
# Importación de funciones
    # No hay

### Bibliotecas ###
# Biblioteca para peticiones http
import requests
# Biblioteca para el manejo del so
import os
# Biblioteca para el manejo de ficheros json
import json

# URL base para consultas api
URL = 'https://pokeapi.co/api/v2/'

#####################################################################
# Función: Obtener los tipos de los pokemon de la api
# Entrada: No hay entrada en la función
# Salida: Diccionario con los tipos posibles de pokemon
def get_pokemon_types() -> dict:
    print('tipos pokemon')
    response = requests.get(URL + '/type')
    response = response.content
    response = json.loads(response)

    results = response['results']

    types = list()
    for result in results:
        types.append(result['name'])
    
    types_dict = {
        'types': types
    }
    
    return types_dict

#####################################################################
# Función: Obtener lista de los nombre pokemon
# Entrada: No hay entrada en la función
# Salida: Lista con los nombres de los pokemon
def get_pokemon_list() -> list:
    print('pokemon list')
    response = requests.get(URL + '/pokemon')
    response = response.content
    response = json.loads(response)

    pokemons = list()

    for pokemon in response['results']:
        pokemons.append(pokemon['name'])
    
    while response['next']:
        response = requests.get(response['next'])
        response = response.content
        response = json.loads(response)
        for pokemon in response['results']:
            pokemons.append(pokemon['name'])

    return pokemons

#####################################################################
# Función: Obtener la información de un pokemon
# Entrada: Nombre del pokemon a consultar
# Salida: Diccionario con las estadisticas del pokemon
def get_pokemon_data(pokemons) -> dict:
    print('pokemon data')
    data_pokemons = dict()
    for pokemon in pokemons:
        response = requests.get(URL + '/pokemon/' + pokemon)
        response = response.content
        response = json.loads(response)
        # Se extraen lo datos
        stats = dict()
        for stat in response['stats']:
            stats[stat['stat']['name']] = stat['base_stat']
        types = list()
        for type_pokemon in response['types']:
            types.append(type_pokemon['type']['name'])
        data_pokemons[response['id']] = {
            'name': pokemon,
            'base_experience': response['base_experience'],
            'stats': stats,
            'types': types
        }
    data_pokemons = {
        'pokemons': data_pokemons
    }
    return data_pokemons

#####################################################################
# Función: Obtener las naturalezas de los pokemon
# Entrada: No hay entrada en la función
# Salida: Lista con las naturalezas pokemon
def get_pokemon_natures() -> list:
    print('pokemon natures')
    response = requests.get(URL + '/nature')
    response = response.content
    response = json.loads(response)

    natures = list()

    for nature in response['results']:
        natures.append(nature['name'])
    
    while response['next']:
        response = requests.get(response['next'])
        response = response.content
        response = json.loads(response)
        for nature in response['results']:
            natures.append(nature['name'])

    return natures

#####################################################################
# Función: Obtener los detalles de las naturalezas de los pokemon
# Entrada: lista de naturalezas
# Salida: Diccionario con las naturalezas pokemon
def get_nature_data(natures) -> dict:
    print('nature data')
    natures_dict = dict()
    for nature in natures:
        natures_dict[nature] = dict()
        response = requests.get(URL + '/nature/' + nature)
        response = response.content
        response = json.loads(response)
        natures_dict[nature]['decreased_stat'] = response['decreased_stat']['name'] if response['decreased_stat'] else None
        natures_dict[nature]['increased_stat'] = response['increased_stat']['name'] if response['increased_stat'] else None
    
    natures = {
        'natures': natures_dict
    }

    return natures





