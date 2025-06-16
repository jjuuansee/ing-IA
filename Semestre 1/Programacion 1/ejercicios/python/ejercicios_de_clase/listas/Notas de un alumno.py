print("NOTAS DE UN ALUMNO")
print("==================")

promedio = 0
lista_de_notas = []
for i in range(5):
    nota = float(input("Ingrese una Nota: "))
lista_de_notas.append(nota)
print(lista_de_notas)
for i in lista_de_notas:
    promedio += i
print(f"La nota promedio: {promedio/5}")
if promedio > 40:
    print('Sos una bestia, seras la proxima Valentina Crossa')
elif promedio == 5:
    print('AJDSJADSJ son un desastre')
else:
    print(f"La nota maxima fue de: {max(lista_de_notas)}")
    print(f"La nota minima fue de: {min(lista_de_notas)}")
