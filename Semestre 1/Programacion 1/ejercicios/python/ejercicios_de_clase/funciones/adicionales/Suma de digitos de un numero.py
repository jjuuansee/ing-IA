print("SUMA DE LOS DIGITOS DE UN NUMERO")
print("================================")

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
    print(f"La suma de los dígitos de {numero_ingresado} es: {resultado}")
