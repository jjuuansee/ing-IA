import xml.etree.ElementTree as ET
import csv

tree = ET.parse('Verificar Inventario.xml')
root = tree.getroot()

for producto in root.findall('producto'):
	nombre = producto.find('nombre').text
	precio = producto.find('precio').text

	if nombre is None or precio is None:
		print('El producto no tiene nombre o precio')
	else:
		print(f'El nombre es: {nombre} y su precio es: {precio}')

with open('Inventario Verificado.csv', mode='w', encoding='utf-8') as archivo:
	writer = csv.writer(archivo, delimiter=',')

	writer.writerow(['Nombre', 'Precio'])

	for producto in root.findall('producto'):
		nombre = producto.find('nombre').text
		precio = producto.find('precio').text
		writer.writerow([nombre, precio])

