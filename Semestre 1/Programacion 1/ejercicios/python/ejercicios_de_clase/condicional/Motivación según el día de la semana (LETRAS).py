print("ALGORITMO DIA DE LA SEMANA")
print("==========================")
dia_de_la_semana = str(input("Ingrese el dia de la semana:"))
dia_de_la_semana = dia_de_la_semana.upper()
if dia_de_la_semana == "LUNES":
    print("Hoy coimenza la semana. Animo!")
elif dia_de_la_semana == "VIERNES":
    print("Ya casi termina!")
elif dia_de_la_semana == "SABADO" or dia_de_la_semana == "DOMINGO":
    print("Fin de semana!")
elif dia_de_la_semana == "MARTES" or dia_de_la_semana == "MIERCOLES" or dia_de_la_semana == "JUEVES":
    print("Vamos que se puede!")
else:
    print("El dia ingresado no es valido")
