def normalizar(cadena):
    alfabeto_con_espacio = "abcdefghijklmnopqrstuvwxyz "  #Esta variable llama al alfabeto para luego con las siguientes funciones poder trabajar letra por letra del mismo.
    cadena = cadena.lower()  #Transforma los caracteres de la cadena (que posiblemente estén en mayúscula) a minúscula
    for letra in cadena:  #Se evalúa cada caracter de la cadena ingresada (cada caracter está asginado a la variable "letra")
        if letra == "á" or letra == "ä" or letra == "â" or letra == "à":  #Todos los caracteres especiales los reemplaza por la vocal correspondiente.
            cadena = cadena.replace(letra, "a")
        elif letra == "é" or letra == "ê" or letra == "è" or letra == "ë":
            cadena = cadena.replace(letra, "e")
        elif letra == "í" or letra == "î" or letra == "ì" or letra == "ï":
            cadena = cadena.replace(letra, "i")
        elif letra == "ó" or letra == "ô" or letra == "ò" or letra == "ö":
            cadena = cadena.replace(letra, "o")
        elif letra == "ú" or letra == "û" or letra == "ù" or letra == "ü":
            cadena = cadena.replace(letra, "u")
    for letra in cadena:  #Primero evalúa cada elemento de la cadena para luego
        if letra not in alfabeto_con_espacio: # analizar dicho ítem en el abecedario
            cadena = cadena.replace(letra, "")  #Transforma ese caracter NO encontrado en el abecedario por un espacio vacío.
    return cadena  #Devuelve la cadena transformada

def cifrar(cadena):
    cadena = normalizar(cadena)  #Se llama a la función anterior
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    paso = int(input("Indique el paso con el cual se cifra la cadena: ")) # Se le pide al usuario que ingrese cuánto quiere avanzar para cifrar la frase ingresada
    nueva_frase = ""  #Esta variable comienza vacía, ya que luego se le irán asignando más valores mediante las iteraciones
    for letra in cadena:  #Primero le asigna a la variable "letra" un caracter de la cadena y lo va analizando. Hace iteraciones con este paso
        if letra in alfabeto:
            indletra = alfabeto.find(letra)  #Busca el índice de la letra en el abecedario
            indnuevo = indletra + paso # El índice nuevo es el resultado de avanzar tantas veces como indique el usuario.
            if indnuevo >= 26: # Si el índice nuevo es mayor a la cantidad de caracteres que tiene "alfabeto", este lo regresa al inicio.
                indnuevo -= 26
            nueva_frase += alfabeto[indnuevo]  #La nueva letra será el caracter ubicado en la posición que marca el nuevo índice calculado
        else:
            nueva_frase += letra # Esto es para los caracteres no pertenecientes al abecedario.
    return (nueva_frase) # La función retorna la cadena cifrada mediante esta variable.

def decifrar(cadena):
    cadena = normalizar(cadena)  #Se hace un llamado a la primera función realizada.
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    paso = int(input("Indique el paso con el cual se decifra la cadena: "))
    nueva_frase = ""  #Se realiza el mismo procedimiento que con la función anterior
    for letra in cadena:
        if letra in alfabeto:  #Primero le asigna a la variable "letra" un caracter de la cadena y lo va analizando. Hace iteraciones con este paso
            indletra = alfabeto.find(letra)  #Busca el índice de la letra en el abecedario
            indnuevo = (indletra - paso) % 26  #Calculamos el nuevo índice, asegurándonos de que esté dentro de nuestro alfabeto
            nueva_frase += alfabeto[indnuevo]  #La nueva letra será el caracter ubicado en la posición que marca el nuevo índice calculado
        else:
            nueva_frase += letra
    return nueva_frase #La función retorna la nueva frase, que antes empezó vacía, pero ahora tiene la cadena de caracteres nuevos.