import re

def validarURL(url):
    if re.match(r'^\w{4,5}?(//)?(www.)?(\w*)+.(\w*)',url):
        print('Url valida')
    else:
        print('Url invalida')

ejemploValido = 'https://www.example.com'
ejemploValido2 = 'http://example.com'
ejemploValido3 = 'http://example.com'

ejemploNoValido = 'http://'
ejemploNoValido2 = '://example.com'
ejemploNoValido3 = 'example.'

validarURL(ejemploValido)
validarURL(ejemploValido2)
validarURL(ejemploValido3)
print('\n')
validarURL(ejemploNoValido)
validarURL(ejemploNoValido2)
validarURL(ejemploNoValido3)
