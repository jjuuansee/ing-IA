print("MAYOR DE EDAD")
print("=============")
nombre = str(input('Ingrese su nombre: '))
edad = int(input('Ingrese su edad: '))
if 18 > edad > 0:
    print(nombre+', eres menor de edad')
elif edad >= 18:
    print(nombre+', ya eres mayor de edad')
else:
    print(nombre+", ingrese una edad correcta")
