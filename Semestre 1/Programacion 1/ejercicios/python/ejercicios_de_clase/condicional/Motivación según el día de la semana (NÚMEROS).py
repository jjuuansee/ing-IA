print("ALGORITMO DIA DE LA SEMANA")
print("==========================")
print("El numero que le corrsponde al Lunes es el 1")
print("El numero que le corrsponde al Martes es el 2")
print("El numero que le corrsponde al Miercoles es el 3")
print("El numero que le corrsponde al Jueves es el 4")
print("El numero que le corrsponde al Viernes es el 5")
print("El numero que le corrsponde al Sabado es el 6")
print("El numero que le corrsponde al Domingo es el 7")
print("=================================================")
dia_de_la_semana = int(input("Ingrese el numero correspondiente al dia de la semana:"))
if dia_de_la_semana == 1:
    print("Hoy coimenza la semana. Animo!")
elif dia_de_la_semana == 5:
    print("Ya casi termina!")
elif dia_de_la_semana == 6 or dia_de_la_semana == 7:
    print("Fin de semana!")
elif dia_de_la_semana == 3 or dia_de_la_semana == 4 or dia_de_la_semana == 2:
    print("Vamos que se puede!")
else:
    print("El dia ingresado no es valido")
