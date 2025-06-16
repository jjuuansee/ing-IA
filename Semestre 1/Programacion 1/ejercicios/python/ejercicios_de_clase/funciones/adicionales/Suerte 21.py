print("NUMERO DE LA SUERTE")
print("===================")

def ultimodigito(n):
    return n % 10

def sacarultimodigito(n):
    return n // 10

def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += ultimodigito(numero)
        numero = sacarultimodigito(numero)
    return suma


numero_ingresado = int(input("Ingresa un número entero positivo mayor que 0: "))
if numero_ingresado <= 0:
    print("El número debe ser mayor que 0.")
else:
    resultado = suma_digitos(numero_ingresado)
    print(f"El numero {numero_ingresado} es de la suerte: {True if resultado == 21 else False}")

