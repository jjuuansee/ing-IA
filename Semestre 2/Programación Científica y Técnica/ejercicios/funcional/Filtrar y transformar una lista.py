from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = filter(lambda x: x%2==0, numeros)
numeros_por_3 = map(lambda x: x*3, numeros_pares)
suma = reduce(lambda x, y: x+y, numeros_por_3)
print(suma)