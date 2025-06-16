import json
diccionario = {
    "Libro": [
        {"Nombre": "Fahrenheit 451", "Autor": "Ray Bradbury", "Publicacion": "1953", "Tipo": "Novela"},
        {"Nombre": "La divina comedia", "Autor": "Dante Alighieri", "Publicacion": "Desconocido", "Tipo": "Poema"}
    ]
}
with open('libro.json', mode='w', encoding='utf-8') as archivo:
    json.dump(diccionario, archivo, indent=4)
