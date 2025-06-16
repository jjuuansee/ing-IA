print("ALGORITMO: SUMA DE NEGATIVOS Y PROMEDIO DE POSITIVOS")
print("====================================================")
sumatoria_negativos = 0
sumatoria_positivos = 0
contador_de_positivos = 0
for i in range(6):
    num = int(input("Ingrese un numero entero: "))
    if num < 0:
        sumatoria_negativos += num
    else:
        sumatoria_positivos += num
        contador_de_positivos += 1
print(f"La suma de los numeros negativos es: {sumatoria_negativos}")
if contador_de_positivos > 0:
    print("EL promedio de los numeros positivos es:", sumatoria_positivos / contador_de_positivos)
else:
    print("No se ingresaron numeros positivos")