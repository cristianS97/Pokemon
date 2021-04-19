import requests
import os
import json

# URL base para consultas api
URL = 'https://pokeapi.co/api/v2/'

def get_pokemon_types():
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

def get_pokemon_list():
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

def get_pokemon_data(pokemons):
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

def get_pokemon_natures():
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
        
    natures = {
        'natures': natures
    }

    return natures







