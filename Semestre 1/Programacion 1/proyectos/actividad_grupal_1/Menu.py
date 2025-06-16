import Funciones  # Se hace un llamado al documento donde realizamos las funciones que aparecen en el menú.
frenar = False  # El menú está dentro de un bucle, el cual frenará cuando esta variable sea True
while not frenar:  # Es lo mismo que decir, while frenar == False
    print("ALGORITMO PARA CIFRAR Y DESCIFRAR UNA FRASE")        # Menú de opciones para el usuario
    print("===========================================")
    print("")
    print("Para CIFRAR una frase INGRESE 1")
    print("Para DESCIFRAR una frase INGRESE 2")
    print("Para SALIR INGRESE 0")
    print("")
    print("(Debes conocer el paso de cifrado y descifrado)")
    print("===============================================")

    num = int(input("Ingrese el numero de la opcion que quiere realizar: "))  #Aquí se decidirá cómo se ejecutara dicho menú, acorde al número que elija
    if num == 1:                                                              #El significado de cada número fue explicado anteriormente.
        frase = input("Ingrese la frase que quiere cifrar: ") #La opción hace llamado a la función cifrar y usa la variable "frase" como el argumento de dicha función
        nueva_frase = Funciones.cifrar(frase)
        print(f"Su frase cifrada es: {nueva_frase}")
    elif num == 2:
        frase = input("Ingrese la frase que quiere descifrar: ")  #La opción 2 hace llamado a la función decifrar y usa la variable "frase" como el argumento de dicha función
        nueva_frase = Funciones.decifrar(frase)
        print(f"La frase descifrada es: {nueva_frase}")
    elif num == 0:
        print("¡Gracias por utilizar el programa!")  #La opción 0 logra la salida del menú, finalizando con el programa.
        frenar = True
    else:
        print("El numero ingresado no es valido")  #Le informa al usuario que elijió una opción inválida, y le da otra oportunidad para que elija bien.
    print("")
