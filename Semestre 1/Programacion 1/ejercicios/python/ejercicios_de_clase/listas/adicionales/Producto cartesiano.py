def producto_cartesiano(lista1, lista2):
    lista_producto = []
    for elemento in lista1:
        for item in lista2:
            lista_producto .append([elemento, item])
    return lista_producto


print(producto_cartesiano([1, 2, 3], ["rojo", "verde"]))
print(producto_cartesiano([1, 2, 3, 4], ['a', 'b', 'c', 'd', 'e', 'f']))
