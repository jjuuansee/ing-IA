print("ALGORIMO PARA SABER SI UN NUMERO ESTA DENTRO DE OTROS DOS NUMEROS")
print("=================================================================")
n = int(input("Ingrese el numero que desea saber si esta entro otros dos numeros: "))
linf = int(input("Ingrese el numero inferior:"))
lsup = int(input("Ingrese el numero superior:"))
if linf <= n <= lsup:
    print("Verdadero")
else:
    print("Falso")
