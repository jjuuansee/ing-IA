import csv

mayores = []
with open('estudiante.csv', mode='r', encoding='utf-8') as archivo:
    contenido = list(csv.reader(archivo, delimiter=','))
    for fila in contenido:
        if fila[1] >= '15':
            mayores.append(fila)

with open('mayores_15.csv', mode='w', encoding='utf-8') as archivo:
    writer = csv.writer(archivo, delimiter=',')
    for fila in mayores:
        writer.writerow(fila)
