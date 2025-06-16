import csv
with open('estudiante.csv', mode='r', encoding='utf-8') as archivo:
    contenido = list(csv.reader(archivo))
    encabezados = contenido[0]
    for fila in contenido[1:]:
        resultado = f"{encabezados[0]}: {fila[0]} | {encabezados[1]}: {fila[1]} | {encabezados[2]}: {fila[2]}"
        print(resultado)
