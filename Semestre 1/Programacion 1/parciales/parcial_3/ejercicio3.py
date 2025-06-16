print("REMPLAZAR LOS CARACTERES DE UNA CADENA")
print("======================================")


def reemplazar_en(cadena, a_reemplazar, por):
    if len(a_reemplazar) != len(por):
        return ""
    cadena_nueva = ""
    for letra in cadena:
        if letra in a_reemplazar:
            indice_letra = a_reemplazar.index(letra)
            cadena_nueva += por[indice_letra]
        else:
            cadena_nueva += letra
    return cadena_nueva


cadena = "hola"
a_reemplazar = "ha"
por = "H4"
print(reemplazar_en(cadena, a_reemplazar, por))  #Imprime Hol4

cadena = "hola"
a_reemplazar = "flo"
por = "Jy0"
print(reemplazar_en(cadena, a_reemplazar, por))  #Imprime h0ya

cadena = "me encanta programar"
a_reemplazar = "aeiou"
por = "@#$%?"
print(reemplazar_en(cadena, a_reemplazar, por))  #Imprime m# #nc@nt@ pr%gr@m@r

cadena = "Peñarol Campeon"
a_reemplazar = "ao"
por = "50"
print(reemplazar_en(cadena, a_reemplazar, por))  #Imprime Peñ5r0l C5mpe0n


