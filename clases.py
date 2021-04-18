class Pokemon:
    
    def __init__(self, numero_pokedex_nacional:int, name:str, types:list, attacks:list, stats:dict):
        self.__name = name
        self.__types = types
        self.__attacks = attacks
        self.__stats = stats
        self.__numero_pokedex_nacional = numero_pokedex_nacional

    def get_numero_pokedex_nacional(self):
        return self.__numero_pokedex_nacional

    def get_name(self):
        return self.__name

    def get_types(self):
        if len(self.__types) == 1:
            return self.__types[0]
        else:
            return f"{self.__types[0]} - {self.__types[1]}"
    
    def get_info(self):
        data = f"{self.get_numero_pokedex_nacional()} - {self.get_name()}"
        data += f"\n{self.get_types()}"
        return data
    
    def get_attacks(self):
        data = ""
        for i, attack in enumerate(self.__attacks):
            data += f"{i+1} - {attack}"
            if i < len(self.__attacks) - 1:
                data += "\n"
        return data

    def get_stats(self):
        data = ""
        for i, key in enumerate(self.__stats):
            data += f"{key}: {self.__stats[key]}"
            if i < len(self.__stats) - 1:
                data += "\n"
        return data