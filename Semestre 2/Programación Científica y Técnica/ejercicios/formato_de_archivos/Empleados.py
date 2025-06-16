import json
mayores_50k = []
with open('Empleados.json', mode='r', encoding='utf-8') as archivo:
    datos_empleados = json.load(archivo)
    for empleado in datos_empleados:
        if empleado['salario'] >= 50000:
            mayores_50k.append(empleado)

with open('Empleados50k.json', mode='w', encoding='utf-8') as archivo:
    json.dump(mayores_50k, archivo, ensure_ascii=False, indent=4)

