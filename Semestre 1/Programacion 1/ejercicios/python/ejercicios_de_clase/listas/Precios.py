print("MINIMO Y MAXIMO EN UNA LISTA DE PRECIOS")
print("=======================================")

def obtener_minimo_maximo_de_precios(num_precios):
    if num_precios <= 0:
        print("Debe ingresar al menos un precio.")
    else:
        precios = []
        for i in range(num_precios):
            precio = float(input("Ingrese un precio: "))
            precios.append(precio)
        if not precios:
            print("La lista de precios está vacía.")
        else:
            minimo = min(precios)
            maximo = max(precios)
            return print(f"El precio maximo de la lista es: {maximo} y el precio minimo: {minimo}")


num_precios = int(input("Ingrese la cantidad de precios que tienes en la lista: "))
obtener_minimo_maximo_de_precios(num_precios)