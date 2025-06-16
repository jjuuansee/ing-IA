print("DIBUJA UNA FORMA")
print("================")

def dibuja_forma(ancho,altura):
    if altura < 1:
        print("La altura ingresada no es correcta")
    elif altura == 1:
        print("x" * ancho)
    else:
        contador = altura
        print("x" * ancho)
        while contador > 2:
            print("x" + " " * (ancho - 2) + "x")
            contador -= 1
        print("x" * ancho)


altura1 = int(input("Ingrese la altura de la figura dibujar:"))
ancho1 = int(input("Ingrese el ancho de la figura que quiere dibujar:"))
dibuja_forma(ancho1, altura1)
