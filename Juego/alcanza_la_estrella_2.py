import random
import os
import time

# Preguntas y respuestas
preguntas = {
    "¿Cuál es el océano más grande?": "a",
    "¿Quién escribió 'El Quijote'?": "b",
    "¿En qué año llegó el hombre a la luna?": "c",
    "¿Cuál es el ave que representa la libertad?": "a",
    "¿Cuál es el animal más grande del mundo?": "b",
    "¿Quién fue el primer presidente de Estados Unidos?": "c",
    "¿Quién pintó 'La última cena'?": "a",
    "¿En qué ciudad se encuentra la Torre Eiffel?": "b",
    "¿Cuál es el país más poblado del mundo?": "c",
    "¿Cuál es el continente más pequeño?": "a"
}

# Tablero
tablero = [" ", " ", " ", " ", " ",
           " ", " ", " ", " ", " ",
           " ", " ", " ", " ", " ",
           " ", " ", " ", " ", " ",
           " ", " ", " ", " ", " "]

# Castigos
castigos = {
    "Puente": -3,
    "Resbalón": -2,
    "Calavera": -19
}

def lanzar_dado():
    input("Presione ENTER para lanzar el dado.")
    # Genera un número aleatorio del 1 al 6
    resultado = random.randint(1, 6)
    print("El resultado del dado es:", resultado)
    return resultado

# crear una matriz de 4x5
matriz = [[0 for j in range(5)] for i in range(4)]
for i in range(4):
    for j in range(5):
        print(matriz[i][j], end=" ")
    print()