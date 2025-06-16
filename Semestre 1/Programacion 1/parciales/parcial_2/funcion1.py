def hexchartodec(val):
    val = val.upper()
    if len(val) > 1:
        return -1
    if '0' <= val <= '9':
        return int(val)
    elif 'A' <= val <= 'F':
        if val == 'A':
            return 10
        elif val == 'B':
            return 11
        elif val == 'C':
            return 12
        elif val == 'D':
            return 13
        elif val == 'E':
            return 14
        elif val == 'F':
            return 15
    return -1


"""
print(hexchartodec("4"))  # Imprime 4
print(hexchartodec("B"))  # Imprime 11
print(hexchartodec("0"))  # Imprime 0
print(hexchartodec("F"))  # Imprime 15
print(hexchartodec("Z"))  # Imprime -1
print(hexchartodec("14")) # Imprime -1
"""