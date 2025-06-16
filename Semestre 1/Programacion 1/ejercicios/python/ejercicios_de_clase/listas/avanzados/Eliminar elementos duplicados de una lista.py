print("ELIMINAR ELEMENTOS DUPLICADOS")
print("=============================")

def elementos_duplicados(lista_de_usuario):
    lista_sin_repetidos = []
    if not lista_de_usuario:
        return "No ingreso ningun elemento"
    else:
        for i in lista_de_usuario:
            if i not in lista_sin_repetidos:
                lista_sin_repetidos.append(i)
        return lista_sin_repetidos


seguir_leyendo = True
lista_de_usuario = []
print("INGRESE LOS ELEMENTOS DE LA LISTA\n\nPARA SALIR INGRESE 0\n====================")
while seguir_leyendo:
    item = int(input("Ingrese un elemento: "))
    if item == 0:
        seguir_leyendo = False
    else:
        lista_de_usuario.append(item)

print(elementos_duplicados(lista_de_usuario))
