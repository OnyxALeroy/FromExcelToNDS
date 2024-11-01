import src.main

if __name__ == '__main__':
    print("The input Excel file must follow the organization of the example file (see in the 'example_excel' folder).")
    print("Note: the first row of your input file must contains your headers.")
    print("Remember to previously open your rom with DSPRE, so that your /nds/ contains a folder of the same name as your rom.")
    src.main.FromExcelToNDS()