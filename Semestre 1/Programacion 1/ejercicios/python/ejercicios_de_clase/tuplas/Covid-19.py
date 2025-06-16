seguir_leyendo = True
casos = []
suma = 0
while seguir_leyendo:
    valor = int(input('Ingrese el numero de infectados del dia: '))
    if valor == -1:
        seguir_leyendo = False
    else:
        suma += valor
        casos.append(valor)
total_casos = len(casos)
promedio_casos = suma / total_casos
max_casos = max(casos)
min_casos = min(casos)
print((total_casos, promedio_casos, max_casos, min_casos))
