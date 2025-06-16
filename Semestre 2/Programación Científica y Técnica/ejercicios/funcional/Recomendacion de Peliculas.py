from functools import reduce

peliculas = [
    {'nombre': 'El pianista', 'Calificacion': 8, 'Genero': 'Drama', 'Reseña Positiva': True},
    {'nombre': 'Interestelar', 'Calificacion': 9, 'Genero': 'Sci-Fi', 'Reseña Positiva': True},
    {'nombre': 'La sociedad de la Nieve', 'Calificacion': 10, 'Genero': 'Drama', 'Reseña Positiva': False}
    ]

peliculas_de_drama = list(filter(lambda x: x['Genero'] == 'Drama', peliculas))
peliculas_con_reseña_positiva = list(filter(lambda x: x['Reseña Positiva'] == True, peliculas))
#ajustar_calificacion_de_reseñadas = list(map(lambda x: x['Calificacion']+0.5 if x['Reseña Positiva'] == True, peliculas))