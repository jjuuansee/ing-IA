A = {i**2 for i in range(1, 1000)}
B = {i**3 for i in range(1, 1000)}

caso_a = A & B
print(caso_a)
print(len(caso_a))
check = {576, 676, 784, 529, 625, 729, 7744, 7569}
es_cuadrado = True
for elemento in check:
    if elemento not in A:
        es_cuadrado = False
        break
print(es_cuadrado)
