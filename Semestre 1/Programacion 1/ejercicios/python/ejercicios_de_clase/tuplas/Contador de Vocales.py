def count_vocales(cadena):
    vocal_a, vocal_e, vocal_i, vocal_o, vocal_u = 0, 0, 0, 0, 0
    for letra in cadena:
        if letra == "a" or letra == "A":
            vocal_a += 1
        elif letra == "e" or letra == "E":
            vocal_e += 1
        elif letra == "i" or letra == "I":
            vocal_i += 1
        elif letra == "o" or letra == "O":
            vocal_o += 1
        elif letra == "u" or letra == "U":
            vocal_u += 1
    return (vocal_a, vocal_e, vocal_i, vocal_o, vocal_u)


print(count_vocales("aeiOUaaaaaeeeeeeeeeeeeeeeeiooouuuuuuuuuuuuu"))
