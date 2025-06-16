print("VOTACIONES")
print("==========")
print("PARA VOTAR EL PARTIDO ROJO INGRESAR A")
print("PARA VOTAR EL PARTIDO VERDE INGRESAR B")
print("PARA VOTAR EL PARTIDO AZUL INGRESAR C")
print("======================================")
voto = str(input("Ingrese su voto:"))
voto = voto.upper()
if voto == "A":
    print("Usted a votado por el partido rojo")
elif voto == "B":
    print("Usted a votado por el partido verde")
elif voto == "C":
    print("Usted a votado por el partido azul")
else:
    print("Opcion erronea")
    