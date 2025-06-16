print("PROMEDIO DE LA SUMA DE LAS TIRADAS DE DOS DADOS")
print("===============================================")
import random
def tirada_dados():
    return random.randint(1,6)


num_tiradas = 20
suma_resultados = 0
for i in range(num_tiradas):
    dado1 = tirada_dados()
    print(dado1)
    dado2 = tirada_dados()
    print(dado2)
    suma_resultados = suma_resultados + dado1 + dado2
promedio = suma_resultados / num_tiradas*2
print(f"El promedio de tiradas de los dados es: {promedio}")
