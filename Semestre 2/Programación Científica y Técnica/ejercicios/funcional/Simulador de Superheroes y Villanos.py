from functools import reduce

superheroes = [{'nombre':'Chapulin Colorado','poder': 1000},
               {'nombre':'Superman', 'poder': 100},
               {'nombre':'Spiderman', 'poder': 20}]

villanos = [{'nombre':'VAR','poder': 100},
            {'nombre':'Colombianos', 'poder': 49},
            {'nombre':'Leodan Gonzalez', 'poder': 20}]

superheroes_poderosos = list(filter(lambda x: x['poder'] > 49, superheroes))
villanos_poderosos = list(filter(lambda x: x['poder'] > 49, villanos))

superheroes_entrenados = list(map(lambda x: {'nombre': x['nombre'], 'poder': x['poder'] * 1.1}, superheroes_poderosos))
villanos_entrenados = list(map(lambda x: {'nombre': x['nombre'], 'poder': x['poder'] * 1.1}, villanos_poderosos))
print(superheroes_entrenados)
ganador_de_batalla = reduce(lambda x, y: x if x['poder'] > y['poder'] else y, superheroes_entrenados + villanos_entrenados)

print(f'El ganador de la batalla es {ganador_de_batalla['nombre']} con {ganador_de_batalla['poder']} puntos de poder')

