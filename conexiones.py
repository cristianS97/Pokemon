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
# Biblioteca para manejo de bbdd
import sqlite3
# Biblioteca para manejo de rutas
from pathlib import Path

ruta = Path(__file__).resolve().parent

class Conexion:
    def __init__(self) -> None:
        self.__conexion = None
    
    def cargar(self, tabla:str, data:tuple) -> None:
        pass

    def conectar(self) -> sqlite3.Connection:
        self.__conexion = sqlite3.connect(ruta.joinpath('bbdd').joinpath('base_pokemon.db'))
    
    def cerrar(self):
        self.__conexion.close()

    def consultar_pokemon(self, pokemon:str) -> sqlite3.Connection:
        pass
    
    def crear_tablas(self) -> None:
        self.crear_tabla_pokemon()
        self.crear_tabla_base_stats()
        self.crear_tabla_types()
        self.crear_tabla_relacion_pokemon_types()

    def crear_tabla_pokemon(self) -> None:
        sql_string = """create table if not exists pokemon(
            id_pokemon integer not null,
            name varchar(30) not null,
            constraint pk_pokemon primary key (id_pokemon)
        )"""
        self.conectar()
        self.__conexion.execute(sql_string)
        self.cerrar()
    
    def crear_tabla_base_stats(self):
        sql_string = """create table if not exists base_stats(
            id_base_stats integer not null,
            id_pokemon integer not null,
            base_experience integer not null,
            hp integer not null,
            attack integer not null,
            defense integer not null,
            special_attack integer not null,
            special_defense integer not null,
            speed integer not null,
            constraint pk_base_stats primary key (id_base_stats),
            constraint fk_base_pokemon foreign key (id_pokemon) references pokemon(id_pokemon)
        )"""
        self.conectar()
        self.__conexion.execute(sql_string)
        self.cerrar()
    
    def crear_tabla_types(self):
        sql_string = """create table if not exists type(
            id_type integer not null,
            type varchar(10) not null,
            constraint pk_type primary key (id_type)
        )"""
        self.conectar()
        self.__conexion.execute(sql_string)
        self.cerrar()
    
    def crear_tabla_relacion_pokemon_types(self):
        sql_string = """create table if not exists pokemon_type(
            id_pokemon integer not null,
            id_type integer not null,
            constraint fk_pokemon_pokemon_type foreign key (id_pokemon) references pokemon (id_pokemon),
            constraint fk_type_pokemon_type foreign key (id_type) references type (id_type)
        )"""
        self.conectar()
        self.__conexion.execute(sql_string)
        self.cerrar()

obj_conexion = Conexion()
obj_conexion.crear_tabla_pokemon()