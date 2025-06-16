es_negativo = False
conjunto = set()
while len(conjunto) < 5 and not es_negativo:
    n = int(input("Ingrese un numero: "))
    if n < 0:
        es_negativo = True
    else:
        if n in conjunto:
            print("El numero ingresado ya existe.")
        else:
            conjunto.add(n)
print(conjunto)
