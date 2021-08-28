# -*- coding: utf-8 -*-
# Autor: Cristian Sáez Mardones
# Fecha: 18-04-2021
# Versión: 2.0.1
# Objetivo: Crear un juego de batallas pokemon

# Importación de archivo
    # No hay
# Importación de bibliotecas
    # Si hay
# Importación de funciones
    # No hay

## Bibliotecas ##
# Librería con funciones matematicas
import math
# Clase para conectarse a la bbdd
from conexiones import Conexion
# Biblioteca para la obtención de números aleatorios y selección aleatoria de un iterable
import random


#####################################################################
# Clase que define una entidad de pokemon
class Pokemon:
    
    #####################################################################
    # Método: Inicializar al objeto pokemon
    # Entrada: Datos para definir a un pokemon
    # Salida: No hay
    def __init__(self, numero_pokedex_nacional:int, name:str, types:list, stats:dict, nature:str) -> None:
        self.__name = name
        self.__types = types
        self.__stats = stats
        self.__numero_pokedex_nacional = numero_pokedex_nacional
        self.__nature = nature
        self.update_stats()

    #####################################################################
    # Método: Obtener el número de pokedex del objeto
    # Entrada: No hay
    # Salida: Número de pokedex del pokemon
    def get_numero_pokedex_nacional(self) -> int:
        return self.__numero_pokedex_nacional

    #####################################################################
    # Método: Obtener el nombre del objeto
    # Entrada: No hay
    # Salida: Nombre del pokemon
    def get_name(self) -> str:
        return self.__name

    #####################################################################
    # Método: Obtener la naturaleza del objeto
    # Entrada: No hay
    # Salida: Número de pokedex del pokemon
    def get_nature(self) -> str:
        return self.__nature

    #####################################################################
    # Método: Obtener los tipos del pokemon
    # Entrada: No hay
    # Salida: String con el o los tipos de pokemon según corresponda
    def get_types(self) -> str:
        return ' - '.join(self.__types)
    
    #####################################################################
    # Método: Obtener información el pokemon
    # Entrada: No hay
    # Salida: String con los datos del pokemon
    def get_info(self) -> str:
        data = f"{self.get_numero_pokedex_nacional()} - {self.get_name()}"
        data += f"\nNature: {self.get_nature()}"
        data += f"\n{self.get_types()}"
        return data

    #####################################################################
    # Método: Obtener los stats del pokemon
    # Entrada: No hay
    # Salida: String con los stats del pokemon
    def get_stats(self) -> str:
        data = ""
        for i, key in enumerate(self.__stats):
            data += f"{key}: {self.__stats[key]}"
            if i < len(self.__stats) - 1:
                data += "\n"
        return data

    #####################################################################
    # Método: Obtener los stats del pokemon en un diccionario
    # Entrada: No hay
    # Salida: Diccionario con los stats de un pokemon
    def get_stats_dict(self) -> str:
        data = dict()
        for i, key in enumerate(self.__stats):
            data[key] =  self.__stats[key]
        return data

    #####################################################################
    # Método: Modificar los stats del pokemon
    # Entrada: stat a modificar, tipo de modificación
    # Salida: no hay
    def set_stat(self, stat:str, update:float) -> None:
        if update == 0.9:
            self.__stats[stat.replace('-', ' ').replace('_', ' ')] = math.floor(self.__stats[stat.replace('-', ' ').replace('_', ' ')] * update)
        else:
            self.__stats[stat.replace('-', ' ').replace('_', ' ')] = math.ceil(self.__stats[stat.replace('-', ' ').replace('_', ' ')] * update)

    #####################################################################
    # Método: Actualizar los stats del pokemon según su naturaleza
    # Entrada: Diccionario con stats
    # Salida: No hay
    def update_stats(self) -> None:
        obj_conexion = Conexion()

        stats_update = obj_conexion.consultar_tabla_porsonalizada(f"select * from nature where nature = '{self.get_nature()}'")[0]
        if stats_update[3]:
            self.set_stat(stats_update[3], 1.1)
        if stats_update[2]:
            self.set_stat(stats_update[2], 0.9)

    #####################################################################
    # Método: Recibe daño
    # Entrada: daño
    # Salida: No hay
    def get_damage(self, damage:int) -> None:
        obj_conexion = Conexion()
        self.__stats['hp'] -= damage
        if self.__stats['hp'] < 0:
            self.__stats['hp'] = 0


#####################################################################
# Clase que define una batalla pokemon
class Batalla:

    #####################################################################
    # Método: Inicializar al objeto batalla
    # Entrada: No hay
    # Salida: No hay
    def __init__(self) -> None:
        self.__turno = 0
        self.__teams = None
        self.__players = None
        self.__starter_player = None
        print("Batalla inciada")
    

    #####################################################################
    # Método: Obtener los turnos transcurridos
    # Entrada: No hay
    # Salida: Turno
    def get_turno(self) -> dict:
        return self.__turno
    

    #####################################################################
    # Método: Inicializar al objeto batalla
    # Entrada: No hay
    # Salida: No hay
    def set_turno(self) -> None:
        self.__turno += 1
    

    #####################################################################
    # Método: Registrar los jugadores en la batalla junto a sus equipos
    # Entrada: Diccionario con jugadores y equipos
    # Salida: No hay
    def set_teams(self, teams:dict) -> None:
        self.__teams = teams
        self.__players = list(self.__teams.keys())
    

    #####################################################################
    # Método: Seleccionar que entrenador inicia
    # Entrada: No hay
    # Salida: No hay
    def get_starter_player(self):
        self.__starter_player = random.choice(self.__players)
        print(f"The starter player is: {self.__starter_player}")
    

    #####################################################################
    # Método: Registrar los jugadores en la batalla junto a sus equipos
    # Entrada: Diccionario con jugadores y equipos
    # Salida: No hay
    def show_teams(self) -> None:
        for player in self.__players:
            print(player.upper())
            for pokemon in self.__teams[player]:
                print(pokemon.get_name())
                print(pokemon.get_types())
                print("\n-------------------\n")
            print("\n==================\n")
            print()
    

    #####################################################################
    # Método: Realiza ataque
    # Entrada: Jugador que ataca, Pokemon que ataca, Jugador que recibe ataque, Pokemon que recibe ataque
    # Salida: no hay
    def do_attack(self, player_attack, pokemon_attack, player_received, pokemon_received):
        print(self.__teams[player_attack][pokemon_attack].get_name() + ' attack ' + self.__teams[player_received][pokemon_received].get_name())
        print(self.__teams[player_received][pokemon_received].get_name() + ' hp: ' + str(self.__teams[player_received][pokemon_received].get_stats_dict()['hp']))
        print(self.__teams[player_attack][pokemon_attack].get_name() + ' attack: ' + str(self.__teams[player_attack][pokemon_attack].get_stats_dict()['attack']))
        damage = self.__teams[player_attack][pokemon_attack].get_stats_dict()['attack']
        self.__teams[player_received][pokemon_received].get_damage(damage)
        print(self.__teams[player_received][pokemon_received].get_name() + ' hp: ' + str(self.__teams[player_received][pokemon_received].get_stats_dict()['hp']))


    #####################################################################
    # Método: Verifica si la battala puede continuar
    # Entrada: No hay
    # Salida: Bolleano
    def battle_can_continue(self):
        for player in self.__players:
            cuenta = 0
            for pokemon in self.__teams[player]:
                if pokemon.get_stats_dict()['hp'] > 0:
                    cuenta += 1
            if cuenta == 0:
                return False
        return True
