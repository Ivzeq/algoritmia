'''
Crear tres conjuntos:
•	pares: valores pares entre 0 y 100
•	impares: valores impares entre 0 y 100
•	azar: 50 valores al azar entre 0 y 100

Una vez generados los tres conjuntos, deberá realizar las siguientes acciones:
•	generar dos nuevos conjuntos: uno con la intersección entre azar y pares; y azar e impares. 
  Informe de cada uno de ellos: la cantidad, el valor máximo y mínimo.

'''
from random import randint

pares = {element for element in range (0,100) if element%2 == 0}
impares = {element for element in range (0,100) if element%2 != 0}
random = set()

while(len(random) != 50):
  random.add(randint(0,100))

azarPares = pares & random
azarImpares = impares & random

print('La cantidad de elementos en comun entre los pares y los random es:', len(azarPares))
print('El valor maximo en comun entre los pares y los random es:', max(azarPares))
print('El valor minimo en comun entre los pares y los random es:', min(azarPares))
print('------------------------------------------------------------------')

print('La cantidad de elementos en comun entre los impares y los random es:', len(azarImpares))
print('El valor maximo en comun entre los impares y los random es:', max(azarImpares))
print('El valor minimo en comun entre los impares y los random es:', min(azarImpares))
print('------------------------------------------------------------------')