import pandas

from src.battle_class import*
from src.string_transform import*

SheetHeaders = ["Infos","Pokemon","Pokemon (FR)","Lv","IVs","Ability","Nature",
                "Held Item","Move 1","Move 2","Move 3","Move 4"]
BattleModes = ["SingleBattle", "DoubleBattle", "TripleBattle", "RotationBattle"]

def open_xlsx(filepath:str)->list[PokemonBattle]:
    Trainers_sheet = pandas.read_excel(filepath,sheet_name="Trainers",header=0)
    BossBattles_sheet = pandas.read_excel(filepath,sheet_name="BossBattles",header=0)
    Sheets = [Trainers_sheet, BossBattles_sheet]

    # Extracting data from each sheet and storing it in a list of lists (AllTrainers)
    AllTrainers = []
    for sheet in Sheets:
        n = len(sheet["Pokemon"])
        data = [[] for i in range(n)]
        for row in range(n):
            for column_name in SheetHeaders:
                if str(sheet[column_name][row]) != "nan" and str(sheet[column_name][row]) not in BattleModes:
                    data[row].append(sheet[column_name][row])
        for row in data:
            if row == []:
                data.remove([])
        for i in range(6):
            data.pop(0)
        AllTrainers.append(data)

    # Remove empty lists
    for i in AllTrainers:
        if i == []:
            AllTrainers.remove(i)
        else:
            if [] in i:
                i.remove([])
            for j in i:
                if [] in j:
                    j.remove([])

    # Building the result list (a list of 'PokemonBattle' entities)
    Result = []
    CurrentLocation = ""
    CurrentTrainer = ""
    CurrentBattleType = BattleMode(0)
    Pokemons = []
    FirstTrainerEncountered = False
    for i in AllTrainers:
        for j in i:
            print(j)
            if j[0] == "Location:":
                CurrentLocation = j[1]
            elif len(j) == 1:
                CurrentTrainer = j[0]
                if not FirstTrainerEncountered:
                    FirstTrainerEncountered = True
                else:
                    Result.append(PokemonBattle(CurrentTrainer, CurrentLocation, CurrentBattleType, Pokemons))
                    Pokemons = []
            else:
                if len(j) == 12:
                    if j[0] == "Double Battle":
                        CurrentBattleType = BattleMode(1)
                    elif j[0] == "Triple Battle":
                        CurrentBattleType = BattleMode(2)
                    else:   # Rotation Battle
                        CurrentBattleType = BattleMode(3)
                    j.pop(0)
                if len(j) == 11:
                    Pokemon = [j[0], int(j[2]), int(j[3]), j[4], formalize(j[5]), formalize(j[6]), j[7], j[8], j[9], j[10]]
                else:
                    Pokemon = [j[0], int(j[2]), int(j[3]), j[4], formalize(j[5]), formalize(j[6]), j[7], j[8], j[9], ""]
                Pokemons.append(Pokemon)
    return Result
