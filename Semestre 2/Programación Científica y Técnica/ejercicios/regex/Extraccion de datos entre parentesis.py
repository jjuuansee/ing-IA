import re
texto = 'Los resultados (2023) fueron mejores que los del año anterior (2022).'
print(re.findall(r'\((.*?)\)', texto))
# \( y \) busca los parentesis
# (.*?) Coincide con todos los caracteres dentro del parentesis y deja de coincidir con
# caracteres cuando se cierra el parentesis. A esto se le llama busqueda codiciosa

