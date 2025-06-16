import requests
api_key = '87c2a29f0f67d8cac27f27ab035b6a8b'
base_url = 'https://api.themoviedb.org/3'

def buscar_pelicula(titulo, idioma="en", anio=None, orden_popularidad="desc"):
    url = f"{base_url}/search/movie"
    parametros = {
        "api_key": api_key,
        "query": titulo,
        "language": idioma,
        "year": anio,
        "sort_by": f"popularity.{orden_popularidad}"
    }
    try:
        respuesta = requests.get(url, params=parametros)
        respuesta.raise_for_status()
        datos = respuesta.json()
    # Verificar si hay resultados
        if datos["results"]:
            for pelicula in datos["results"][::]:
                print(f"Título: {pelicula['title']}, Fecha de lanzamiento: {pelicula.get('release_date')}")
        else:
            print("No se encontraron resultados para esa búsqueda.")

    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud:", e)

buscar_pelicula('Harry Potter')