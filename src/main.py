from src.open_xlsx import*
from src.nds_editing import*

# -------------------------------------------------------------------------------------------------

def FromExcelToNDS():
    input_filepath = "input/"
    nds_filepath = "nds/"
    # Select targets
    # FIXME: For tests only
    # input_filepath += str(input("Enter your input file: "))
    input_filepath += "trainers_db.xlsx"

    BattlesToImplement = open_xlsx(input_filepath)
    for battle in BattlesToImplement:
        battle.print()

    # FIXME: For tests only
    # nds_filepath_input = str(input("Enter your .nds file: "))
    nds_filepath_input = "Pokemon - Platinum Version (Europe).nds"
    edit_nds(nds_filepath, nds_filepath_input, BattlesToImplement)
    pass