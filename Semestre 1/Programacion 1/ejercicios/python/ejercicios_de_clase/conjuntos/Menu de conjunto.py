salir = False
conjunto = set()
while not salir:

    print("==========================================")
    print("    A: Agregar elemento al conjunto")
    print("    B: Borrar elemento del conjunto")
    print("T: Borrar todos los elementos del conjunto")
    print("          M: Mostrar conjunto")
    print("              F: Finalizar")
    print("==========================================")

    opcion = input("Ingrese una opcion: ")
    opcion = opcion.upper()

    if opcion == "A":
        elemento = input("Ingrese un elemento a ingresar: ")
        if elemento not in conjunto:
            conjunto.add(elemento)
        else:
            print("El elemento ya existe")

    elif opcion == "B":
        elemento = input("Ingrese un elemento a borrar: ")
        if elemento not in conjunto:
            print("El elemento a eliminar no existe")
        else:
            conjunto.discard(elemento)

    elif opcion == "T":
        conjunto.clear()
        print("Los elementos del conjunto han sido eliminados")

    elif opcion == "M":
        print(f"Tu conjunto es: {conjunto}")

    elif opcion == "F":
        salir = True
        print("Saliendo...")

    else:
        print("Opcion invalida")
