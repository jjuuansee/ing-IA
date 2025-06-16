print("TRADUCTOR\n=========")

delimitador = " "


def enlistar_frase(frase):
    frase_minusc = frase.lower()
    frase_enlistada = frase_minusc.split(delimitador)
    return frase_enlistada


def traductor(lista_esp, lista_ing, frase):
    frase_enlistada = enlistar_frase(frase)
    lista_traducida = []
    if len(lista_esp) != len(lista_ing):
        return "Nos haz ingresado la misma cantidad de traducciones"
    else:
        for palabra in frase_enlistada:
            i = lista_esp.index(palabra)
            palabra_traducida = lista_ing[i]
            lista_traducida.append(palabra_traducida)
            cadena_traducida = delimitador.join(lista_traducida)
    return cadena_traducida


list_esp = ["es","hoy","viernes"]
list_ing = ["is","today","friday"]
frase = 'Hoy es viernes'
print(traductor(list_esp, list_ing, frase))