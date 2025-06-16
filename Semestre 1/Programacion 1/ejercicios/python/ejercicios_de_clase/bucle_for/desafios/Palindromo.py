print("GEMATRIA")
print("========")


def normaliza_frase(frase):
    caracteres = "áéíóúü"
    normalizados = "aeiouu"
    cadena_nueva = ""
    for letra in frase.lower():
        i = caracteres.find(letra)
        if i >= 0:
            cadena_nueva += normalizados[i]
        else:
            cadena_nueva += letra
    return cadena_nueva


def palindromo(frase):
    frase_auxiliar = normaliza_frase(frase)
    frase_original = frase_auxiliar
    frase_invertida = frase_original[::-1]
    if frase_invertida != frase_original:
        return False
    return True


frase = input("Ingrese una frase: ")
print(palindromo(frase))