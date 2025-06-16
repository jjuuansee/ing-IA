import funcion1


def hextodec(val):
    valor_decimal = 0
    for caracter in val:
        valor_del_caracter = funcion1.hexchartodec(caracter)
        if valor_del_caracter == -1:
            return -1
        valor_decimal = valor_decimal * 16 + valor_del_caracter
    return valor_decimal


print(hextodec("A1F"))  # Imprime 2591
print(hextodec("14"))  # Imprime 20
