from functools import reduce

deportistas = [{
    'nombre': 'Messi',
    'puntuacion': 100},
    {
        'nombre': 'Ronaldo',
        'puntuacion': 80},
    {
        'nombre': 'Cacha Arevalo Rios',
        'puntuacion': 1000}]
mayor_puntuacion = reduce(lambda x , y: x if x['puntuacion'] > y['puntuacion'] else y, deportistas)
print(f' El deportista con mayor puntuacion es {mayor_puntuacion['nombre']} con {mayor_puntuacion['puntuacion']} puntos')
