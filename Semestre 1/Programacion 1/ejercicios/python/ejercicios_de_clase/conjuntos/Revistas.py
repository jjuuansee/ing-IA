print('ENCUESTA SOBRE REVIISTAS\n========================')

a = {"juan", "pepe", "maria", "jose", "esteban", "lucia"}

b = {"juan", "pepe", "marta", "lucia", "john"}

c = {"lucia", "john", "maria", "esteban", "margarita"}
total = 10

caso_a = (a & b - ( a & b & c)) | (a & c - (a & b & c)) | (b & c - (a & b & c))
print(f"Las personas que leen solo 2 revistas son: {caso_a}")
print("cant: ", len(caso_a))

caso_b = (a | b | c)
og = total-len(caso_b)
print(f"Quienes no leen ninguna revista son: {og}")

lectores_a = a - (b | c)
lectores_b = b - (a | c)
lectores_c = c - (a | b)
caso_c = lectores_a | lectores_b | lectores_c
print(f"Las personas que solo leen una revista son: {caso_c}")
print("cant: ", len(caso_c))

caso_d = (a & b & c)
print(f"Quienes leen las 3 revistas son: {caso_d}")
print("cant: ", len(caso_d))
