print("HORAS ANTERIORES Y POSTERIORES")
print("==============================")
hora1 = int(input("Ingrese la primer hora: "))
hora2 = int(input("Ingrese la segunda hora: "))
if hora1 < 0 or hora1 > 23 or hora2 < 0 or hora2 > 23:
    print("Las horas ingresadas son invalidas")
else:
    minuto1 = int(input("Ingrese los minutos de la primer hora: "))
    minuto2 = int(input("Ingrese los minutos de la segunda hora: "))
    if minuto1 < 0 or minuto1 > 59 or minuto2 < 0 or minuto2 > 59:
        print("Los minutos ingresados son invalidos")
    else:
        segundo1 = int(input("Ingrese los segundos de la primer hora: "))
        segundo2 = int(input("Ingrese los segundos de la segunda hora: "))
        if segundo1 < 0 or segundo1 > 59 or segundo1 < 0 or segundo1 > 59:
            print("Los segundos ingresados son invalidos")
        elif hora1 < hora2:
            print("La primer hora ingresada es anterior a la segunda hora")
        elif hora1 == hora2 and minuto1 < minuto2:
            print("La primer hora ingresada es anterior a la segunda hora")
        elif hora1 == hora2 and minuto1 == minuto2 and segundo1 < segundo2:
            print("La primer hora ingresada es anterior a la segunda hora")
        elif hora1 == hora2 and minuto1 == minuto2 and segundo1 == segundo2:
            print("La primer hora ingresada es igual a la segunda hora")
        else:
            print("La primer hora ingresada es posterior a la segunda hora ingresada")