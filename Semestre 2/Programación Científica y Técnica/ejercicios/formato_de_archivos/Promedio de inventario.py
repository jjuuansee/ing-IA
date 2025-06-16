import xml.etree.ElementTree as ET

tree = ET.parse('Inventario.xml')
root = tree.getroot()

promedio = 0
total_productos = 0


for producto in root.findall('producto'):
    precio = float(producto.find('precio').text)
    promedio += precio
    total_productos += 1

promedio_total = promedio / total_productos


etiqueta_promedio = ET.Element('promedio')
etiqueta_promedio.text = f'{promedio_total:.2f}'

root.append(etiqueta_promedio)

# Guardar el archivo XML con la nueva etiqueta
tree.write('Inventario_con_promedio.xml', encoding='utf-8', xml_declaration=True)

print("El promedio total se ha añadido al archivo XML.")
