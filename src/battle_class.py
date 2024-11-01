from enum import Enum

class BattleMode(Enum):
    SingleBattle = 0
    DoubleBattle = 1
    TripleBattle = 2
    RotationBattle = 3

class Pokemon:
    def __init__(self, name:str, level:int, iv:int, ability:str, nature:str, item:str, moves:list[str]):
        self.name = name
        self.level = level
        self.iv = iv
        self.ability = ability
        self.nature = nature
        self.item = item
        self.moves = moves
        pass

# Note: A Pokémon is represented as a list:
#       [English Name (str), Lvl (int), IV (int), Ability (str), Nature (str),
#            Item (str), Moves (list of str)]        
class PokemonBattle:
    def __init__(self, trainer_name:str, location:str, battle_mode:BattleMode, pokemons:list[list]):
        self.trainer_name = trainer_name
        self.location = location
        self.battle_mode = battle_mode
        self.pokemons = pokemons
        pass

    def print(self):
        print(f"Trainer Name: {self.trainer_name}")
        print(f"Location: {self.location}")
        for pokemon in self.pokemons:
            print(pokemon)
        print()
        pass