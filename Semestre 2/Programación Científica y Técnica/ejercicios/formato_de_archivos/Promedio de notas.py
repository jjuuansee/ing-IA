import csv

with (open('Notas.csv', mode='r', encoding='utf-8') as notas):
    notas_alumnos = csv.reader(notas)
    encabezado = next(notas_alumnos)
    promedio = 0
    cantidad_alumnos = 0
    for nota in notas_alumnos:
        promedio += int(nota[1])
        cantidad_alumnos += 1
    promedio = promedio / cantidad_alumnos
    print(f'El promedio de la clase es: {promedio}')
