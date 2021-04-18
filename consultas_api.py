import requests
import os
import json

# URL base para consultas api
URL = 'https://pokeapi.co/api/v2/'

def get_pokemon_type():
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
    pass








