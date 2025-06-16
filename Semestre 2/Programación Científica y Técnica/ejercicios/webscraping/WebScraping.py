import re
import requests

sitio = 'http://tienda.valitoburgers.com.uy/'
resultado = requests.get(sitio)
resultado_html = resultado.text

patron = r'<h3 class=" font-bold capitalize text-body md:text-sm "\s*>(.*?)</h3>'
hambuerguesas = re.findall(patron, str(resultado_html))
lista_hambuerguesas = list(set(hambuerguesas))

exclusiones = [
    'promo', 'pepsi', '7 up', '7up', 'lata', 'lata', '500cc', '1.5 lts',
    'salus', 'frutte', 'tonica', 'pomelo', 'manzana', 'limonada',
    'fritas', 'cheese sticks', 'guarnicion', 'porción', 'aros de cebolla'
]
hambuerguesas_filtradas = []

for nombre_ham in lista_hambuerguesas:
    for elem_exlu in exclusiones:
        if elem_exlu in nombre_ham:
            nombre_ham = nombre_ham.replace(elem_exlu, '')
    hambuerguesas_filtradas.append(nombre_ham.strip())

# Elimina el quinto elemento de la lista
if len(hambuerguesas_filtradas) >= 5:
    hambuerguesas_filtradas.pop(4)

print(hambuerguesas_filtradas)
