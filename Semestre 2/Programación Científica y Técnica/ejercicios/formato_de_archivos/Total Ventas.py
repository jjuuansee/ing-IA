import csv
import json
import xml.etree.ElementTree as ET

with open('Ventas.csv', mode='r', encoding='utf-8') as archivo:
    archivo = csv.reader(archivo)
    encabezado = next(archivo)

    total_A = 0
    total_B = 0
    total_C = 0

    for row in archivo:
        if row[0] == 'Producto A':
            total_A += int(row[2])
        elif row[0] == 'Producto B':
            total_B += int(row[2])
        else:
            total_C += int(row[2])

with open('TotalVentas.json', mode='w', encoding='utf-8') as archivo_json:
    totales = {'Total A': total_A, 'Total B': total_B, 'Total C': total_C}
    json.dump(totales, archivo_json, indent=4, ensure_ascii=False)

root = ET.Element('TotalVentas')

producto_a = ET.SubElement(root, 'ProductoA')
producto_a.text = str(total_A)

producto_b = ET.SubElement(root, 'ProductoB')
producto_b.text = str(total_B)

producto_c = ET.SubElement(root, 'ProductoC')
producto_c.text = str(total_C)

tree = ET.ElementTree(root)
tree.write('TotalVentas.xml', encoding='utf-8', xml_declaration=True)
