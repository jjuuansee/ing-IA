import funcion1


valido = True
seguir_leyendo = True

while seguir_leyendo:
    valor_de_usuario = input("Ingrese un dígito hexadecimal o 'Fin' para terminar: ")
    if valor_de_usuario.lower() == "fin":
        seguir_leyendo = False
    elif funcion1.hexchartodec(valor_de_usuario) == -1:
        valido = False
if valido:
    print("Correcto")
else:
    print("Incorrecto")
