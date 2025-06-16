creditos = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5,
    'Contabilidad': 8,
    'Programación': 6,
    'Redacción': 6,
    'Trabajo final': 6
}
total_creditos = 0
for materia, credito in creditos.items():
    print(f'{materia} tiene: {credito} creditos')
    total_creditos += credito
print(f"El total de creditos es de: {total_creditos}")
