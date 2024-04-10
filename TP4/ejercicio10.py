'''
Ejercicio 10: El factorial de un número entero N mayor que cero se define como el producto
de todos los enteros X tales que 0 < X <= N. Desarrollar un programa para calcular
el factorial de un número dado. Deberán rechazarse las entradas inválidas
(menores que 0).
'''

factorialN = int(input('Ingrese un numero entero a evaluar como factorial \n'))
if factorialN <0:
    while factorialN <0:
        factorialN = int(input('Ingrese un numero entero a evaluar como factorial \n'))

factorActual = 1
resultadoFactorial = 1


while factorActual <= factorialN:
    resultadoFactorial *= factorActual
    factorActual += 1

print('El factorial de', factorialN, 'es', resultadoFactorial)