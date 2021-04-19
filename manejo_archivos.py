from pathlib import Path
import json

ruta = Path(__file__).resolve().parent

def write_types(types):
    with open(ruta.joinpath('archivos').joinpath('types.json'), 'w') as json_file:
        json.dump(types, json_file, indent=4)

def read_types():
    with open(ruta.joinpath('archivos').joinpath('types.json')) as json_file:
        TIPOS_POKEMON = json.load(json_file)['types']
    return TIPOS_POKEMON

def write_pokemons(pokemons):
    with open(ruta.joinpath('archivos').joinpath('pokemons.json'), 'w') as json_file:
        json.dump(pokemons, json_file, indent=4)

def read_pokemons():
    with open(ruta.joinpath('archivos').joinpath('pokemons.json')) as json_file:
        POKEMONS = json.load(json_file)['pokemons']
    return POKEMONS

def write_natures(natures):
    with open(ruta.joinpath('archivos').joinpath('natures.json'), 'w') as json_file:
        json.dump(natures, json_file, indent=4)

def read_natures():
    with open(ruta.joinpath('archivos').joinpath('natures.json')) as json_file:
        NATURES = json.load(json_file)['natures']
    return NATURES