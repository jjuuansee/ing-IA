from functools import reduce
youtubers = [
    ('Techworld', 150000, 1200000),
    ('Techtonia', 9000, 80000),
    ('Gamer', 500000, 2500000),
    ('TravelVlog', 60000, 1800000),
    ('Gympro', 200000, 1800000)
]
mas_de_100k_subs = list(filter(lambda x: x[1] >= 100000, youtubers))
print(f'Los youtubers con mas de 100k de suscriptores son: {mas_de_100k_subs}')

youtubers_bonificacion_25_views = list(map(lambda x: (x[0], x[1], round(x[2]*1.25)),filter(lambda x: x[2] >= 1000000, youtubers)))
print(f'Los youtubers con mas de un millon de views recibieron una bonificacion del 25%. Ahora sus views son {youtubers_bonificacion_25_views}')

youtbers_con_mas_de_1m_views = list(filter(lambda x: x[2] >= 1200000, youtubers_bonificacion_25_views))
print(f'Los youtubers bonificados con mas de 1.2M de views son {youtbers_con_mas_de_1m_views}')

total_suscripciones = reduce(lambda x, y: x + y[1], youtubers_bonificacion_25_views, 0)
print(f'El total de suscriptores es de {total_suscripciones}')

total_views = reduce(lambda x, y: x + y[2], youtubers_bonificacion_25_views, 0)
print(f'El total de vistas es de {total_views}')
