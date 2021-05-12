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
    # Si hay

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
    def cargar(self, tabla:str, data:list, columns:int, relacion:bool=False) -> None:
        self.conectar()
        cursor = self.__conexion.cursor()
        incognitas = "?" * columns
        while '??' in incognitas:
            incognitas = incognitas.replace('??', '?,?')
        if relacion:
            cursor.executemany(f"insert into {tabla} values ({incognitas})", data)
        else:   
            cursor.executemany(f"insert into {tabla} values (null, {incognitas})", data)
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
    # Función: Consultar información de una tabla
    # Entrada: Nombre de la tabla a consultar
    # Salida: toda la información de una tabla
    def consultar_tabla(self, tabla:str) -> list:
        sql_string = f"select * from {tabla}"
        self.conectar()
        cursor = self.__conexion.cursor()
        cursor.execute(sql_string)
        data = cursor.fetchall()
        cursor.close()
        self.cerrar()
        return data

    #####################################################################
    # Función: Consultar información de una tabla
    # Entrada: Nombre de la tabla a consultar
    # Salida: toda la información de una tabla
    def consultar_tabla_porsonalizada(self, sql_string:str) -> list:
        self.conectar()
        cursor = self.__conexion.cursor()
        cursor.execute(sql_string)
        data = cursor.fetchall()
        cursor.close()
        self.cerrar()
        return data
    
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

obj_conexion = Conexion()

if __name__ == '__main__':
    # Funciones para consultar la API
    from consultas_api import *

    obj_conexion.crear_tablas()



    TYPES = get_pokemon_types()
    types2 = list()
    for tipo in TYPES['types']:
        types2.append((tipo,))
    obj_conexion.cargar('type', types2, 1)



    POKEMONS = get_pokemon_list()
    pokemons2 = list()
    for pokemon in POKEMONS:
        pokemons2.append((pokemon,))
    obj_conexion.cargar('pokemon', pokemons2, 1)



    data = obj_conexion.consultar_tabla('pokemon')
    print(data)
    data = obj_conexion.consultar_tabla('type')
    print(data)



    data = obj_conexion.consultar_tabla('pokemon')
    pokemons = list()
    for pokemon in data:
        pokemons.append(pokemon[1])

    data = get_pokemon_data(pokemons)
    for pokemon_data in data['pokemons']:
        insert_data = list()
        aux = data['pokemons'][pokemon_data]
        name = aux['name']
        print(name)
        id_pokemon = obj_conexion.consultar_tabla_porsonalizada(f"select id_pokemon from pokemon where name = '{name}'")
        insert_data.append(id_pokemon[0][0])
        insert_data.append(aux['base_experience'])
        insert_data.append(aux['stats']['hp'])
        insert_data.append(aux['stats']['attack'])
        insert_data.append(aux['stats']['defense'])
        insert_data.append(aux['stats']['special-attack'])
        insert_data.append(aux['stats']['special-defense'])
        insert_data.append(aux['stats']['speed'])
        obj_conexion.cargar('base_stats', [tuple(insert_data)], len(insert_data))



    data = obj_conexion.consultar_tabla('pokemon')
    pokemons = list()
    for pokemon in data:
        pokemons.append(pokemon[1])

    data = get_pokemon_data(pokemons)
    insert_data = list()
    for pokemon_data in data['pokemons']:
        aux = data['pokemons'][pokemon_data]
        name = aux['name']
        print(name)
        id_pokemon = obj_conexion.consultar_tabla_porsonalizada(f"select id_pokemon from pokemon where name = '{name}'")[0][0]
        types = aux['types']
        for pokemon_type in types:
            id_type = obj_conexion.consultar_tabla_porsonalizada(f"select id_type from type where type = '{pokemon_type}'")
            id_type = id_type[0][0]
            insert_data.append((id_pokemon, id_type))

    obj_conexion.cargar('pokemon_type', insert_data, 2, True)



    data = get_nature_data(get_pokemon_natures())
    insert_data = list()

    for nature in data['natures']:
        decreased_stat = data['natures'][nature]['decreased_stat']
        increased_stat = data['natures'][nature]['increased_stat']
        try:
            decreased_stat = decreased_stat.replace('-', '_')
            increased_stat = increased_stat.replace('-', '_')
        except:
            pass
        insert_data.append((nature, decreased_stat, increased_stat))

    obj_conexion.cargar('nature', insert_data, 3)




