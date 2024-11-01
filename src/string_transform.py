def formalize(item_name:str)->str:
    res = ""
    for char in item_name:
        if char == "(":
            break
        elif char != " " and char != "-":
            res += char.upper()
    return res
