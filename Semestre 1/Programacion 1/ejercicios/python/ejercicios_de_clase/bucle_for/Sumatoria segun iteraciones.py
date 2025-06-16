print("SUMATORIA DE ITERACIONES")
print("========================")

sumatoria = 0
cantidad_de_iteraciones = int(input("Ingrese el numero iteraciones que desea tener: "))
for i in range(cantidad_de_iteraciones):
    num = int(input("Ingrese un numero entero:"))
    sumatoria += num
print(f"La sumatoria es: {sumatoria}")
