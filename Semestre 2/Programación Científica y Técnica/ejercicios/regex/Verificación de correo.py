import re

correo_bien = 'juanparoli14@gmail.com'
correo_mal = ('hola{Mundo}@pedrito.com')


def verificar_correo(correo):
    if re.match(r'[\w-]+@[\w-]+\.[\w-]{3}', correo):
        return("Correo válido")
    else:
        return("Correo inválido")


print(verificar_correo(correo_bien))
print(verificar_correo(correo_mal))
