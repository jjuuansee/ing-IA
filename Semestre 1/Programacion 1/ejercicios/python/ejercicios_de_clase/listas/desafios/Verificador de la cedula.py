print("CEDULA URUGUAYA\n===============")

valores_predefinidos = 2987634
def digito_verificador(ci):
    if ci <= 100000 or ci > 9999999:
        return -1
    suma = 0 
    while ci > 0:  #Saca los dígitos de la cédula uno por uno y los multiplica por los
        # digitos de los valores predefinidos
        digito_de_cedula = ci % 10
        ci = ci // 10 
        digito_de_valores_predefinidos = valores_predefinidos % 10
        valores_predefinidos = valores_predefinidos // 10
        suma += digito_de_cedula * digito_de_valores_predefinidos
    digito = suma % 10 
    if digito != 0:
        return 10 - digito
    else:
        return digito


def esValida(ci, digito_verificador_de_usuario):
    return digito_verificador_de_usuario == digito_verificador(ci)


ci = int(input("Ingrese el número de cedula sin digito verificador: "))
digito_verificador_de_usuario = int(input("Ingrese el digito verificador --------------------: "))

if esValida(ci, digito_verificador_de_usuario) == True:
    print("Cedula correcta")
else: 
    print("Cedula incorrecta")
