# -*- coding: utf-8 -*-
# Autor: Cristian Sáez Mardones
# Fecha: 18-04-2021
# Versión: 2.0.1
# Objetivo: Crear un juego de batallas pokemon

# Importación de archivo
    # No hay
# Importación de bibliotecas
    # No hay
# Importación de funciones
    # No hay

#####################################################################
# Función: Definir los stats de un pokemons
# Entrada: Stats de los pokemon
# Salida: Diccionario con los stats
def base_stats(hp:int, attack:int, defense:int, sa:int, sd:int, speed:int) -> dict:
    return {
        'hp': hp,
        'attack': attack,
        'defense': defense,
        'special attack': sa,
        'special defense': sd,
        'speed': speed
    }


# URL base para consultas api
URL_API = 'https://pokeapi.co/api/v2/'