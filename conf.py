# Función para definir los stats de un pokemons
def base_stats(hp:int, attack:int, defense:int, sa:int, sd:int, speed:int) -> dict:
    return {
        'hp': hp,
        'attack': attack,
        'defense': defense,
        'special attack': sa,
        'special defense': sd,
        'speed': speed
    }
