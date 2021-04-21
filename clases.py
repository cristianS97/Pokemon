# -*- coding: utf-8 -*-
# Autor: Cristian Sáez Mardones
# Fecha: 18-04-2021
# Versión: 
# Objetivo: Crear un juego de batallas pokemon

# Importación de archivo
    # No hay
# Importación de bibliotecas
    # No hay
# Importación de funciones
    # No hay

#####################################################################
# Clase que define una entidad de pokemon
class Pokemon:
    
    #####################################################################
    # Método: Inicializar al objeto pokemon
    # Entrada: Datos para definir a un pokemon
    # Salida: No hay
    def __init__(self, numero_pokedex_nacional:int, name:str, types:list, stats:dict, nature:str):
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