import re
texto = 'ATH12345'
if re.match(r'^(ATH)+\d{5}', texto):
    print('Valido')
else:
    print('No')