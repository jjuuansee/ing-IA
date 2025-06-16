print("TOTAL DE SEGUNDOS Y DIFERENCIA DE SEGUNDOS")
print("==========================================")


def total_de_segundos(horas,minutos,segundos):
    tiempo_total = horas * (60 ** 2) + minutos * 60 + segundos
    return tiempo_total


horas1 = int(input("Ingrese el numero de horas: "))
minutos1 = int(input("Ingrese el numero de minutos: "))
segundos1 = int(input("Ingrese el numero de segundos: "))
tiempo_total1 = total_de_segundos(horas1,minutos1,segundos1)
horas2 = int(input("Ingrese el numero de la segunda hora: "))
minutos2 = int(input("Ingrese el numero de los segundos minutos: "))
segundos2 = int(input("Ingrese el numero de la tercer hora: "))
tiempo_total2 = total_de_segundos(horas2,minutos2,segundos2)
diferencia = horas2 - horas1
if diferencia > 0:
    print(f"La diferencia de segundos es de: {diferencia}")
else:
    print(f"La diferencia de segundos es de: {diferencia * -1} segundo")