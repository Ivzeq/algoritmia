'''
Ingresar un número N y validar que sea positivo. Luego:
a. Mostrar los primeros números impares, hasta alcanzar el número ingresado.
b. Informar la suma de esos números impares.
Ejemplo:
· Si se ingresa 5, se debe mostrar 1 3 5 y la suma es 9.
· Si se ingresa 8, se debe mostrar 1 3 5 7 y la suma es 16.
· Si se ingresa -5, se debe pedir otro número.
'''

numeroN = 0

numeroEvaluado = 1
acumuladorImpares = 0
stringFinal = ''

numeroN = int(input('Ingrese un numero positivo\n'))

while(numeroN < 0):
    numeroN = int(input('Numero ingresado incorrecto. Ingrese un numero positivo\n'))

while (numeroEvaluado <= numeroN):
    if (numeroEvaluado % 2 != 0):
        stringFinal += str(numeroEvaluado) + ' '
        acumuladorImpares += numeroEvaluado
    numeroEvaluado += 1

print(stringFinal)
print('La suma de los impares es:', acumuladorImpares)