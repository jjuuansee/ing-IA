import pygame
import render
import config
import random


# Esta función se encarga de crear una matriz vacía de tamaño NxN donde N es config.LARGO_TABLERO
def crear_tablero_minas():
    tablero = []
    for a in range(config.LARGO_TABLERO):
        fila = []
        for b in range(config.LARGO_TABLERO):
            fila.append(0)
        tablero.append(fila)
    return tablero


# Esta función es la encargada de crear una matriz vacía de tamaño NxN donde N es config.LARGO_TABLERO
def crear_tablero_revelado():
    tablero = []
    for a in range(config.LARGO_TABLERO):
        fila = []
        for b in range(config.LARGO_TABLERO):
            fila.append(False)
        tablero.append(fila)
    return tablero


# Esta función es la encargada de ingresar la cantidad de bombas que es definida en config.NUM_MINAS
def plantar_bombas(tablero):
    num_bombas = 0
    while num_bombas < config.NUM_MINAS:
        fila = random.randint(0, config.LARGO_TABLERO - 1)
        columna = random.randint(0, config.LARGO_TABLERO - 1)
        if tablero[fila][columna] != -1:
            tablero[fila][columna] = -1
            num_bombas += 1
    return tablero


# La siguiente función es la encargada de definir, para cada celda sin una bomba, cuantas bombas hay en
# las celdas de alrededor. El resultado se guarda en la misma celda.
def calcular_adyacentes(tablero):
    for fila in range(config.LARGO_TABLERO):  # Iteración en cada fila del tablero
        for columna in range(config.LARGO_TABLERO):  # Lo mismo en cada columna
            if tablero[fila][columna] != -1:  # Si la celda no tiene una bomba
                cont_bomb = 0  # Contador de bombas adyacentes
                for a in range(max(0, fila - 1), min(config.LARGO_TABLERO, fila + 2)):  # Iteración sobre las filas adyacentes, considerando los límites.
                    for b in range(max(0, columna - 1), min(config.LARGO_TABLERO, columna + 2)):  # Lo mismo con las columnas adyacentes y los límites del tablero
                        if tablero[a][b] == -1:  # Si una celda adyacente tiene una bomba
                            cont_bomb += 1  # El contador aumenta
                tablero[fila][columna] = cont_bomb  # Asigna el contador a la celda actual dle tablero.
    return tablero


def revelar_celdas(fila, columna, tablero_minas, tablero_revelado):
    # Recibe una fila y una columna (la celda donde el jugador hizo click) y la "revela", o sea,
    # cambia la celda correspondiente en tablero_revelado a "True".
    # Si la celda de tablero_minas es -1, entonces la función devuelve -1.
    # Si la celda estaba vacía (0 u otro número positivo), entonces devuelve 0.
    # Si se revelaron todas las celdas vacías, entonces devuelve 1.
    if tablero_minas[fila][columna] == -1:  # Si el usuario apretó una bomba
        for f in range(config.LARGO_TABLERO):   # recorre cada fila y columna en buca de las otras bombas
            for c in range(config.LARGO_TABLERO):
                if tablero_minas[f][c] == -1:   # y las muestra.
                    tablero_revelado[f][c] = True
        return -1

    revisar_celdas = [(fila, columna)]  #Lista que contiene la celda elegida por el usuario
    while revisar_celdas:  #Se espera que se revisen la mayor cantidad de celdas.
        f, c = revisar_celdas.pop()  #Se separa una celda en específico
        if not tablero_revelado[f][c]:  #Si no se reveló dicha celda
            tablero_revelado[f][c] = True  #Se marca como revelada
            if tablero_minas[f][c] == 0:  # si no tiene bombas a su alrededor
                for a in range(max(0, f - 1), min(config.LARGO_TABLERO, f + 2)):  # Iteración en filas y celdas adyacentes
                    for b in range(max(0, c - 1), min(config.LARGO_TABLERO, c + 2)):  # considerando los límites del tablero
                        if not tablero_revelado[a][b] and (a, b) not in revisar_celdas:
                            revisar_celdas.append((a, b))  # Si la celda adyacente no ha sido revelada ni revisada se añade a la lista para hacerlo pronto

    for f in range(config.LARGO_TABLERO):
        for c in range(config.LARGO_TABLERO):
            if tablero_minas[f][c] != -1 and not tablero_revelado[f][c]:
                return 0  #Retorna la continuidad del juego
    return 1


# ======================================
# A partir de acá no se puede modificar
# ======================================


if __name__ == "__main__":  # Esto es solo para indicarle a Pycharm que arranque la ejecución por acá.
    # Configuración inicial
    tablero_minas = crear_tablero_minas()  # Matriz de enteros, que representa el tablero de juego
    tablero_revelado = crear_tablero_revelado()  # Matriz de booleanos, que representa si cada celda está revelada o no.
    plantar_bombas(tablero_minas)  # Agregamos las minas de forma aleatoria
    calcular_adyacentes(tablero_minas)  # Agregamos los números en las celdas

    # Bucle principal del juego
    juego_terminado = 0
    while juego_terminado == 0:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                render.salir("")  # Salimos antes de tiempo.
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Funciona solo cuando se apreta el click izq del mouse
                fila = pygame.mouse.get_pos()[1] // config.CELL_SIZE
                columna = pygame.mouse.get_pos()[0] // config.CELL_SIZE
                juego_terminado = revelar_celdas(fila, columna, tablero_minas, tablero_revelado)

        # Dibuja el tablero
        # Si quieren agregar una imagen de fondo, descárgenla y pongan la ruta en config.imagen_fondo
        render.dibujar_tablero(tablero_minas, tablero_revelado)

    # Salimos
    if juego_terminado == -1:
        render.salir("¡PERDISTE!")
    else:
        render.salir("¡GANASTE!")