import xml.etree.ElementTree as ET

arbol = ET.parse('Inventario.xml')
raiz = arbol.getroot()

for producto in raiz.findall('producto'):
    nombre = producto.find('nombre').text
    categoria = producto.find('categoria').text
    precio = producto.find('precio').text
    print(f'Nombre: {nombre} | Categoria: {categoria} | Precio: {precio}')
