import re

def validar_telefono(numero):
    if re.match(r'^\+?(\d{1,3})?\s?\d{9,12}$', numero):
        # ^ indica el inicio de la cadena
        # \+? Puede comenzar con un + o no
        # (\d{1,3})? Puede cotener un grupo de 1 a 3 digitos
        # \s? Puede tener un espacio
        # \d{9,12}$ Hay 9 a 12 digitos despues de todo lo anterior
        print('Número válido')
    else:
        print('Número inválido')

Valido1 = '+598 091253046'
Valido2 = '34 678123456'
Valido3 = '123456789012'
NoValido = '12345'
NoValido2 = '+123456'
NoValido3 = '+12 345'

validar_telefono(Valido1)
validar_telefono(Valido2)
validar_telefono(Valido3)
validar_telefono(NoValido)
validar_telefono(NoValido2)
validar_telefono(NoValido3)
