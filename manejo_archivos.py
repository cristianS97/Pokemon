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
# Biblioteca para el manejo de rutas
from pathlib import Path
# Biblioteca para e manejo de ficheros JSON
import json

# Ruta del archivo
ruta = Path(__file__).resolve().parent

#####################################################################
# Función: Escribir los tipos de pokemon en un archivo json
# Entrada: diccionario con tipos de pokemon
# Salida: No hay
def write_types(types) -> None:
    with open(ruta.joinpath('archivos').joinpath('types.json'), 'w') as json_file:
        json.dump(types, json_file, indent=4)

#####################################################################
# Función: Leer el fichero json con los tipos de pokemon
# Entrada: No hay entrada en la función
# Salida: Lista con los tipos de pokemon
def read_types() -> dict:
    with open(ruta.joinpath('archivos').joinpath('types.json')) as json_file:
        TIPOS_POKEMON = json.load(json_file)['types']
    return TIPOS_POKEMON

#####################################################################
# Función: Escribir los pokemon junto a sus datos en un archivo json
# Entrada: diccionario con tipos de pokemon
# Salida: No hay
def write_pokemons(pokemons) -> None:
    with open(ruta.joinpath('archivos').joinpath('pokemons.json'), 'w') as json_file:
        json.dump(pokemons, json_file, indent=4)

#####################################################################
# Función: Leer el fichero json con los pokemon
# Entrada: No hay entrada en la función
# Salida: Diccionario con la información de los pokemon
def read_pokemons() -> dict:
    with open(ruta.joinpath('archivos').joinpath('pokemons.json')) as json_file:
        POKEMONS = json.load(json_file)['pokemons']
    return POKEMONS

#####################################################################
# Función: Escribir las naturalezas pokemon en un archivo json
# Entrada: diccionario con naturalezas de pokemon
# Salida: No hay
def write_natures(natures) -> None:
    with open(ruta.joinpath('archivos').joinpath('natures.json'), 'w') as json_file:
        json.dump(natures, json_file, indent=4)

#####################################################################
# Función: Leer el fichero json con las naturalezas pokemon
# Entrada: No hay entrada en la función
# Salida: Lista con las naturalezas pokemon
def read_natures() -> dict:
    with open(ruta.joinpath('archivos').joinpath('natures.json')) as json_file:
        NATURES = json.load(json_file)['natures']
    return NATURES