import re
texto = 'En el año 2023, compré 3 libros por 15$ cada uno.'
print(re.findall(r'\d+', texto))

