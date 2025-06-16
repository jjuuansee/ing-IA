print("INDICE DE MASA CORPORAL")
print("=======================")


def masa_corporal(peso,altura):
    imc = round(peso / altura ** 2.2)
    return imc


peso_ej = float(input("Ingrese su peso en kg: "))
altura_ej = float(input("Ingrese su altura en metros: "))
imc = masa_corporal(peso_ej,altura_ej)
print(f"Tu indice de masa corporal es: {imc}")
