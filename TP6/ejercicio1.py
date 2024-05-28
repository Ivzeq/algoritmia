'''
Escribir una función que reciba como parámetros dos números enteros. Calcular
y devolver el resultado de la multiplicación de ambos valores utilizando solamente
sumas. Por ejemplo 4 * 3 = 4 + 4 + 4
'''


def multiplicacion_factores(factor1,factor2):
    producto = 0
    for i in range(factor2):
        producto += factor1 

    return producto