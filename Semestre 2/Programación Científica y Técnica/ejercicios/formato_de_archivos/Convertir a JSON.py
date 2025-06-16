import csv
import json

datos_csv = []
with open('estudiante.csv', mode='r', encoding='utf-8') as archivo:
    lector_csv = csv.DictReader(archivo)
    filas = list(lector_csv)
with open('estudiante_conv.json', mode='w', encoding='utf-8') as archivo:
    json.dump(filas, archivo, ensure_ascii=False, indent=4)
