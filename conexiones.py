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
    #####################################################################
    # Función: Inicializar la clase
    # Entrada: No hay
    # Salida: No hay
    def __init__(self) -> None:
        self.__conexion = None
    
    #####################################################################
    # Función: Cargar datos en la bbdd
    # Entrada: Nombre de tabla y data a insertar
    # Salida: No hay
    def cargar(self, tabla:str, data:list) -> None:
        self.conectar()
        cursor = self.__conexion.cursor()
        incognitas = "?" * len(data[0])
        while '??' in incognitas:
            incognitas = incognitas.replace('??', '?,?')
        cursor.executemany(f"insert into {tabla} values ({incognitas})", data)
        self.cerrar()

    #####################################################################
    # Función: Iniciar la conexión con la bbdd
    # Entrada: No hay
    # Salida: No hay
    def conectar(self) -> None:
        self.__conexion = sqlite3.connect(ruta.joinpath('bbdd').joinpath('base_pokemon.db'))
    
    #####################################################################
    # Función: Guardar cambios y cerrar conexión con bbdd
    # Entrada: No hay
    # Salida: No hay
    def cerrar(self) -> None:
        self.__conexion.commit()
        self.__conexion.close()

    #####################################################################
    # Función: Consultar información de un pokemon
    # Entrada: Nombre del pokemon a consultar
    # Salida: Diccionario con la información del pokemon
    def consultar_pokemon(self, pokemon:str) -> dict:
        pass
    
    #####################################################################
    # Función: Crear las tablas en la bbdd
    # Entrada: No hay
    # Salida: No hay
    def crear_tablas(self) -> None:
        self.crear_tabla_pokemon()
        self.crear_tabla_base_stats()
        self.crear_tabla_types()
        self.crear_tabla_relacion_pokemon_types()
        self.crear_tabla_nature()
        self.crear_tabla_trainer()
        self.crear_tabla_team()
        self.crear_tabla_pokemon_team()

    #####################################################################
    # Función: Crear tabla de pokemon en bbdd
    # Entrada: No hay
    # Salida: No hay
    def crear_tabla_pokemon(self) -> None:
        sql_string = """create table if not exists pokemon(
            id_pokemon integer not null,
            name varchar(30) not null,
            constraint pk_pokemon primary key (id_pokemon),
            constraint unique_pokemon_name unique (name)
        )"""
        self.conectar()
        self.__conexion.execute(sql_string)
        self.cerrar()
    
    #####################################################################
    # Función: Crear tabla de stats pokemon en bbdd
    # Entrada: No hay
    # Salida: No hay
    def crear_tabla_base_stats(self) -> None:
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
    
    #####################################################################
    # Función: Crear tabla de tipos pokemon en bbdd
    # Entrada: No hay
    # Salida: No hay
    def crear_tabla_types(self) -> None:
        sql_string = """create table if not exists type(
            id_type integer not null,
            type varchar(10) not null,
            constraint pk_type primary key (id_type),
            constraint unique_type_name unique (type)
        )"""
        self.conectar()
        self.__conexion.execute(sql_string)
        self.cerrar()
    
    #####################################################################
    # Función: Crear tabla de relación pokemon y tipo en bbdd
    # Entrada: No hay
    # Salida: No hay
    def crear_tabla_relacion_pokemon_types(self) -> None:
        sql_string = """create table if not exists pokemon_type(
            id_pokemon integer not null,
            id_type integer not null,
            constraint fk_pokemon_pokemon_type foreign key (id_pokemon) references pokemon (id_pokemon),
            constraint fk_type_pokemon_type foreign key (id_type) references type (id_type)
        )"""
        self.conectar()
        self.__conexion.execute(sql_string)
        self.cerrar()
    
    #####################################################################
    # Función: Crear tabla de naturalezas pokemon en bbdd
    # Entrada: No hay
    # Salida: No hay
    def crear_tabla_nature(self) -> None:
        sql_string = """create table if not exists nature(
            id_nature integer not null,
            nature varchar(20) not null,
            decreased_stat varchar(20),
            increased_stat varchar(20),
            constraint pk_nature primary key (id_nature),
            constraint unique_nature unique (nature)
        )"""
        self.conectar()
        self.__conexion.execute(sql_string)
        self.cerrar()
    
    #####################################################################
    # Función: Crear tabla de entrenador en bbdd
    # Entrada: No hay
    # Salida: No hay 
    def crear_tabla_trainer(self) -> None:
        sql_string = """create table if not exists trainer(
            id_trainer integer not null,
            name varchar(20) not null,
            gender char(1) not null,
            constraint pk_trainer primary key (id_trainer),
            constraint unique_trainer_name unique (name)
        )"""
        self.conectar()
        self.__conexion.execute(sql_string)
        self.cerrar()
    
    #####################################################################
    # Función: Crear tabla de equipos en bbdd
    # Entrada: No hay
    # Salida: No hay
    def crear_tabla_team(self) -> None:
        sql_string = """create table if not exists team(
            id_team integer not null,
            id_trainer integer not null,
            team_name varchar(30) not null,
            constraint pk_team primary key (id_team),
            constraint fk_trainer_team foreign key (id_trainer) references trainer (id_trainer),
            constraint unique_team unique (id_trainer, team_name)
        )"""
        self.conectar()
        self.__conexion.execute(sql_string)
        self.cerrar()
    
    #####################################################################
    # Función: Crear tabla de relación equipo-pokemon en bbdd
    # Entrada: No hay
    # Salida: No hay
    def crear_tabla_pokemon_team(self) -> None:
        sql_string = """create table if not exists pokemon_team(
            id_pokemon integer not null,
            id_team integer not null,
            id_nature integer not null,
            pokemon_name varchar(30) not null,
            constraint fk_pokemon_team_pokemon foreign key (id_pokemon) references pokemon (id_pokemon),
            constraint fk_pokemon_team_team foreign key (id_team) references team (id_team),
            constraint fk_pokemon_team_nature foreign key (id_nature) references nature (id_nature)
        )"""
        self.conectar()
        self.__conexion.execute(sql_string)
        self.cerrar()

# print('Pruebas de creación')
# obj_conexion = Conexion()
# obj_conexion.crear_tablas()
# obj_conexion.cargar("trainer", [(None, 'maria', 'f')])
# obj_conexion.cargar("trainer", [(None, 'Gato', 'm'), (None, 'pepe', 'm')])
# obj_conexion.cargar("pokemon", [(None, 'charmander'), (None, 'squirtle')])
# print('Fin prueba')