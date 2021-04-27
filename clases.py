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

## Bibliotecas ##
# Librería con funciones matematicas
import math

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
    # Método: Modificar los stats del pokemon
    # Entrada: stat a modificar, tipo de modificación
    # Salida: no hay
    def set_stat(self, stat:str, update:float) -> None:
        if update == 0.9:
            self.__stats[stat.replace('-', ' ')] = math.floor(self.__stats[stat.replace('-', ' ')] * update)
        else:
            self.__stats[stat.replace('-', ' ')] = math.ceil(self.__stats[stat.replace('-', ' ')] * update)

    #####################################################################
    # Método: Actualizar los stats del pokemon según su naturaleza
    # Entrada: Diccionario con stats
    # Salida: No hay
    def update_stats(self, natures_data:dict) -> None:
        stats_update = natures_data[self.get_nature()]
        if stats_update['increased_stat']:
            self.set_stat(stats_update['increased_stat'], 1.1)
        if stats_update['decreased_stat']:
            self.set_stat(stats_update['decreased_stat'], 0.9)
        
