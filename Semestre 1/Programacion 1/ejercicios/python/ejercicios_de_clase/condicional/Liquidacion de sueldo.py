print("LIQUIDACION DE SUELDO")
print("=====================")
sueldo_acordado = float(input("Ingrese su sueldo acordado:"))
if sueldo_acordado < 0:
    print("El sueldo ingresado es invalido")
else:
    antiguedad = float(input("Ingrese su antiguedad en la empresa: "))
    if antiguedad < 0.0:
        print("La antiguedad en la empresa es invalida")
    else:
        sueldo_final = 0
        if 0 < antiguedad <= 20:
            sueldo_acordado += sueldo_acordado*(antiguedad*0.01)
            sueldo_final = sueldo_acordado
        else:
            sueldo_acordado += sueldo_acordado * (20 * 0.01)
            sueldo_final = sueldo_acordado
        sueldo_final = sueldo_final * 0.89
        sueldo_final = sueldo_final * 0.94
        if sueldo_final > 120000:
            sueldo_final = sueldo_final * 0.75
        elif sueldo_final > 70000 < 120000:
            sueldo_final = sueldo_final * 0.80
        print("Su sueldo liquidado es de:", sueldo_final)
