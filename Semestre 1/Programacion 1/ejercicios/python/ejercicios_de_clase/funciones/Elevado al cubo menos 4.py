print("ELEVADO AL CUBO MENOS 4")
print("=======================")

def elevado_al_cubo_menos_4(n):
    resultado = (n ** 3)-4
    return resultado


n = int(input("Ingrese un numero entero:"))
print(elevado_al_cubo_menos_4(n))