from clases import Pokemon

pokemon1 = Pokemon('Pikachu', ['electrico'], ['placaje', 'gruñido'], {'iv':20, 'def':15})
print(pokemon1.get_info())
print("ATACKS")
print(pokemon1.get_attacks())
print("STATS")
print(pokemon1.get_stats())