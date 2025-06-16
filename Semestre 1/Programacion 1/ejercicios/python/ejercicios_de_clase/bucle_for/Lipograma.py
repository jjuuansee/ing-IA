print("LIPOGRAMA")
print("=========")


def es_lipograma(cadena):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    letras_unicas = ""
    for letra in cadena.lower():
        if letra in abecedario and letra not in letras_unicas:
            letras_unicas += letra
    return len(letras_unicas) == len(abecedario) - 1


frase = input("Escribe la frase que desea saber si es pangrama: ")
print(es_lipograma(frase))
