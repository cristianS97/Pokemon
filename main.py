from clases import Pokemon
from conf import base_stats

pokemon1 = Pokemon(1, 'bulbasaur', ['grass', 'poisson'], ['tackle', 'vine whip'], base_stats(45, 49, 49, 65, 65, 45))
print(pokemon1.get_info())
print("ATACKS")
print(pokemon1.get_attacks())
print("STATS")
print(pokemon1.get_stats())

print("\n==================\n")

pokemon1 = Pokemon(4, 'charmander', ['fire'], ['growl', 'scratch'], base_stats(39, 52, 43, 60, 50, 65))
print(pokemon1.get_info())
print("ATACKS")
print(pokemon1.get_attacks())
print("STATS")
print(pokemon1.get_stats())

print("\n==================\n")

pokemon1 = Pokemon(7, 'squirtle', ['water'], ['growl', 'scratch'], base_stats(44, 48, 65, 50, 64, 43))
print(pokemon1.get_info())
print("ATACKS")
print(pokemon1.get_attacks())
print("STATS")
print(pokemon1.get_stats())