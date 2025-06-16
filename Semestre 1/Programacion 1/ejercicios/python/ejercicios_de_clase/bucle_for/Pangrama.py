print("PANGRAMA")
print("========")

def normaliza_cadena(cadena):
    caracteres = "áéíóúü"
    normalizados = "aeiouu"
    cadena_nueva = ""
    for letra in cadena.lower():
        i = caracteres.find(letra)
        if i >= 0:
            cadena_nueva += normalizados[i]
        else:
            cadena_nueva += letra
    return cadena_nueva


def es_pangrama(cadena):
    abcdario = "abcdefghijklmnñopqrstuvwxyz"
    aux = normaliza_cadena(cadena)
    for letra in abcdario:
        if letra not in aux:
            return False
    return True


frase = input("Escribe la frase que desea saber si es pangrama: ")
print(es_pangrama(frase))

normailizado = input("Ingrese otra frase con muchas tildes y caracteres: ")
print(normaliza_cadena(normailizado))