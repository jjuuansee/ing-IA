print("AÑO BISIESTO")
print("^^^^^^^^^^^^")
año = int(input("Ingrese el año:"))
if año < 0:
    print("Ingrese un año válido")
elif año % 4 == 0:
    print("El año es bisiesto")
elif año % 4 == 0 and año % 100 == 0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
