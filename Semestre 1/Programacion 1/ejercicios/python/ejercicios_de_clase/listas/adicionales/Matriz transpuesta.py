def transpuesta_matriz(matriz):
    # Crear una matriz de ceros con el tamaño transpuesto
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []

    for i in range(columnas):
        nueva_fila = []
        for j in range(filas):
            nueva_fila.append(A[j][i])
        resultado.append(nueva_fila)
    return resultado


# Ejemplo
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Transposición de una matriz:")
transpuesta = transpuesta_matriz(A)
for fila in transpuesta:
    print(fila)
