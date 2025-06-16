print("FUNCION DE HAILSTONE")
print("====================")


def hailstone(n):
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        print(int(n))
    return "FIN"


n = int(input("Ingrese un numero entero: "))
print(hailstone(n))
