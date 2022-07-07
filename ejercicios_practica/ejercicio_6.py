# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

from itertools import count
from pickle import APPEND
from typing import Counter


inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))

cantidad_numeros_positivos = 0  # Inicializo el contador en 0
cantidad_numeros_negativos = 0

numeros_negativos = []
numeros_positivos = []

# for ... in range(....)

for h in range(inicio,fin + 1):
    if h < 0:
        numeros_negativos.append(h)

    elif h >= 0:
        numeros_positivos.append(h)

# Imprimir el valor de la cantidad de números positivos y negativos

print('La cantidad de numeros negativos es:', len(numeros_negativos))
print('La cantidad de numeros positivos es:', len(numeros_positivos))

print("terminamos!")
