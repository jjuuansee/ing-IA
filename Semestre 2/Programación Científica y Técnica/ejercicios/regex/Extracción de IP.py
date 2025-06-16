import re
texto = 'El servidor 192.168.1.1 respondió, pero 10.0.0.5 no esta disponible'
print(re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', texto))
