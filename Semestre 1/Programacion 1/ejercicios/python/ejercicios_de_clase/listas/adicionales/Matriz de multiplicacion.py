def matriz_multiplicacion(matriz1, matriz2):
    if len(matriz1) == len(matriz2[0]):  # El numero de filas de la matriz 1 tiene que ser igual al
        #                                  numero de columnas de la matriz 2
        matriz_result = []
        for i in range(len(matriz1)):  # Por cada fila de la matriz 1
            matriz_result.append([])   # agregar una lista vacia al resultado
            for j in range(len(matriz2[0])):  # Por cada columna de la matriz 2
                matriz_result[i].append(0)    # agregar 0 a la matriz resultante
#                                                      [[0, 0], [0, 0]]

        for fila in range(len(matriz1)):  # Solo se va a iterar el numero de filas que halla en la matriz 1
            for columna in range(len(matriz2[0])):
                for elemento in range(len(matriz1[0])):
                    matriz_result[fila][columna] += matriz1[fila][elemento] * matriz2[elemento][columna]  # A cada elemento de la matriz resultante
                                                                                    # se le asigna el resultado de la multipicacion
                                                                                    # de las dos matrices
        return matriz_result




matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8], [9, 10], [11, 12]]
multiplicacion = matriz_multiplicacion(matriz1, matriz2)
for fila in multiplicacion:
    print(fila)