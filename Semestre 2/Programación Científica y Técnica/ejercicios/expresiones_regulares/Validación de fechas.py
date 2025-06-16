import re
fecha = '29/08/2024'
fecha2 = '15/02/2006'
fecha3 = '32/05/2021'
fecha4 = '12/13/2021'


def validar_fecha(fecha):
    if re.match(r'(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/(\d{4})', fecha):
        return 'Fecha valida'
    else:
        return 'Fecha invalida'


print(validar_fecha(fecha))
print(validar_fecha(fecha2))
print(validar_fecha(fecha3))
print(validar_fecha(fecha4))
