print("REMPLAZAR LOS ESPACIOS DE UNA FRASE CON PUNTO Y COMA")
print("====================================================")

frase = input("Ingrese la frase: ")
nueva_frase = ""
for letra in frase:
    if letra == " ":
        nueva_frase += ";"
    else:
        nueva_frase += letra
print(nueva_frase)
