# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

from itertools import count


notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Similar al ejercicio de "calificaciones":

Debe caluclar el promedio de todas las notas que se encuentra
almacenadas en una lista llamada "notas" que ya
hemos definido al comienzo del archivo

Luego transformar la califiación en una letra
según la siguiente escala:
- Si el puntaje es mayor igual a 90 --> imprimir A
- Si el puntaje es mayor igual a 80 --> imprimir B
- Si el puntaje es mayor igual a 70 --> imprimir C
- Si el puntaje es mayor igual a 60 --> imprimir D
- Si el puntaje es menor a  60      --> imprimir F

A medida que recorre las notas, no debe considerar como válidas aquellas
que son negativas, en ese caso el alumno estuvo ausente

Debe contar la cantidad de notas válidas y la cantidad de ausentes
'''

print("Mi organizador académico (#_#)")
# Empezar aquí la resolución del ejercicio

# Para calcular el promedio primero debe obtener la suma
# de todas las notas, que irá almacenando en esta variable
sumatoria = 0           # Ya le hemos inicializado en 0
cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró


cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

# Realice aquí el bucle para recorrer todas las notas
# y cacular la sumatoria

notas_validas = []
notas_ausentes = []

for h in notas:
    sumatoria += h 
    
    if h > 0:
        notas_validas.append(h)
        cantidad_notas = len(notas_validas)


    else:
        notas_ausentes.append(h)
        cantidad_ausentes = len(notas_ausentes)


# Terminado el bucle calcule el promedio como
# promedio = sumatoria / cantidad_notas

promedio = sumatoria / cantidad_notas

# Utilice la nota promedio calculada y transformela
# a calificación con letras, imprima en pantalla el resultado

if promedio >= 90:
    print('La nota es A')

elif promedio >= 80:
    print('La nota es B')

elif promedio >= 70:
    print('La nota es C')

elif promedio >= 60:
    print('La nota es D')

elif promedio < 60:
    print('La nota es F')

# Imprima en pantalla al cantidad de ausentes

print('La cantidad de ausentes fue de:', cantidad_ausentes)