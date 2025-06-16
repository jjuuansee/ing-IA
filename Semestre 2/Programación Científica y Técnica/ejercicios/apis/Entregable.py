import requests
import json
from collections import Counter

api_key = 'db815c2f53d68f9b5124dc2116eb73b1'
resultados = []
temperaturas = []
descripciones = []

while True:
    ciudad = input("Ingrese la ciudad (o escriba 'salir' para terminar): ")
    if ciudad.lower() == "salir":
        break

    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'

    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            clima = respuesta.json()
            descripcion = clima["weather"][0]["description"]
            temperatura = clima["main"]["temp"]

            # Agregar el resultado en un diccionario a la lista de resultados para luego meterlo dentro del json
            resultados.append({ciudad: {"descripcion": descripcion, "temperatura": temperatura}})
            # Agregar la temperatura a la lista correspondiente para luego calcular el promedio
            temperaturas.append(temperatura)
            # Agregar la descripción a la lista correspondiente para luego ver cual es la más ocurrente
            descripciones.append(descripcion)

            print(f'Clima en {ciudad}: {descripcion}')
            print(f'Temperatura: {temperatura}°C')
        else:
            # Manejo de error en la consulta a la API
            print(f"Error {respuesta.status_code}: {respuesta.json().get('message', 'Error desconocido')}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")

# Calcular el promedio de las temperaturas, si hay alguna registrada en la lista
if temperaturas:
    promedio = sum(temperaturas) / len(temperaturas)
    print('=================================================================================================================')
    print(f"Temperatura promedio de las ciudades consultadas: {round(promedio)}°C")
else:
    print("No se registraron temperaturas para calcular un promedio.")

# Calcular la descripción de clima más común con el módulo Count
if descripciones:
    contador_descripciones = Counter(descripciones)
    descripcion_mas_comun = contador_descripciones.most_common(1)[0]
    print(f"""La descripción de clima más frecuente fue '{descripcion_mas_comun[0]}' con 
{descripcion_mas_comun[1]} ocurrencias.""")

else:
    print("No se registraron descripciones de clima para calcular la más frecuente.")

# Guardar toda la lista de resultados y el promedio en el archivo JSON
with open('resultados_clima.json', 'w') as archivo:
    json.dump({
        "resultados": resultados,
        "temperatura_promedio": promedio, # type: ignore
        "descripcion_mas_frecuente": {
            "descripcion": descripcion_mas_comun[0], # type: ignore
            "ocurrencias": descripcion_mas_comun[1] # type: ignore
        }
    }, archivo, indent=4)

print("Consulta de clima finalizada y resultados guardados en 'resultados_clima.json'")
print('=================================================================================================================')