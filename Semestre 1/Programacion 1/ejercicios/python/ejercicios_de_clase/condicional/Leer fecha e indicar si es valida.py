print("INDICAR SI UNA FECHA ES VALIDA")
print("==============================")
dia = int(input("Ingrese el dia correspondiente para la fecha: "))
mes = int(input("Ingrese el mes correspondiente para la fecha: "))
año = int(input("Ingrese el año correspondiente para la fecha: "))
es_valido = True
if año < 0:
    print("Ingrese un año válido")
elif año % 4 == 0:
    bisiesto = True
elif año % 4 == 0 and año % 100 == 0:
    bisiesto = True
else:
    bisiesto = False
if dia > 31:
    es_valido = False
elif mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia > 30:
    es_valido = False
elif bisiesto == True and mes == 2 and dia > 29 or bisiesto == False and mes == 2 and dia > 28:
    es_valido = False
else:
    es_valido = True
if es_valido:
    print("La fecha", str(dia)+"/"+str(mes)+"/"+str(año), "es valida")
else:
    print("La fecha", str(dia)+"/"+str(mes)+"/"+str(año), "no es valida")

