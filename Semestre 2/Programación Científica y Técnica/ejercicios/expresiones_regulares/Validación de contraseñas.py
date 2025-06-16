import re
from xml.etree.ElementPath import xpath_tokenizer_re


def validador_de_contraseñas(contraseña):
    if re.search(r'[0-9]',contraseña) and re.search(r'[A-Z]',contraseña) and re.search(r'[a-z]',contraseña) and re.search(r'[@#$%^&*()!]',contraseña):
        print('Contraseña valida')
    else:
        print('Contraseñas no valida')

contrasenaValida = 'Ju4n$e'
contrasenaValida1 = 'Segura123!'
contrasenaNoValida = 'Juanse!'
contrasenaNoValida2 = 'Pa$$word'
(validador_de_contraseñas(contrasenaValida))
(validador_de_contraseñas(contrasenaValida1))
(validador_de_contraseñas(contrasenaNoValida))
(validador_de_contraseñas(contrasenaNoValida2))
