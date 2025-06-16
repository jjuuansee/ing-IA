print("PALABRAS MÁGICAS")
print("================")


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


def gematria(frase):
    valor = 0
    abcdario = "abcdefghijklmnñopqrstuvwxyz"
    frase_auxiliar = normaliza_frase(frase)
    for letra in frase_auxiliar:
        if letra in abcdario:
            posicion = abcdario.find(letra)
            valor += posicion + 1
    return valor

def palabra_magica(frase):
    frase_auxiliar = normaliza_frase(frase)
    gematria_frase = gematria(frase_auxiliar)
    if gematria_frase != 21:
        return False
    return True



frase = input("Ingrese una frase: ")
print(palabra_magica(frase))
