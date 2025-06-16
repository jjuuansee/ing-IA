print("CANTIDAD DE NUMEROS QUE SALIERON AL TIRAR UN DADO")
print("=================================================")
import random
def tirada_dados():
    return random.randint(1,6)
num_tiradas = 30
contador_de_1 = 0
contador_de_2 = 0
contador_de_3 = 0
contador_de_4 = 0
contador_de_5 = 0
contador_de_6 = 0
for i in range(num_tiradas):
    dado = tirada_dados()
    if dado == 1:
        contador_de_1 += 1
    elif dado == 2:
        contador_de_2 += 1
    elif dado == 3:
        contador_de_3 += 1
    elif dado == 4:
        contador_de_4 += 1
    elif dado == 5:
        contador_de_5 += 1
    else:
        contador_de_6 += 1
print(f"La cantidad de caras 1, salio {contador_de_1} veces")
print(f"La cantidad de caras 2, salio {contador_de_2} veces")
print(f"La cantidad de caras 3, salio {contador_de_3} veces")
print(f"La cantidad de caras 4, salio {contador_de_4} veces")
print(f"La cantidad de caras 5, salio {contador_de_5} veces")
print(f"La cantidad de caras 6, salio {contador_de_6} veces")
