diccionario = {
    "Euro": "€",
    "Dolar": "U$D",
    "Yen": "¥",
    "Peso": "$",
    "Real": "R$"
}
accion = input("Ingrese la divisa que quiere saber su simbolo: ")
if accion in diccionario.keys():
    print(diccionario[accion])
else:
    print("Esa divisa no se encuentra en el diccionario")
