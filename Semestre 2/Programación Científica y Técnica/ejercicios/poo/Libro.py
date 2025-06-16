class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def __str__(self):
        return f'{self.titulo} el libro de {self.autor} con un costo de {self.precio}'


libro1 = Libro('El aguila blanca', 'Juansito', '69')
print(libro1)