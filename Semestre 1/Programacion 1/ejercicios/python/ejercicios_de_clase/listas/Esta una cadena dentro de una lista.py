print("ESTA LA CADENA DENTRO DE UNA LISTA")
print("")
print("Ingrese un numero entero cualquiera para dejar de ingresar caracteres")
print("=====================================================================")


def cadena_in_lista(lista_de_caracteres, cadena):
    if cadena in lista_de_caracteres:  #Verificar si la cadena está en la lista
        return True
    else:
        return False


frenar = False
lista_de_caracteres = []
while not frenar:
    caracter = input("Ingrese un caracter, palabra o frase para agregar a la lista: ")
    caracter = caracter.lower()
    if caracter == "salir":
        frenar = True
    else:
        lista_de_caracteres.append(caracter)
if not lista_de_caracteres:
    print("La lista esta vacia")


cadena = input("Ingrese el caracter que desea saber si esta dentro de la lista: ")
cadena = cadena.lower()
print(cadena_in_lista(lista_de_caracteres, cadena))
